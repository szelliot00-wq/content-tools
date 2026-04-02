#!/bin/bash
set -e

# Navigate to project root (content-tools) regardless of where this is called from
cd "$(dirname "$0")/.."

# Pull latest changes (picks up edits to creators.json made on another machine)
git pull --rebase origin main

# Activate the shared content-tools venv
source .venv/bin/activate

# Run the summarizer — skips videos that already have a summary
python youtube-summarizer/summarize.py

# Commit new summaries and transcripts if any were written
git add youtube-summarizer/summaries/ youtube-summarizer/transcripts/
if git diff --staged --quiet; then
    echo "No new YouTube summaries to commit."

    # Alert if no summaries have been committed for 2+ days.
    # Uses git log rather than file mtime — git pull --rebase updates mtimes
    # on all files, making mtime checks unreliable.
    LAST_COMMIT_TS=$(git log --format="%ct" -- "youtube-summarizer/summaries/" | head -1)
    if [ -z "$LAST_COMMIT_TS" ]; then
        echo "No summary commits found — skipping staleness check."
    else
        NOW=$(date +%s)
        AGE_DAYS=$(( (NOW - LAST_COMMIT_TS) / 86400 ))
        LAST_COMMIT_DATE=$(date -r "$LAST_COMMIT_TS" +%Y-%m-%d)
        echo "Most recent summary commit: $LAST_COMMIT_DATE (${AGE_DAYS} day(s) ago)"
        if [ "$AGE_DAYS" -ge 2 ]; then
            echo "WARNING: No new YouTube summaries for ${AGE_DAYS} days — sending alert"
            python3 -m shared.heartbeat "YouTube Summarizer (silent — no new summaries for ${AGE_DAYS} days)"
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
