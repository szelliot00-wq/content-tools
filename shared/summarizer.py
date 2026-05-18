#!/usr/bin/env python3
"""
Reusable Claude CLI wrapper for content-tools.
Uses the authenticated Claude CLI session — no API key required.
"""
from __future__ import annotations

import os
import signal
import subprocess
import sys
import time

MAX_CHARS = 120_000
MODEL = "claude-sonnet-4-6"


def _find_claude() -> str:
    for candidate in ["/opt/homebrew/bin/claude", "/usr/local/bin/claude"]:
        if os.path.exists(candidate):
            return candidate
    return "claude"


def summarize(content: str, prompt_template: str) -> str | None:
    """Summarize content using the Claude CLI. Returns None on error."""
    if len(content) > MAX_CHARS:
        content = content[:MAX_CHARS] + "\n\n[Content truncated...]"

    prompt = prompt_template.format(content=content)
    claude_bin = _find_claude()

    for attempt in range(2):
        proc = subprocess.Popen(
            [claude_bin, "--print", "--model", MODEL, "--dangerously-skip-permissions"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env={**os.environ, "CLAUDECODE": ""},
            start_new_session=True,
        )
        try:
            stdout, stderr = proc.communicate(input=prompt, timeout=120)
        except subprocess.TimeoutExpired:
            try:
                os.killpg(proc.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            for fd in (proc.stdout, proc.stderr, proc.stdin):
                try:
                    if fd:
                        fd.close()
                except OSError:
                    pass
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                pass
            print("Claude CLI timed out after 120s", file=sys.stderr)
            if attempt == 0:
                print("Retrying in 30s...", file=sys.stderr)
                time.sleep(30)
            continue
        if proc.returncode == 0:
            return stdout.strip()
        detail = (stderr or stdout).strip()[:300]
        print(f"Claude CLI error (rc={proc.returncode}): {detail}", file=sys.stderr)
        if attempt == 0:
            print("Retrying in 30s...", file=sys.stderr)
            time.sleep(30)

    return None
