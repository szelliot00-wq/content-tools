#!/bin/bash
# Master runner — calls all three content tools in sequence.
# Owns all git operations; Python scripts are pure data-processors.
#
# On failure: waits 30s, pulls latest, retries once.
# Sends alert email only if a tool fails after retry.
# No email on success — silence means everything ran fine.

LOCKFILE=/tmp/content-tools-run.pid
if [ -f "$LOCKFILE" ]; then
    OLD_PID=$(cat "$LOCKFILE" 2>/dev/null)
    if [ -n "$OLD_PID" ] && kill -0 "$OLD_PID" 2>/dev/null; then
        echo "=== Another instance (PID $OLD_PID) already running — exiting ==="
        exit 0
    fi
fi
echo $$ > "$LOCKFILE"
trap 'rm -f "$LOCKFILE"' EXIT

ERRORS=0
FAILED_TOOLS=()

REPO="$HOME/Claude-projects/content-tools"
VENV="$REPO/.venv"
PYTHON="$VENV/bin/python"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

find_agent_browser() {
    for candidate in /opt/homebrew/bin/agent-browser /usr/local/bin/agent-browser; do
        [ -f "$candidate" ] && { echo "$candidate"; return; }
    done
    local nvm_base="$HOME/.nvm/versions/node"
    if [ -d "$nvm_base" ]; then
        # Pick the newest node version
        local ab
        ab=$(ls -1 "$nvm_base" 2>/dev/null | sort -rV | while read -r v; do
            local bin="$nvm_base/$v/bin/agent-browser"
            [ -f "$bin" ] && echo "$bin" && break
        done)
        [ -n "$ab" ] && { echo "$ab"; return; }
    fi
    command -v agent-browser 2>/dev/null || echo "agent-browser"
}

AGENT_BROWSER=$(find_agent_browser)

close_browsers() {
    "$AGENT_BROWSER" close --all 2>/dev/null || true
}

# timeout wrapper — handles macOS (no built-in timeout) and Linux
run_with_timeout() {
    local secs="$1"; shift
    if command -v timeout >/dev/null 2>&1; then
        timeout "$secs" "$@"
    elif command -v gtimeout >/dev/null 2>&1; then
        gtimeout "$secs" "$@"
    else
        echo "  Warning: timeout command not available — running without timeout" >&2
        "$@"
    fi
}

git_commit_push() {
    local label="$1"; shift
    git -C "$REPO" add "$@"
    if git -C "$REPO" diff --staged --quiet; then
        echo "  No new output to commit for $label."
        return 0
    fi
    git -C "$REPO" commit -m "Auto: $label $(date +%Y-%m-%d)"
    git -C "$REPO" pull --rebase
    git -C "$REPO" push
}

check_staleness() {
    local name="$1"
    local git_path="$2"
    local max_age_days="${3:-2}"
    local last_ts
    last_ts=$(git -C "$REPO" log --format="%ct" -- "$git_path" | head -1)
    [ -z "$last_ts" ] && return
    local now age_days last_date
    now=$(date +%s)
    age_days=$(( (now - last_ts) / 86400 ))
    last_date=$(date -r "$last_ts" +%Y-%m-%d 2>/dev/null || date -d "@$last_ts" +%Y-%m-%d 2>/dev/null)
    echo "  Most recent $name commit: $last_date (${age_days} day(s) ago)"
    if [ "$age_days" -ge "$max_age_days" ]; then
        echo "  WARNING: $name stale — sending alert"
        "$PYTHON" -m shared.heartbeat "$name (no new content for ${age_days} days)" || true
    fi
}

run_tool() {
    local name="$1"
    local script="$2"   # python script relative to REPO

    echo ""
    echo "=== $name ==="
    close_browsers

    if run_with_timeout 540 "$PYTHON" "$REPO/$script"; then
        echo "=== $name: done ==="
        return 0
    fi

    local rc=$?
    if [ $rc -eq 124 ]; then
        echo "=== $name: TIMED OUT after 9 minutes ==="
    else
        echo "=== $name: failed (rc=$rc) — waiting 30s then retrying ==="
        sleep 30
        git -C "$REPO" pull --rebase || true
        close_browsers
        if run_with_timeout 540 "$PYTHON" "$REPO/$script"; then
            echo "=== $name: retry succeeded ==="
            return 0
        fi
        echo "=== $name: FAILED after retry ==="
    fi

    ERRORS=$((ERRORS + 1))
    FAILED_TOOLS+=("$name")
    return 1
}

# ---------------------------------------------------------------------------
# Pre-flight
# ---------------------------------------------------------------------------

echo "=== Run started at $(date) ==="

# Stash uncommitted changes so pull --rebase is clean
STASHED=0
if ! git -C "$REPO" diff --quiet || ! git -C "$REPO" diff --cached --quiet; then
    echo "=== Stashing uncommitted changes before pull ==="
    git -C "$REPO" stash push -m "run-all pre-flight $(date +%Y-%m-%d)"
    STASHED=1
fi

# Push any local commits that haven't reached the remote yet
if git -C "$REPO" log --oneline @{u}..HEAD 2>/dev/null | grep -q .; then
    echo "=== Pushing orphaned local commits ==="
    git -C "$REPO" push || true
fi

git -C "$REPO" pull --rebase
"$VENV/bin/pip" install -q -r "$REPO/requirements.txt"

if [ "$STASHED" = "1" ]; then
    git -C "$REPO" stash pop || echo "Warning: stash pop failed — check for conflicts"
fi

# ---------------------------------------------------------------------------
# Run tools
# ---------------------------------------------------------------------------

if run_tool "YouTube Summarizer" "youtube-summarizer/summarize.py"; then
    git_commit_push "YouTube summaries" \
        "youtube-summarizer/summaries/" \
        "youtube-summarizer/transcripts/"
    check_staleness "YouTube summaries" "youtube-summarizer/summaries/" 2
fi

if run_tool "Article Reader" "article-reader/fetch.py"; then
    git_commit_push "Article summaries" \
        "summaries/articles/"
    check_staleness "Article summaries" "summaries/articles/" 3
fi

if run_tool "Competitor Tracker" "competitor-tracker/scrape.py"; then
    git_commit_push "Competitor snapshots" \
        "competitor-tracker/snapshots/" \
        "summaries/competitors/"
fi

# Final browser cleanup
close_browsers

# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

echo ""
if [ $ERRORS -gt 0 ]; then
    echo "=== $ERRORS tool(s) failed after retry — sending alert ==="
    "$PYTHON" \
        "$REPO/shared/heartbeat.py" \
        "${FAILED_TOOLS[@]}"
    exit 1
fi

echo "=== All tools completed successfully ==="
