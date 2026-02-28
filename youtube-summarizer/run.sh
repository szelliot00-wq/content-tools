#!/bin/bash
set -e

# Navigate to project root (content-tools) regardless of where this is called from
cd "$(dirname "$0")/.."

# Pull latest changes (picks up edits to creators.json made on another machine)
git pull origin main

# Activate the shared content-tools venv
source .venv/bin/activate

# Run the summarizer — skips videos that already have a summary
python youtube-summarizer/summarize.py

# Commit new summaries and transcripts if any were written
git add youtube-summarizer/summaries/ youtube-summarizer/transcripts/
if git diff --staged --quiet; then
    echo "No new YouTube summaries to commit."

    # Alert if no summaries have been written for 2+ days
    LATEST=$(find youtube-summarizer/summaries -name '*.md' -not -path '*/.*' | xargs ls -t 2>/dev/null | head -1)
    if [ -z "$LATEST" ]; then
        echo "No summaries found at all — skipping staleness check."
    else
        MTIME=$(stat -f %m "$LATEST")   # macOS stat
        NOW=$(date +%s)
        AGE_DAYS=$(( (NOW - MTIME) / 86400 ))
        echo "Most recent summary: $LATEST (${AGE_DAYS} day(s) old)"
        if [ "$AGE_DAYS" -ge 2 ]; then
            echo "WARNING: No new YouTube summaries for ${AGE_DAYS} days — sending alert"
            python3 shared/heartbeat.py "YouTube Summarizer (silent — no new summaries for ${AGE_DAYS} days)"
        fi
    fi
else
    git commit -m "Auto: new YouTube summaries $(date +%Y-%m-%d)

Co-Authored-By: Warp <agent@warp.dev>"
    git pull --rebase origin main
    git push origin main

    # Email digest of newly committed summaries
    python youtube-summarizer/send_digest.py
fi
