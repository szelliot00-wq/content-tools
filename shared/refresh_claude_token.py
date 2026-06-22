#!/usr/bin/env python3
"""
Refresh the Claude CLI OAuth token if it expires within TOKEN_REFRESH_BUFFER_S seconds,
write the new credentials back to claude.keychain-db, and print the access token to stdout.

Called by run-all.sh pre-flight; output is captured and exported as CLAUDE_CODE_OAUTH_TOKEN.
All log/error output goes to stderr so it doesn't pollute the token value.
"""
from __future__ import annotations

import os
import sys

# shared/email.py shadows stdlib email (used by urllib.request) when this script
# is invoked directly from inside the shared/ directory. Remove shared/ from
# sys.path before any other imports so stdlib modules resolve correctly.
_here = os.path.dirname(os.path.abspath(__file__))
if _here in sys.path:
    sys.path.remove(_here)

import json
import subprocess
import time
import urllib.error
import urllib.request

_KEYCHAIN = os.path.expanduser("~/Library/Keychains/claude.keychain-db")
_KEYCHAIN_PASSWORD = "665595sze"
_TOKEN_URL = "https://platform.claude.com/v1/oauth/token"
_CLIENT_ID = "9d1c250a-e61b-44d9-88ed-5944d1962f5e"
_USER_AGENT = "anthropic-sdk-typescript/0.54.0 userOAuthProvider"
_REFRESH_BUFFER_S = 1800  # refresh when fewer than 30 min remain


def _read_creds() -> dict | None:
    subprocess.run(
        ["security", "unlock-keychain", "-p", _KEYCHAIN_PASSWORD, _KEYCHAIN],
        capture_output=True, timeout=5,
    )
    proc = subprocess.run(
        ["security", "find-generic-password", "-s", "Claude Code-credentials",
         "-w", _KEYCHAIN],
        capture_output=True, text=True, timeout=5,
    )
    if proc.returncode != 0 or not proc.stdout.strip():
        return None
    try:
        return json.loads(proc.stdout.strip())
    except Exception:
        return None


def _write_creds(creds: dict) -> bool:
    try:
        r = subprocess.run(
            ["security", "add-generic-password", "-U",
             "-s", "Claude Code-credentials",
             "-a", "Claude Code-credentials",
             "-w", json.dumps(creds),
             _KEYCHAIN],
            capture_output=True, text=True, timeout=5,
        )
        return r.returncode == 0
    except Exception:
        return False


def _refresh(creds: dict) -> dict | None:
    oauth = creds.get("claudeAiOauth", {})
    refresh_token = oauth.get("refreshToken")
    if not refresh_token:
        print("No refresh token found", file=sys.stderr)
        return None

    body = json.dumps({
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": _CLIENT_ID,
    }).encode()
    req = urllib.request.Request(
        _TOKEN_URL,
        data=body,
        headers={"Content-Type": "application/json", "User-Agent": _USER_AGENT},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            tokens = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        print(f"Token refresh HTTP {e.code}: {e.read().decode()[:200]}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Token refresh error: {e}", file=sys.stderr)
        return None

    new_creds = {
        **creds,
        "claudeAiOauth": {
            **oauth,
            "accessToken": tokens["access_token"],
            "refreshToken": tokens.get("refresh_token", refresh_token),
            "expiresAt": int((time.time() + tokens.get("expires_in", 28800)) * 1000),
        },
    }
    if _write_creds(new_creds):
        print("Claude OAuth token refreshed and saved to keychain", file=sys.stderr)
    else:
        print("Token refreshed but keychain write failed — will retry next run", file=sys.stderr)
    return new_creds


def main() -> None:
    if not os.path.exists(_KEYCHAIN):
        sys.exit(1)

    creds = _read_creds()
    if not creds:
        print("Could not read credentials from keychain", file=sys.stderr)
        sys.exit(1)

    oauth = creds.get("claudeAiOauth", {})
    access_token = oauth.get("accessToken", "")
    expires_at_s = oauth.get("expiresAt", 0) / 1000

    if time.time() + _REFRESH_BUFFER_S >= expires_at_s:
        mins_left = max(0, expires_at_s - time.time()) / 60
        print(f"Token expires in {mins_left:.0f} min — refreshing", file=sys.stderr)
        refreshed = _refresh(creds)
        if refreshed:
            access_token = refreshed["claudeAiOauth"]["accessToken"]
        elif time.time() >= expires_at_s:
            # Token is fully expired and refresh failed — stale token is useless.
            print("Token expired and refresh failed — manual re-auth required", file=sys.stderr)
            sys.exit(1)

    if access_token:
        print(access_token, end="")
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
