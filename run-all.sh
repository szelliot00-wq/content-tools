#!/bin/bash
# Master runner — calls all three content tools in sequence.
#
# On failure: waits 30s, pulls latest (resolves git conflicts), retries once.
# Sends a failure alert email only if a tool fails after retry.
# No email on success — silence means everything ran fine.

ERRORS=0
FAILED_TOOLS=()

run_tool() {
    local name="$1"
    local script="$2"
    local repo="$3"   # path to git repo to pull before retry
    echo ""
    echo "=== $name ==="

    if bash "$script"; then
        echo "=== $name: done ==="
        return 0
    fi

    # First attempt failed — wait then retry once.
    # Pull the repo first to resolve any git push conflicts.
    echo "=== $name: failed — waiting 30s then retrying ==="
    sleep 30
    git -C "$repo" pull --rebase origin main 2>/dev/null || true

    if bash "$script"; then
        echo "=== $name: retry succeeded ==="
        return 0
    fi

    echo "=== $name: FAILED after retry ==="
    ERRORS=$((ERRORS + 1))
    FAILED_TOOLS+=("$name")
}

echo "=== Run started at $(date) ==="

run_tool "YouTube Summarizer" \
    "$HOME/Claude-projects/youtube-summarizer/run-summarizer.sh" \
    "$HOME/Claude-projects/youtube-summarizer"

run_tool "Article Reader" \
    "$HOME/Claude-projects/content-tools/article-reader/run.sh" \
    "$HOME/Claude-projects/content-tools"

run_tool "Competitor Tracker" \
    "$HOME/Claude-projects/content-tools/competitor-tracker/run.sh" \
    "$HOME/Claude-projects/content-tools"

echo ""
if [ $ERRORS -gt 0 ]; then
    echo "=== $ERRORS tool(s) failed after retry — sending alert ==="
    "$HOME/Claude-projects/content-tools/.venv/bin/python3" \
        "$HOME/Claude-projects/content-tools/shared/heartbeat.py" \
        "${FAILED_TOOLS[@]}"
    exit 1
fi

echo "=== All tools completed successfully ==="
