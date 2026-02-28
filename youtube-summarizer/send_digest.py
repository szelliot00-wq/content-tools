#!/usr/bin/env python3
"""
youtube-summarizer/send_digest.py — Email digest of newly summarised videos.

Reads the summary files added in the last git commit and sends them via
shared/email.py (the same email module used by article-reader and
competitor-tracker).

Called by run.sh immediately after a successful git push.
"""
from __future__ import annotations

import subprocess
import sys
from datetime import datetime
from pathlib import Path

# Add content-tools root to path so we can import shared.email
_DIR = Path(__file__).resolve().parent        # .../content-tools/youtube-summarizer/
_PROJECT_ROOT = _DIR.parent                    # .../content-tools/
sys.path.insert(0, str(_PROJECT_ROOT))

from shared.email import send_digest  # noqa: E402


def get_new_summary_files() -> list[str]:
    """Return paths of summary .md files added in the last git commit."""
    result = subprocess.run(
        ["git", "diff", "--name-only", "HEAD~1", "HEAD"],
        capture_output=True,
        text=True,
        cwd=_PROJECT_ROOT,
    )
    if result.returncode != 0:
        return []
    return [
        f for f in result.stdout.strip().splitlines()
        if f.startswith("youtube-summarizer/summaries/") and f.endswith(".md")
    ]


def main() -> int:
    new_files = get_new_summary_files()
    if not new_files:
        print("No new summaries to email.")
        return 0

    items = []
    for rel_path in new_files:
        full_path = _PROJECT_ROOT / rel_path
        if not full_path.exists():
            continue

        content = full_path.read_text(encoding="utf-8")
        lines = content.splitlines()

        # First line is "# Video Title"
        title = lines[0].lstrip("# ").strip() if lines else "Unknown"

        # Extract video ID from "Video ID: `abc123`"
        video_id = None
        for line in lines[:5]:
            if "Video ID:" in line and "`" in line:
                video_id = line.split("`")[1]
                break

        # Creator name from directory: youtube-summarizer/summaries/{creator-id}/file.md
        parts = rel_path.split("/")
        creator_id = parts[2] if len(parts) > 2 else "unknown"
        creator_name = creator_id.replace("-", " ").title()

        # Body is everything after the "Video ID:" header line
        body_lines: list[str] = []
        past_header = False
        for line in lines:
            if not past_header:
                if line.startswith("Video ID:"):
                    past_header = True
                continue
            body_lines.append(line)

        items.append({
            "title": f"{title} — {creator_name}",
            "content": "\n".join(body_lines).strip(),
            "url": f"https://youtube.com/watch?v={video_id}" if video_id else None,
        })

    if not items:
        print("No valid summaries found.")
        return 0

    subject = f"📺 {len(items)} new YouTube summary(ies) — {datetime.now().strftime('%b %d')}"
    send_digest(subject=subject, items=items)
    return 0


if __name__ == "__main__":
    sys.exit(main())
