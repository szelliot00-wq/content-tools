# Lore – give your coding agent the decisions your team made

Source: https://github.com/itsthelore/rac-core

## Summary
Lore (built on the open-source RAC — Requirements as Code engine) is a tool that stores a team's decisions, requirements, designs, and roadmaps as typed Markdown in a Git repo and serves them read-only to AI coding agents (Claude Code, Cursor, Claude Desktop) via MCP. Unlike RAG/embeddings, retrieval is fully deterministic — the agent gets the exact, current decision rather than a similarity-ranked guess. It also enforces knowledge quality in CI, rejecting malformed artifacts or references to superseded decisions before they land.

## Key takeaways
- **Deterministic, not fuzzy**: Lore uses no embeddings or LLM calls for retrieval — it returns the precise, current artifact every time, making results reproducible across runs.
- **Read-only by design**: The MCP server can only read; agents cannot mutate the knowledge store. The trust boundary is human PR review.
- **CI enforcement**: `rac validate` and `rac gate` reject malformed artifacts, broken links, and references to superseded decisions before merging — keeping the corpus clean.
- **Composes with RAG**: Export commands (`--documents`, `--graph`) feed external RAG/memory tools so agents can recall fuzzily there, then verify the exact decision in Lore.
- **Plain Markdown storage**: Every artifact is standard Markdown with a small frontmatter envelope — no proprietary format, and it exports to Google's Open Knowledge Format (OKF).
- **Import path from existing docs**: A `rac-import` agent skill converts existing Confluence/Notion/Markdown docs into valid Lore artifacts with a human-review step before writing anything.
- **Zero egress by default**: The engine makes no LLM or network calls; an optional usage ping is off by default and can be provably disabled for regulated environments.