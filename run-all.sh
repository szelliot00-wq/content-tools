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
    echo ""
    echo "=== $name ==="

    if bash "$script"; then
        echo "=== $name: done ==="
        return 0
    fi

    # First attempt failed — wait then retry once.
    # Pull the repo in case a concurrent push caused a conflict.
    echo "=== $name: failed — waiting 30s then retrying ==="
    sleep 30
    git -C "$REPO" pull --rebase origin main 2>/dev/null || true

    if bash "$script"; then
        echo "=== $name: retry succeeded ==="
        return 0
    fi

    echo "=== $name: FAILED after retry ==="
    ERRORS=$((ERRORS + 1))
    FAILED_TOOLS+=("$name")
}

REPO="$HOME/Claude-projects/content-tools"
VENV="$REPO/.venv"

echo "=== Run started at $(date) ==="

# Pull latest code and install any new dependencies before doing anything else.
# This means new modules, tool scripts, and requirements are picked up automatically.
# Note: changes to run-all.sh itself take effect on the *next* run (bash can't
# reload itself mid-execution).
echo "=== Updating repo and dependencies ==="
git -C "$REPO" pull origin main
"$VENV/bin/pip" install -q -r "$REPO/requirements.txt"

run_tool "YouTube Summarizer" "$REPO/youtube-summarizer/run.sh"
run_tool "Article Reader"    "$REPO/article-reader/run.sh"
run_tool "Competitor Tracker" "$REPO/competitor-tracker/run.sh"

echo ""
if [ $ERRORS -gt 0 ]; then
    echo "=== $ERRORS tool(s) failed after retry — sending alert ==="
    "$HOME/Claude-projects/content-tools/.venv/bin/python3" \
        "$HOME/Claude-projects/content-tools/shared/heartbeat.py" \
        "${FAILED_TOOLS[@]}"
    exit 1
fi

echo "=== All tools completed successfully ==="
