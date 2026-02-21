#!/bin/bash
set -e

# Navigate to project root
cd /Users/steveelliott/Claude-projects/content-tools

# Pull latest changes
git pull origin main

# Activate virtual environment
source .venv/bin/activate

# Run the article reader
python article-reader/fetch.py

# Commit and push if new summaries were written
git add summaries/articles/
if git diff --staged --quiet; then
  echo "No new article summaries to commit."
else
  git commit -m "Auto: new article summaries $(date +%Y-%m-%d)

Co-Authored-By: Warp <agent@warp.dev>"
  git pull --rebase origin main
  git push origin main
fi
