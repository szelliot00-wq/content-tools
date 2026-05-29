# Zot now supports Claude Opus 4.8

Source: https://www.zot.sh

**Note:** The article title claims "Zot now supports Claude Opus 4.8," but the provided content contains no mention of Claude Opus 4.8 — it appears to be the general zot documentation/homepage. Additionally, "Claude Opus 4.8" is not a real model as of today (May 29, 2026); the latest is Claude Opus 4.6. The title may be fabricated or the actual announcement content was not included.

Here is a summary based on what was actually provided:

## Summary
Zot is a minimal, single-binary terminal coding agent written in Go that connects to a wide range of AI providers (Anthropic, OpenAI, Gemini, DeepSeek, etc.) and can edit files, run shell commands, and answer Telegram messages. It emphasizes simplicity — no runtime, no Docker, no plugin manager — while offering advanced features like background swarm agents, session management, extensions via JSON-RPC, and a tool permission gate. It supports both interactive TUI use and headless/embedded automation modes.

## Key takeaways
- Single static Go binary with no runtime dependencies; installable via a one-line curl command.
- Supports a broad provider catalog (20+ providers) with API key or subscription-based auth.
- Four built-in tools (file read/write/edit, bash) kept intentionally minimal; extensible via subprocess + JSON-RPC extensions in any language.
- Swarm mode allows spawning parallel background sub-agents that share the same working directory.
- Sessions are persisted as JSONL transcripts with support for resume, branch, export, and auto-compaction at 85% context usage.
- Built-in model fallback picker activates on recoverable provider errors (rate limits, outages, expired tokens).
- Skills system loads per-folder markdown instruction files on demand to keep the context window lean.