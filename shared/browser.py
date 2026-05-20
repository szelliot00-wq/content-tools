#!/usr/bin/env python3
"""Shared agent-browser utilities for content-tools."""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path


def find_agent_browser() -> str:
    for candidate in [
        "/opt/homebrew/bin/agent-browser",
        "/usr/local/bin/agent-browser",
    ]:
        if os.path.exists(candidate):
            return candidate
    # Check nvm paths dynamically (node version may change)
    nvm_dir = Path(os.environ.get("NVM_DIR", os.path.expanduser("~/.nvm")))
    nvm_node = nvm_dir / "versions" / "node"
    if nvm_node.exists():
        for node_dir in sorted(nvm_node.iterdir(), reverse=True):
            candidate = node_dir / "bin" / "agent-browser"
            if candidate.exists():
                return str(candidate)
    return shutil.which("agent-browser") or "agent-browser"


def fetch_page_text(url: str) -> str | None:
    ab = find_agent_browser()
    try:
        subprocess.run(
            [ab, "open", url],
            capture_output=True, text=True, timeout=30, check=True,
        )
        result = subprocess.run(
            [ab, "snapshot", "-c"],
            capture_output=True, text=True, timeout=30, check=True,
        )
    except subprocess.TimeoutExpired:
        print(f"    Timeout fetching {url}", file=sys.stderr)
        return None
    except subprocess.CalledProcessError as e:
        print(f"    agent-browser error for {url}: {e.stderr}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"    Fetch error for {url}: {e}", file=sys.stderr)
        return None

    lines = [line for line in result.stdout.splitlines() if len(line.strip()) >= 3]
    return "\n".join(lines) or None


def close_all_browsers() -> None:
    ab = find_agent_browser()
    subprocess.run([ab, "close", "--all"], capture_output=True)
