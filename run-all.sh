#!/bin/bash
# Master runner — calls all three content tools in sequence.
# A failure in one tool is caught and reported but does not stop the others.
# Sends a heartbeat email at the end so every run is visible, even when
# individual tools have nothing new to report.

ERRORS=0
TOOL_STATUS=""  # set by run_tool, read immediately after each call

run_tool() {
    local name="$1"
    local script="$2"
    echo ""
    echo "=== $name ==="
    if bash "$script"; then
        echo "=== $name: done ==="
        TOOL_STATUS="ok"
    else
        echo "=== $name: FAILED ==="
        TOOL_STATUS="failed"
        ERRORS=$((ERRORS + 1))
    fi
}

echo "=== Run started at $(date) ==="

run_tool "YouTube Summarizer" "$HOME/Claude-projects/youtube-summarizer/run-summarizer.sh"
YT_STATUS="$TOOL_STATUS"

run_tool "Article Reader" "$HOME/Claude-projects/content-tools/article-reader/run.sh"
AR_STATUS="$TOOL_STATUS"

run_tool "Competitor Tracker" "$HOME/Claude-projects/content-tools/competitor-tracker/run.sh"
CT_STATUS="$TOOL_STATUS"

# Send heartbeat — always, regardless of individual tool outcomes.
echo ""
echo "=== Sending heartbeat email ==="
"$HOME/Claude-projects/content-tools/.venv/bin/python3" \
    "$HOME/Claude-projects/content-tools/shared/heartbeat.py" \
    "YouTube Summarizer:$YT_STATUS" \
    "Article Reader:$AR_STATUS" \
    "Competitor Tracker:$CT_STATUS"

echo ""
if [ $ERRORS -gt 0 ]; then
    echo "=== $ERRORS tool(s) failed — check log above ==="
    exit 1
fi

echo "=== All tools completed successfully ==="
