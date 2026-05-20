#!/usr/bin/env python3
"""
Standalone YouTube digest mailer. Pass summary .md file paths as arguments.
(Email is also sent inline by summarize.py during normal runs — this is for manual use only.)
"""
from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_PROJECT_ROOT))
from shared.email import send_digest


def parse_summary_file(path: Path) -> dict | None:
    content = path.read_text(encoding="utf-8")
    lines = content.splitlines()
    title = lines[0].lstrip("# ").strip() if lines else "Unknown"

    video_id = None
    for line in lines[:5]:
        if "Video ID:" in line and "`" in line:
            video_id = line.split("`")[1]
            break

    creator_name = path.parent.name.replace("-", " ").title()

    body_lines: list[str] = []
    past_header = False
    for line in lines:
        if not past_header:
            if line.startswith("Video ID:"):
                past_header = True
            continue
        body_lines.append(line)

    return {
        "title": f"{title} — {creator_name}",
        "content": "\n".join(body_lines).strip(),
        "url": f"https://youtube.com/watch?v={video_id}" if video_id else None,
    }


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: send_digest.py <summary.md> [summary.md ...]")
        return 1
    items = [item for arg in sys.argv[1:] if (item := parse_summary_file(Path(arg)))]
    if not items:
        print("No valid summaries.")
        return 0
    send_digest(
        subject=f"📺 {len(items)} YouTube summary(ies) — {datetime.now().strftime('%b %d')}",
        items=items,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
