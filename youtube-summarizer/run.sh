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
else
    git commit -m "Auto: new YouTube summaries $(date +%Y-%m-%d)

Co-Authored-By: Warp <agent@warp.dev>"
    git pull --rebase origin main
    git push origin main

    # Email digest of newly committed summaries
    python youtube-summarizer/send_digest.py
fi
