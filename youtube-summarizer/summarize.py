#!/usr/bin/env python3
"""
YouTube video summarizer: fetch transcripts and generate key insights.
Configure creators in creators.json; transcripts go to transcripts/, summaries to summaries/.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
TRANSCRIPTS_DIR = SCRIPT_DIR / "transcripts"
SUMMARIES_DIR = SCRIPT_DIR / "summaries"
CONFIG_PATH = SCRIPT_DIR / "creators.json"

sys.path.insert(0, str(PROJECT_DIR))
from shared import summarizer
from shared.email import send_digest

try:
    from youtube_transcript_api import YouTubeTranscriptApi
except ImportError:
    YouTubeTranscriptApi = None


def load_creators():
    with open(CONFIG_PATH, encoding="utf-8") as f:
        return json.load(f)["creators"]


def get_enabled_creators():
    return [c for c in load_creators() if c.get("enabled", True)]


def get_channel_video_ids(channel_url: str, max_videos: int = 50) -> list[dict]:
    """Use yt-dlp to get video IDs and titles from a channel."""
    cmd = [
        sys.executable, "-m", "yt_dlp",
        "--flat-playlist",
        "--print", "%(id)s\t%(title)s",
        "--no-warnings",
        "--max-downloads", str(max_videos),
        channel_url,
    ]
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=120, check=True, cwd=SCRIPT_DIR)
    except subprocess.CalledProcessError as e:
        print(f"yt-dlp error for {channel_url}: {e.stderr or e}", file=sys.stderr)
        return []
    except FileNotFoundError:
        print("yt-dlp not found. Install with: pip install yt-dlp", file=sys.stderr)
        return []

    videos = []
    for line in out.stdout.strip().splitlines():
        parts = line.split("\t", 1)
        vid = (parts[0] or "").strip()
        title = (parts[1] or "").strip() if len(parts) > 1 else ""
        if vid and re.match(r"^[\w-]{11}$", vid):
            videos.append({"id": vid, "title": title})
    return videos


def fetch_transcript(video_id: str) -> str | None:
    if not YouTubeTranscriptApi:
        print("youtube-transcript-api not installed.", file=sys.stderr)
        return None
    try:
        api = YouTubeTranscriptApi()
        fetched = api.fetch(video_id)
        if fetched is None:
            return None
        snippets = getattr(fetched, "snippets", None) or []
        return " ".join(getattr(s, "text", str(s)) for s in snippets).replace("\n", " ")
    except Exception as e:
        print(f"  Transcript failed for {video_id}: {e}", file=sys.stderr)
        return None


def save_transcript(creator_id: str, video_id: str, text: str) -> Path:
    folder = TRANSCRIPTS_DIR / creator_id
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"{video_id}.txt"
    path.write_text(text, encoding="utf-8")
    return path


def load_transcript(creator_id: str, video_id: str) -> str | None:
    path = TRANSCRIPTS_DIR / creator_id / f"{video_id}.txt"
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")


def _build_prompt_template(video_title: str, category: str | None) -> str:
    if category == "product_management":
        return f"""Summarize this product management YouTube video transcript in detail.

Video title: {video_title}

Transcript:
{{content}}

Provide your response in this exact format:

## Summary
(3–5 sentences describing what the video covers, the core argument or framework, and who it is most relevant to.)

## Key insights
- (Bullet 1)
- (Bullet 2)
- (… more as needed — be thorough, include specifics, numbers, and examples from the video)

## Use cases
(List specific situations, roles, or problems where the advice or framework in this video applies. Use bullet points.)

## Patterns & frameworks
(Call out any named frameworks, mental models, processes, or repeatable patterns discussed. For each, briefly describe what it is and how it works.)
"""
    return f"""Summarize this YouTube video transcript and extract key insights.

Video title: {video_title}

Transcript:
{{content}}

Provide your response in this exact format:

## Summary
(2–4 sentences describing what the video covers.)

## Key insights
- (Bullet 1)
- (Bullet 2)
- (… more as needed)
"""


def save_summary(creator_id: str, video_id: str, content: str, title: str) -> Path:
    folder = SUMMARIES_DIR / creator_id
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"{video_id}.md"
    header = f"# {title}\n\nVideo ID: `{video_id}`\n\n"
    path.write_text(header + content, encoding="utf-8")
    return path


def is_new_creator(creator_id: str) -> bool:
    folder = SUMMARIES_DIR / creator_id
    return not folder.exists() or not any(folder.glob("*.md"))


def process_video(
    creator_id: str, video_id: str, title: str, refresh: bool, category: str | None = None
) -> dict | None:
    """Process one video. Returns digest item dict if a new summary was created, else None."""
    transcript = load_transcript(creator_id, video_id)
    if transcript is None or refresh:
        transcript = fetch_transcript(video_id)
        if transcript is None:
            return None
        save_transcript(creator_id, video_id, transcript)

    summary_path = SUMMARIES_DIR / creator_id / f"{video_id}.md"
    if summary_path.exists() and not refresh:
        print(f"  Skip (have summary): {video_id}")
        return None

    template = _build_prompt_template(title, category)
    summary = summarizer.summarize(transcript, template)
    if not summary:
        print(f"  Claude unavailable for {video_id} — skipping, will retry next run")
        return None

    save_summary(creator_id, video_id, summary, title)
    print(f"  Wrote summary: {video_id} — {title[:50]}...")

    creator_name = creator_id.replace("-", " ").title()
    return {
        "title": f"{title} — {creator_name}",
        "content": summary,
        "url": f"https://youtube.com/watch?v={video_id}",
    }


def extract_video_id(url_or_id: str) -> str | None:
    s = (url_or_id or "").strip()
    if re.match(r"^[\w-]{11}$", s):
        return s
    m = re.search(r"(?:v=|/v/|youtu\.be/)([\w-]{11})", s)
    return m.group(1) if m else None


def run(
    creator_slug: str | None = None,
    max_videos: int = 3,
    refresh: bool = False,
    video_url: str | None = None,
) -> int:
    new_items: list[dict] = []

    if video_url:
        vid = extract_video_id(video_url)
        if not vid:
            print("Could not parse video ID from URL.", file=sys.stderr)
            return 1
        creator_id = creator_slug or "dave-killeen"
        print(f"Single video mode: {video_url}")
        cmd = [sys.executable, "-m", "yt_dlp", "--print", "%(title)s", "--no-warnings",
               f"https://www.youtube.com/watch?v={vid}"]
        try:
            out = subprocess.run(cmd, capture_output=True, text=True, timeout=30, cwd=SCRIPT_DIR)
            title = (out.stdout or "").strip() if out.returncode == 0 else ""
        except Exception:
            title = ""
        creator_category = next(
            (c.get("category") for c in load_creators() if c.get("id") == creator_id), None
        )
        item = process_video(creator_id, vid, title, refresh, creator_category)
        if item:
            new_items.append(item)
    else:
        creators = get_enabled_creators()
        if creator_slug:
            creators = [c for c in creators if c.get("id") == creator_slug]
        if not creators:
            print("No matching creators. Check creators.json and --creator.", file=sys.stderr)
            return 1
        for c in creators:
            cid = c["id"]
            url = c.get("channel_url", "").strip()
            if not url:
                print(f"Skipping {cid}: no channel_url", file=sys.stderr)
                continue
            new_creator = is_new_creator(cid)
            effective_max = 3 if new_creator else max_videos
            print(f"Channel: {c.get('name', cid)} — {url}{' [new channel, fetching 3]' if new_creator else ''}")
            videos = get_channel_video_ids(url, max_videos=effective_max)
            if not videos:
                print("  No videos found.")
                continue
            print(f"  Found {len(videos)} videos. Processing up to {effective_max}...")
            category = c.get("category")
            for v in videos[:effective_max]:
                item = process_video(cid, v["id"], v.get("title", ""), refresh, category)
                if item:
                    new_items.append(item)

    if new_items:
        date_str = datetime.now().strftime("%b %d")
        send_digest(
            subject=f"📺 {len(new_items)} new YouTube summary(ies) — {date_str}",
            items=new_items,
        )

    return 0


def main():
    import argparse
    p = argparse.ArgumentParser(description="Download YouTube transcripts and summarize.")
    p.add_argument("--creator", "-c", help="Only process this creator id (e.g. dave-killeen)")
    p.add_argument("--max-videos", "-n", type=int, default=3, help="Max videos per channel (default 3)")
    p.add_argument("--refresh", action="store_true", help="Re-fetch transcript and re-summarize")
    p.add_argument("--video-url", "-v", help="Process a single video by URL")
    args = p.parse_args()
    sys.exit(run(
        creator_slug=args.creator,
        max_videos=args.max_videos,
        refresh=args.refresh,
        video_url=args.video_url,
    ))


if __name__ == "__main__":
    main()
