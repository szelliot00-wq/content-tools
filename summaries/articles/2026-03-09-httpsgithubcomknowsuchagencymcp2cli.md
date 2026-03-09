# Show HN: Mcp2cli – One CLI for every API, 96-99% fewer tokens than native MCP

Source: https://github.com/knowsuchagency/mcp2cli

## Summary
Mcp2cli is a new tool that addresses the high token consumption of native MCP (Machine-to-Cloud Protocol) servers by converting them or any OpenAPI specification into a command-line interface (CLI) at runtime. This allows Large Language Models (LLMs) to discover and use tools on demand, rather than having full tool schemas injected into context on every turn. The approach drastically reduces token usage, achieving savings of 96-99%, while offering dynamic updates without codegen and compatibility with any LLM.

## Key takeaways
- **Problem Solved:** Native MCP servers inject full tool schemas into an LLM's context on every turn, leading to massive token waste (e.g., 362,000 tokens for schemas over 25 turns with 120 tools).
- **Solution Offered:** Mcp2cli transforms MCP servers or OpenAPI specs (JSON/YAML) into a runtime CLI, enabling LLMs to discover and fetch tool details only when needed.
- **Significant Token Savings:** The tool achieves substantial token reductions, measured at 96% for 30 tools over 15 turns and 99% for 120 tools over 25 turns, freeing up context window space and reducing costs.
- **Dynamic & Flexible:** It requires no codegen or rebuilds when server APIs change, works with any LLM (as it's just a CLI), and supports both MCP and OpenAPI specifications interchangeably.
- **Ease of Integration:** Mcp2cli can also be installed as a skill for popular AI coding agents like Claude Code, Cursor, and Codex.