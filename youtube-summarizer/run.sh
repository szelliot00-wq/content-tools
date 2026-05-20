#!/bin/bash
# Manual invocation wrapper. All git operations are handled by run-all.sh.
REPO="$(cd "$(dirname "$0")/.." && pwd)"
source "$REPO/.venv/bin/activate"
exec python "$REPO/youtube-summarizer/summarize.py" "$@"
