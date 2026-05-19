#!/usr/bin/env python3
"""
Article Reader: fetch RSS feeds and manual URLs, summarize, email digest.
Configure sources in sources.json; summaries go to summaries/articles/.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests

from dotenv import load_dotenv

# Full path required — launchd does not load nvm
AGENT_BROWSER = "/Users/steveelliott/.nvm/versions/node/v24.14.0/bin/agent-browser"

load_dotenv()

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
SUMMARIES_DIR = PROJECT_DIR / "summaries" / "articles"
SOURCES_PATH = SCRIPT_DIR / "sources.json"

# Add project root to path so we can import shared/
sys.path.insert(0, str(PROJECT_DIR))
from shared import summarizer as gemini
from shared import email as mailer

SUMMARY_PROMPT = """Summarize this article and extract key takeaways.

Title: {title}

Content:
{content}

Format your response exactly as:

## Summary
(2-4 sentences describing the article.)

## Key takeaways
- (Point 1)
- (Point 2)
- (More as needed)
"""

CUTOFF_DAYS = 7


def load_sources() -> dict:
    with open(SOURCES_PATH, encoding="utf-8") as f:
        return json.load(f)


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = text.strip("-")
    return text[:80]


def summary_exists(slug: str) -> Path | None:
    """Return path if a summary file with this slug already exists."""
    for p in SUMMARIES_DIR.glob(f"*-{slug}.md"):
        return p
    return None


def summary_path(slug: str) -> Path:
    date_str = datetime.now().strftime("%Y-%m-%d")
    return SUMMARIES_DIR / f"{date_str}-{slug}.md"


def save_summary(title: str, url: str, content: str, slug: str) -> Path:
    SUMMARIES_DIR.mkdir(parents=True, exist_ok=True)
    path = summary_path(slug)
    header = f"# {title}\n\nSource: {url}\n\n"
    path.write_text(header + content, encoding="utf-8")
    return path


def fetch_rss_items(feed: dict) -> list[dict] | None:
    """Return list of {title, url, text} from RSS feed, or None on fetch/parse failure."""
    try:
        import feedparser
    except ImportError:
        print("feedparser not installed.", file=sys.stderr)
        return None

    url = feed.get("url", "")
    max_items = feed.get("max_items", 3)
    cutoff_days = feed.get("cutoff_days", CUTOFF_DAYS)
    cutoff = datetime.now(tz=timezone.utc) - timedelta(days=cutoff_days) if cutoff_days else None

    print(f"  RSS: {feed.get('name', url)}")
    try:
        # Try a plain HTTP request first — fast and no Chrome overhead.
        # If requests returns a parseable feed, use it.  If not (e.g. Cloudflare
        # blocks the request and returns an HTML challenge page), fall back to
        # agent-browser which handles Cloudflare via a real browser session.
        parsed = None
        try:
            resp = requests.get(url, timeout=15, headers={"User-Agent": "Mozilla/5.0"})
            resp.raise_for_status()
            candidate = feedparser.parse(resp.text)
            if not candidate.bozo or candidate.entries:
                parsed = candidate
        except Exception:
            pass  # fall through to agent-browser

        if parsed is None:
            subprocess.run(
                [AGENT_BROWSER, "open", url],
                capture_output=True, text=True, timeout=30, check=True,
            )
            result = subprocess.run(
                [AGENT_BROWSER, "eval", "document.documentElement.outerText"],
                capture_output=True, text=True, timeout=30, check=True,
            )
            parsed = feedparser.parse(json.loads(result.stdout.strip()))
    except Exception as e:
        print(f"    Feed fetch error: {e}", file=sys.stderr)
        return None
    if parsed.bozo and not parsed.entries:
        print(f"    Failed to parse feed: {url}", file=sys.stderr)
        return None

    items = []
    for entry in parsed.entries[:max_items * 3]:  # fetch extra, filter by date
        if len(items) >= max_items:
            break
        raw_id = entry.get("link") or entry.get("id") or ""
        entry_url = raw_id if raw_id.startswith("http") else ""
        entry_title = entry.get("title", "Untitled")

        # Date filtering (skipped if cutoff is None)
        if cutoff:
            pub = entry.get("published_parsed") or entry.get("updated_parsed")
            if pub:
                import calendar
                pub_dt = datetime.fromtimestamp(calendar.timegm(pub), tz=timezone.utc)
                if pub_dt < cutoff:
                    continue

        # Use inline summary content if available and substantial enough to be
        # real article text. Some feeds (e.g. HN) put only short metadata in
        # the summary field; skip_inline forces fetching the linked article.
        skip_inline = feed.get("skip_inline", False)
        inline = entry.get("summary") or entry.get("content", [{}])[0].get("value", "")
        if inline and not skip_inline:
            from bs4 import BeautifulSoup
            text = BeautifulSoup(inline, "html.parser").get_text(separator="\n", strip=True)
            if len(text) < 300:  # too short — likely just metadata, fetch the article
                text = _extract_text(entry_url) or text
        else:
            text = _extract_text(entry_url)
        if not text:
            continue
        items.append({"title": entry_title, "url": entry_url, "text": text})

    print(f"    {len(items)} new items fetched")
    return items


def fetch_manual_urls(manual_urls: list[dict]) -> list[dict]:
    """Return list of {title, url, text} for manually specified URLs."""
    items = []
    for entry in manual_urls:
        url = entry.get("url", "")
        title = entry.get("title", url)
        print(f"  Manual URL: {url}")
        text = _extract_text(url)
        if text:
            items.append({"title": title, "url": url, "text": text})
        else:
            print(f"    Could not extract text from {url}", file=sys.stderr)
    return items


def _extract_text(url: str) -> str | None:
    try:
        subprocess.run(
            [AGENT_BROWSER, "open", url],
            capture_output=True, text=True, timeout=30, check=True,
        )
        result = subprocess.run(
            [AGENT_BROWSER, "snapshot", "-c"],
            capture_output=True, text=True, timeout=30, check=True,
        )
    except subprocess.TimeoutExpired:
        print(f"    Timeout fetching {url}", file=sys.stderr)
        return None
    except subprocess.CalledProcessError as e:
        print(f"    agent-browser error for {url}: {e.stderr}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"    Fetch error for {url}: {e}", file=sys.stderr)
        return None

    lines = [line for line in result.stdout.splitlines() if len(line.strip()) >= 3]
    return "\n".join(lines) or None


def process_item(item: dict) -> dict | None:
    """Summarize one article. Returns digest item dict or None if skipped."""
    title = item["title"]
    url = item["url"]
    text = item["text"]
    slug = slugify(url) if url else slugify(title)

    if summary_exists(slug):
        print(f"    Skip (already summarized): {slug}")
        return None

    prompt = SUMMARY_PROMPT.format(title=title, content="{content}")
    summary = gemini.summarize(text, prompt)
    if not summary:
        summary = f"## Summary\n(Claude unavailable — skipped.)\n\n## Key takeaways\n- See source article."

    path = save_summary(title, url, summary, slug)
    print(f"    Saved: {path.name}")
    return {"title": title, "content": summary, "url": url}


def run() -> int:
    sources = load_sources()
    digest_items: list[dict] = []
    feed_errors: list[str] = []

    # RSS feeds
    for feed in sources.get("rss_feeds", []):
        if not feed.get("enabled", True):
            continue
        items = fetch_rss_items(feed)
        if items is None:
            feed_errors.append(feed.get("name", feed.get("url", "unknown")))
            continue
        for item in items:
            result = process_item(item)
            if result:
                digest_items.append(result)

    # Manual URLs
    for item in fetch_manual_urls(sources.get("manual_urls", [])):
        result = process_item(item)
        if result:
            digest_items.append(result)

    subprocess.run([AGENT_BROWSER, "close", "--all"], capture_output=True)

    if feed_errors:
        print(f"\nFeed errors: {feed_errors} — sending alert...")
        run_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        mailer.send_digest(
            subject=f"⚠️ Article Reader: {len(feed_errors)} feed(s) failed — {run_time}",
            items=[
                {
                    "title": f"❌ {name}",
                    "content": (
                        "This RSS feed could not be fetched or parsed.\n\n"
                        "Check the log on the MacBook Pro:\n\n"
                        "`tail -100 ~/Claude-projects/content-tools/cron.log`"
                    ),
                    "url": None,
                }
                for name in feed_errors
            ],
        )

    if not digest_items:
        print("No new articles to digest.")
        return 0

    print(f"\nSending digest with {len(digest_items)} article(s)...")
    date_str = datetime.now().strftime("%b %d")
    subject = f"Article Digest — {len(digest_items)} new article(s) — {date_str}"
    mailer.send_digest(subject=subject, items=digest_items)
    return 0


def main():
    sys.exit(run())


if __name__ == "__main__":
    main()
