#!/usr/bin/env python3
"""
Reusable Claude CLI wrapper for content-tools.
"""
from __future__ import annotations

import os
import subprocess
import sys
import time

MAX_CHARS = 120_000
CLAUDE_BIN = "/usr/local/bin/claude"


def summarize(content: str, prompt_template: str) -> str | None:
    """Summarize content using the Claude CLI. Returns None on error."""
    if len(content) > MAX_CHARS:
        content = content[:MAX_CHARS] + "\n\n[Content truncated...]"

    prompt = prompt_template.format(content=content)

    env = os.environ.copy()
    env["CLAUDECODE"] = ""  # required for non-interactive claude CLI use

    for attempt in range(2):
        try:
            result = subprocess.run(
                [CLAUDE_BIN, "--print", prompt],
                capture_output=True,
                text=True,
                timeout=120,
                env=env,
            )
            if result.returncode == 0:
                return result.stdout.strip()
            print(f"Claude CLI error (exit {result.returncode}): {result.stderr}", file=sys.stderr)
        except subprocess.TimeoutExpired:
            print("Claude CLI timed out after 120s", file=sys.stderr)
        except Exception as e:
            print(f"Claude CLI error: {e}", file=sys.stderr)

        if attempt == 0:
            print("Retrying in 30s...", file=sys.stderr)
            time.sleep(30)

    return None
