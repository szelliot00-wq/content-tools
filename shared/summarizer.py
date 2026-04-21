#!/usr/bin/env python3
"""
Reusable Anthropic Claude API wrapper for content-tools.
"""
from __future__ import annotations

import os
import sys
import time

from dotenv import load_dotenv

load_dotenv()

try:
    import anthropic as anthropic_sdk
except ImportError:
    anthropic_sdk = None

MAX_CHARS = 120_000
MODEL = "claude-sonnet-4-6"


def summarize(content: str, prompt_template: str) -> str | None:
    """Summarize content using Claude. Returns None on error or missing config."""
    if not anthropic_sdk:
        print("anthropic not installed. Run: pip install anthropic", file=sys.stderr)
        return None

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ANTHROPIC_API_KEY not set in environment.", file=sys.stderr)
        return None

    if len(content) > MAX_CHARS:
        content = content[:MAX_CHARS] + "\n\n[Content truncated...]"

    prompt = prompt_template.format(content=content)

    client = anthropic_sdk.Anthropic(api_key=api_key)
    for attempt in range(2):
        try:
            response = client.messages.create(
                model=MODEL,
                max_tokens=4096,
                messages=[{"role": "user", "content": prompt}],
            )
            return (response.content[0].text or "").strip()
        except Exception as e:
            print(f"Claude error: {e}", file=sys.stderr)
            if attempt == 0:
                print("Retrying in 30s...", file=sys.stderr)
                time.sleep(30)
    return None
