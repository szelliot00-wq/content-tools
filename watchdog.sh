#!/bin/bash
# watchdog.sh — checks whether run-all.sh ran today; sends alert if not.
#
# Run by a separate launchd job at 09:15 — 75 minutes after the main 08:00 job.
# If cron.log was not modified today, it means launchd never fired run-all.sh.

REPO="$HOME/Claude-projects/content-tools"
LOG="$REPO/cron.log"
VENV="$REPO/.venv"

TODAY=$(date +%Y-%m-%d)

if [ ! -f "$LOG" ]; then
    LAST_MOD="never"
else
    LAST_MOD=$(date -r "$LOG" +%Y-%m-%d)
fi

echo "=== Watchdog check at $(date) ==="
echo "cron.log last modified: $LAST_MOD (today: $TODAY)"

if [ "$LAST_MOD" = "$TODAY" ]; then
    echo "Main job ran today — OK"
    exit 0
fi

echo "WARNING: main job did not run today — sending alert"
"$VENV/bin/python3" "$REPO/shared/heartbeat.py" \
    "Scheduler (launchd did not run — cron.log last modified: $LAST_MOD)"
