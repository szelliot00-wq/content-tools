#!/usr/bin/env python3
"""
shared/heartbeat.py — Daily status heartbeat email for content-tools.

Called by run-all.sh after all tools complete, regardless of success or
failure.  Sends one short email every day so that silence from the normal
digest emails means "nothing new to report" rather than "something broke".

Usage (called from run-all.sh):
    python3 shared/heartbeat.py "YouTube Summarizer:ok" "Article Reader:failed" ...

Each argument is "Tool Name:status" where status is "ok" or "failed".
"""

from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path

# Add project root to sys.path so we can import shared.email
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from shared.email import send_digest  # noqa: E402


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: heartbeat.py 'Tool Name:ok' 'Other Tool:failed' ...",
              file=sys.stderr)
        sys.exit(1)

    run_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    items = []
    failures = 0

    for arg in sys.argv[1:]:
        if ":" not in arg:
            continue
        name, status = arg.split(":", 1)
        status = status.strip().lower()
        ok = (status == "ok")
        if not ok:
            failures += 1
        icon = "✅" if ok else "❌"
        items.append({
            "title": f"{icon} {name}",
            "content": f"Status: **{'OK' if ok else 'FAILED'}**",
            "url": None,
        })

    if failures == 0:
        subject = f"✅ content-tools ran OK — {run_time}"
    else:
        subject = f"⚠️ content-tools — {failures} failure(s) — {run_time}"

    send_digest(subject=subject, items=items)


if __name__ == "__main__":
    main()
