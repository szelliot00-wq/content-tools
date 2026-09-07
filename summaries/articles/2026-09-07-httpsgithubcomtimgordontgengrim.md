# Show HN: Engrim – A universal, local-first SQLite memory engine for AI CLIs

Source: https://github.com/timgordontg/engrim

## Summary
Engrim is an open-source, local-first SQLite memory engine designed to give AI coding assistants (Claude Code, Cursor, Windsurf, Google Antigravity) persistent, cross-session memory without cloud lock-in. It stores project decisions, constraints, and state in a local SQLite database and surfaces a curated ~4,000-character memory pack at session start, allowing developers to switch between AI models mid-project without losing context. It was validated across 105 sessions on a 50,000-line algorithmic trading codebase, compressing 153,000 tokens of work history into under 1,000 tokens per reload.

## Key takeaways
- **Universal cross-model memory**: A single SQLite store works across Google Antigravity, Claude Code, Cursor, and Windsurf — switch AI tools mid-project and pick up where you left off.
- **Massive context cost reduction**: Claims 99%+ reduction in reloaded context tokens per session restart by loading only a curated memory pack instead of full conversation history.
- **Hybrid search**: Combines SQLite FTS5 keyword search with static vector embeddings (`model2vec`) via reciprocal-rank fusion for fast, relevant memory retrieval.
- **Agent provenance tracking**: Every memory record stores which agent wrote it (`antigravity`, `claude-code`, `cursor`, etc.), so multi-agent collaboration stays auditable.
- **One-command setup**: `engrim setup` auto-detects installed environments and wires hooks, MCP config, and status lines for all of them simultaneously.
- **Fully local and private**: No cloud calls — all data stays in a local SQLite file with owner-only permissions; MIT licensed.
- **MCP server included**: Exposes `engrim_recall`, `engrim_add`, `engrim_context`, and `engrim_review` as MCP tools for deep IDE/agent integration.