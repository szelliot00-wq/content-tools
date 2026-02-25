#!/bin/bash
set -e

# Navigate to project root (works on any machine regardless of clone location)
cd "$(dirname "$0")/.."

# Pull latest changes
git pull origin main

# Activate virtual environment
source .venv/bin/activate

# Run the competitor tracker
python competitor-tracker/scrape.py

# Commit and push if snapshots or summaries changed
git add competitor-tracker/snapshots/ summaries/competitors/
if git diff --staged --quiet; then
  echo "No competitor changes to commit."
else
  git commit -m "Auto: competitor snapshot update $(date +%Y-%m-%d)

Co-Authored-By: Warp <agent@warp.dev>"
  git pull --rebase origin main
  git push origin main
fi
