#!/bin/bash
# Master runner — calls all three content tools in sequence.
# A failure in one tool is caught and reported but does not stop the others.

ERRORS=0

run_tool() {
    local name="$1"
    local script="$2"
    echo ""
    echo "=== $name ==="
    if bash "$script"; then
        echo "=== $name: done ==="
    else
        echo "=== $name: FAILED ==="
        ERRORS=$((ERRORS + 1))
    fi
}

run_tool "YouTube Summarizer" "$HOME/Claude-projects/youtube-summarizer/run-summarizer.sh"
run_tool "Article Reader" "$HOME/Claude-projects/content-tools/article-reader/run.sh"
run_tool "Competitor Tracker" "$HOME/Claude-projects/content-tools/competitor-tracker/run.sh"

echo ""
if [ $ERRORS -gt 0 ]; then
    echo "=== $ERRORS tool(s) failed — check log above ==="
    exit 1
fi

echo "=== All tools completed successfully ==="
