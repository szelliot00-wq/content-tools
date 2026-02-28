#!/usr/bin/env python3
"""
YouTube video summarizer: fetch transcripts and generate key insights.
Configure creators in creators.json; transcripts go to transcripts/, summaries to summaries/.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# Optional: Google Gemini for summaries
try:
    from google import genai as google_genai
except ImportError:
    google_genai = None

try:
    from youtube_transcript_api import YouTubeTranscriptApi
except ImportError:
    YouTubeTranscriptApi = None

SCRIPT_DIR = Path(__file__).resolve().parent
TRANSCRIPTS_DIR = SCRIPT_DIR / "transcripts"
SUMMARIES_DIR = SCRIPT_DIR / "summaries"
CONFIG_PATH = SCRIPT_DIR / "creators.json"


def load_creators():
    with open(CONFIG_PATH, encoding="utf-8") as f:
        return json.load(f)["creators"]


def get_enabled_creators():
    return [c for c in load_creators() if c.get("enabled", True)]


def get_channel_video_ids(channel_url: str, max_videos: int = 50) -> list[dict]:
    """Use yt-dlp to get video IDs and titles from a channel. Returns list of {id, title}."""
    cmd = [
        sys.executable,
        "-m",
        "yt_dlp",
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
        print("yt-dlp not found. Install with: pip install yt-dlp (or brew install yt-dlp)", file=sys.stderr)
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
        print("youtube-transcript-api not installed. Run: pip install youtube-transcript-api", file=sys.stderr)
        return None
    try:
        api = YouTubeTranscriptApi()
        fetched = api.fetch(video_id)
        if fetched is None:
            return None
        # New API: FetchedTranscript with .snippets (FetchedTranscriptSnippet with .text)
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


def _build_prompt(transcript: str, video_title: str, category: str | None) -> str:
    if category == "product_management":
        return f"""Summarize this product management YouTube video transcript in detail.

Video title: {video_title}

Transcript:
{transcript}

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
{transcript}

Provide your response in this exact format:

## Summary
(2–4 sentences describing what the video covers.)

## Key insights
- (Bullet 1)
- (Bullet 2)
- (… more as needed)
"""


def summarize_with_gemini(transcript: str, video_title: str, category: str | None = None) -> str | None:
    if not google_genai:
        return None
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return None
    client = google_genai.Client(api_key=api_key)
    # Truncate very long transcripts to stay within context
    max_chars = 120_000
    if len(transcript) > max_chars:
        transcript = transcript[:max_chars] + "\n\n[Transcript truncated...]"
    prompt = _build_prompt(transcript, video_title, category)
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        return (response.text or "").strip()
    except Exception as e:
        print(f"  Gemini error: {e}", file=sys.stderr)
        return None


def write_summary_fallback(transcript: str, video_title: str) -> str:
    """Fallback when no Gemini key: short extract and note to add API key for full summaries."""
    preview = (transcript[:1500] + "...") if len(transcript) > 1500 else transcript
    return f"""## Summary
(Set GEMINI_API_KEY and install google-genai for AI-generated summaries.)

## Key insights
(Install google-genai and set GEMINI_API_KEY, then re-run to get key insights.)

## Transcript preview
{preview}
"""


def save_summary(creator_id: str, video_id: str, content: str, title: str) -> Path:
    folder = SUMMARIES_DIR / creator_id
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"{video_id}.md"
    header = f"# {title}\n\nVideo ID: `{video_id}`\n\n"
    path.write_text(header + content, encoding="utf-8")
    return path


def is_new_creator(creator_id: str) -> bool:
    """Return True if this creator has no existing summaries (i.e. first run)."""
    folder = SUMMARIES_DIR / creator_id
    return not folder.exists() or not any(folder.glob("*.md"))


def process_video(creator_id: str, video_id: str, title: str, refresh: bool, category: str | None = None) -> bool:
    transcript = load_transcript(creator_id, video_id)
    if transcript is None or refresh:
        transcript = fetch_transcript(video_id)
        if transcript is None:
            return False
        save_transcript(creator_id, video_id, transcript)
    summary_path = SUMMARIES_DIR / creator_id / f"{video_id}.md"
    if summary_path.exists() and not refresh:
        print(f"  Skip (have summary): {video_id}")
        return True
    if google_genai and os.environ.get("GEMINI_API_KEY"):
        summary = summarize_with_gemini(transcript, title, category)
    else:
        summary = None
    if not summary:
        summary = write_summary_fallback(transcript, title)
    save_summary(creator_id, video_id, summary, title)
    print(f"  Wrote summary: {video_id} — {title[:50]}...")
    return True


def extract_video_id(url_or_id: str) -> str | None:
    """Extract 11-char video ID from URL or return as-is if it looks like an ID."""
    s = (url_or_id or "").strip()
    if re.match(r"^[\w-]{11}$", s):
        return s
    # Common patterns: ?v=ID, /watch?v=ID, /v/ID, youtu.be/ID
    m = re.search(r"(?:v=|/v/|youtu\.be/)([\w-]{11})", s)
    return m.group(1) if m else None


def run(
    creator_slug: str | None = None,
    max_videos: int = 3,
    refresh: bool = False,
    video_url: str | None = None,
):
    if video_url:
        vid = extract_video_id(video_url)
        if not vid:
            print("Could not parse video ID from URL.", file=sys.stderr)
            return 1
        creator_id = creator_slug or "dave-killeen"
        print(f"Single video mode: {video_url}")
        # Fetch title via yt-dlp for display
        cmd = [sys.executable, "-m", "yt_dlp", "--print", "%(title)s", "--no-warnings", f"https://www.youtube.com/watch?v={vid}"]
        try:
            out = subprocess.run(cmd, capture_output=True, text=True, timeout=30, cwd=SCRIPT_DIR)
            title = (out.stdout or "").strip() if out.returncode == 0 else ""
        except Exception:
            title = ""
        creator_category = next((c.get("category") for c in load_creators() if c.get("id") == creator_id), None)
        process_video(creator_id, vid, title, refresh, creator_category)
        return 0
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
            print("  No videos found. Check channel URL (e.g. https://www.youtube.com/@Handle).")
            continue
        print(f"  Found {len(videos)} videos. Processing up to {effective_max}...")
        category = c.get("category")
        for v in videos[:effective_max]:
            process_video(cid, v["id"], v.get("title", ""), refresh, category)
    return 0


def main():
    import argparse
    p = argparse.ArgumentParser(description="Download YouTube transcripts and summarize (key insights).")
    p.add_argument("--creator", "-c", help="Only process this creator id (e.g. dave-killeen)")
    p.add_argument("--max-videos", "-n", type=int, default=3, help="Max videos per channel (default 3)")
    p.add_argument("--refresh", action="store_true", help="Re-fetch transcript and re-summarize")
    p.add_argument("--video-url", "-v", help="Process a single video by URL (e.g. for testing)")
    args = p.parse_args()
    sys.exit(
        run(
            creator_slug=args.creator,
            max_videos=args.max_videos,
            refresh=args.refresh,
            video_url=args.video_url,
        )
    )


if __name__ == "__main__":
    main()
