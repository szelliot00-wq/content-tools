# Show HN: Mcptoon – Token-efficient MCP CLI client

Source: https://github.com/activeing123/mcptoon

## Summary
mcptoon is a token-efficient CLI client for the Model Context Protocol (MCP) that replaces verbose JSON responses with a compact format called TOON (Token-Optimized Object Notation). It targets the problem that standard MCP tool discovery and calls consume 10,000+ tokens on syntax overhead alone, eating 30–55% of a typical 128K context window. mcptoon is a zero-dependency, 50KB Python package that works with any AI agent that can run shell commands.

## Key takeaways
- **Massive token savings**: Tool discovery drops from ~2,000 tokens (JSON) to ~60 tokens (TOON) — a 97% reduction; structured tool results save 40–60%.
- **TOON format**: A compact notation that replaces JSON braces/quotes with pipes, spaces for arrays, single chars for booleans (`T`/`F`) and null (`∅`), shrinking syntax overhead without losing semantic content.
- **Multiple output modes**: `--toon` (compact with semantics), `--compact` (names only), `--json` (standard), `--raw`, plus truncation controls (`--head N`, `--max-chars N`).
- **Agent-agnostic**: Works with Claude Code, Codex, Cursor, OpenCode, and anything else that runs shell commands — one config file shared across all agents.
- **Built-in safety**: Blocks dangerous operations (deletes, drops, etc.) by default, requiring an explicit `--destructive` flag.
- **Zero dependencies**: Pure Python 3.10+, ~50KB install, cross-platform (Windows/macOS/Linux) — versus competitors at 10–50MB with 5–20 dependencies.
- **Extras**: Local usage tracking, 5-minute schema cache, Python API, and custom handler registration to bypass MCP entirely for specific tools.