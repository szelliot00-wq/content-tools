#!/usr/bin/env python3
"""
Reusable Gemini API wrapper for content-tools.
"""
from __future__ import annotations

import os
import sys

from dotenv import load_dotenv

load_dotenv()

try:
    from google import genai as google_genai
except ImportError:
    google_genai = None

MAX_CHARS = 120_000


def summarize(content: str, prompt_template: str) -> str | None:
    """Summarize content using Gemini. Returns None on error or missing config."""
    if not google_genai:
        print("google-genai not installed. Run: pip install google-genai", file=sys.stderr)
        return None

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("GEMINI_API_KEY not set in environment.", file=sys.stderr)
        return None

    if len(content) > MAX_CHARS:
        content = content[:MAX_CHARS] + "\n\n[Content truncated...]"

    prompt = prompt_template.format(content=content)

    try:
        client = google_genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        return (response.text or "").strip()
    except Exception as e:
        print(f"Gemini error: {e}", file=sys.stderr)
        return None
