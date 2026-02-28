#!/usr/bin/env python3
"""
shared/heartbeat.py — Failure alert email for content-tools.

Called by run-all.sh only when one or more tools fail after the automatic
retry.  Each argument is the name of a failed tool.  Silence means all
tools ran successfully.

Usage (called from run-all.sh):
    python3 shared/heartbeat.py "YouTube Summarizer" "Article Reader"
"""

from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from shared.email import send_digest  # noqa: E402


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: heartbeat.py 'Tool Name' ...", file=sys.stderr)
        sys.exit(1)

    failed_tools = sys.argv[1:]
    run_time = datetime.now().strftime("%Y-%m-%d %H:%M")

    items = [
        {
            "title": f"❌ {name}",
            "content": (
                "This tool failed and could not be recovered by the automatic retry.\n\n"
                "Check the log on the MacBook Pro:\n\n"
                "`tail -100 ~/Claude-projects/content-tools/cron.log`"
            ),
            "url": None,
        }
        for name in failed_tools
    ]

    n = len(failed_tools)
    subject = f"⚠️ content-tools: {n} tool(s) failed — {run_time}"

    send_digest(subject=subject, items=items)


if __name__ == "__main__":
    main()
