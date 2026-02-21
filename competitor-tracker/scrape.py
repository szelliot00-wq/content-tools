#!/usr/bin/env python3
"""
Competitor Tracker: scrape competitor pages, diff against snapshots, summarize changes, email digest.
Configure competitors in competitors.json; snapshots in snapshots/, summaries in summaries/competitors/.
"""
from __future__ import annotations

import difflib
import json
import re
import sys
from datetime import datetime
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
SNAPSHOTS_DIR = SCRIPT_DIR / "snapshots"
SUMMARIES_DIR = PROJECT_DIR / "summaries" / "competitors"
COMPETITORS_PATH = SCRIPT_DIR / "competitors.json"

# Add project root to path so we can import shared/
sys.path.insert(0, str(PROJECT_DIR))
from shared import summarizer as gemini
from shared import email as mailer

DIFF_THRESHOLD = 50  # minimum characters changed to trigger summary

SUMMARY_PROMPT = """A competitor's website changed. Summarize what's new or different.
Focus on: new features, pricing changes, product updates, new offerings.
Ignore: typos, minor wording tweaks, nav/footer changes.

Changes detected:
{content}

Format your response exactly as:

## What Changed
(1-2 sentences describing the key change.)

## Notable Updates
- (Point 1)
- (Point 2)
- (More as needed)
"""


def load_competitors() -> list[dict]:
    with open(COMPETITORS_PATH, encoding="utf-8") as f:
        data = json.load(f)
    return [c for c in data.get("competitors", []) if c.get("enabled", True)]


def label_slug(label: str) -> str:
    label = label.lower()
    label = re.sub(r"[^\w\s-]", "", label)
    label = re.sub(r"[\s_]+", "-", label)
    return label.strip("-")[:40]


def snapshot_path(competitor_id: str, label: str) -> Path:
    return SNAPSHOTS_DIR / f"{competitor_id}-{label_slug(label)}.txt"


def summary_path(competitor_id: str) -> Path:
    date_str = datetime.now().strftime("%Y-%m-%d")
    return SUMMARIES_DIR / f"{date_str}-{competitor_id}.md"


def fetch_page_text(url: str) -> str | None:
    try:
        resp = requests.get(url, timeout=20, headers={"User-Agent": "Mozilla/5.0"})
        resp.raise_for_status()
    except Exception as e:
        print(f"    Fetch error for {url}: {e}", file=sys.stderr)
        return None

    soup = BeautifulSoup(resp.text, "html.parser")

    # Remove nav, header, footer, script, style elements
    for tag in soup(["nav", "header", "footer", "script", "style", "noscript"]):
        tag.decompose()

    raw = soup.get_text(separator="\n", strip=True)

    # Remove boilerplate: lines under 3 chars or that are just punctuation/whitespace
    lines = [line for line in raw.splitlines() if len(line.strip()) >= 3]
    return "\n".join(lines)


def compute_diff(old_text: str, new_text: str) -> tuple[str, int]:
    """Return (diff_text, changed_char_count)."""
    old_lines = old_text.splitlines(keepends=True)
    new_lines = new_text.splitlines(keepends=True)
    diff = list(difflib.unified_diff(old_lines, new_lines, lineterm=""))
    diff_text = "".join(diff)

    # Count added/removed chars (lines starting with + or -)
    changed = sum(
        len(line[1:])
        for line in diff
        if line.startswith(("+", "-")) and not line.startswith(("+++", "---"))
    )
    return diff_text, changed


def process_url(competitor_id: str, competitor_name: str, url_entry: dict) -> dict | None:
    """
    Fetch, diff, summarize one URL. Returns change summary dict or None if no significant change.
    """
    url = url_entry["url"]
    label = url_entry.get("label", url)
    snap_path = snapshot_path(competitor_id, label)

    print(f"    {label}: {url}")
    new_text = fetch_page_text(url)
    if not new_text:
        return None

    # First run — no snapshot yet
    if not snap_path.exists():
        SNAPSHOTS_DIR.mkdir(parents=True, exist_ok=True)
        snap_path.write_text(new_text, encoding="utf-8")
        print(f"      Snapshot created (first run): {snap_path.name}")
        return None

    old_text = snap_path.read_text(encoding="utf-8")
    diff_text, changed = compute_diff(old_text, new_text)

    if changed < DIFF_THRESHOLD:
        print(f"      No significant change ({changed} chars)")
        return None

    print(f"      Change detected: {changed} chars — summarizing...")

    summary = gemini.summarize(diff_text, SUMMARY_PROMPT)
    if not summary:
        summary = f"## What Changed\n({changed} characters changed — set GEMINI_API_KEY for AI summary.)\n\n## Notable Updates\n- See diff below.\n\n```\n{diff_text[:2000]}\n```"

    # Update snapshot
    snap_path.write_text(new_text, encoding="utf-8")
    print(f"      Snapshot updated: {snap_path.name}")

    return {
        "label": label,
        "url": url,
        "summary": summary,
        "changed": changed,
    }


def run() -> int:
    competitors = load_competitors()
    if not competitors:
        print("No enabled competitors in competitors.json.")
        return 0

    SUMMARIES_DIR.mkdir(parents=True, exist_ok=True)
    digest_items: list[dict] = []

    for competitor in competitors:
        cid = competitor["id"]
        name = competitor["name"]
        print(f"Competitor: {name}")

        changes: list[dict] = []
        for url_entry in competitor.get("urls", []):
            result = process_url(cid, name, url_entry)
            if result:
                changes.append(result)

        if not changes:
            continue

        # Combine all URL changes for this competitor into one summary file
        combined_content = ""
        for change in changes:
            combined_content += f"### {change['label']}\n\n{change['summary']}\n\n---\n\n"

        path = summary_path(cid)
        header = f"# {name} — Changes {datetime.now().strftime('%Y-%m-%d')}\n\n"
        path.write_text(header + combined_content, encoding="utf-8")
        print(f"  Saved summary: {path.name}")

        # One digest item per changed competitor
        digest_items.append({
            "title": f"{name} — website changes detected",
            "content": combined_content,
            "url": competitor.get("urls", [{}])[0].get("url"),
        })

    if not digest_items:
        print("No significant competitor changes detected.")
        return 0

    print(f"\nSending digest with {len(digest_items)} competitor change(s)...")
    date_str = datetime.now().strftime("%b %d")
    subject = f"Competitor Updates — {len(digest_items)} change(s) — {date_str}"
    mailer.send_digest(subject=subject, items=digest_items)
    return 0


def main():
    sys.exit(run())


if __name__ == "__main__":
    main()
