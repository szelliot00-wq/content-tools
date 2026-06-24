# 5 AI Agent Terms You Need to Know

Video ID: `k5jYwyhDMxA`

## Summary
This video breaks down five foundational concepts that transform a basic LLM into a capable AI agent. It covers the instruction layer, external tool connectivity, inter-agent communication, and multi-agent parallelism. The presenter positions these as the core building blocks behind modern frontier AI agents, tracing each term's origin and governance.

## Key insights
- **agents.md / CLAUDE.md** — A markdown file at the project root that agents read on startup; it encodes project-specific rules like test commands, coding conventions, and PR formatting. Claude uses `CLAUDE.md` instead of `agents.md`, but the concept is identical. Files can be nested, with closer ones taking precedence.
- **Agent Skills** — A folder containing a `skill.md` file (with metadata and a trigger description) plus any needed scripts. Skills are only loaded when the user's request matches the description, keeping the context window clean when they're irrelevant.
- **MCP (Model Context Protocol)** — An open protocol originating at Anthropic, now under the Linux Foundation, that gives agents a standardized way to talk to external tools, APIs, and data sources. An MCP server wraps any backend (e.g., Notion, Stripe) so any MCP-compatible agent can reach it without custom connectors.
- **A2A (Agent-to-Agent)** — A Google-originated open protocol, also now under the Linux Foundation, for agents communicating with each other. Each agent publishes an "agent card" describing its capabilities, which other agents read to delegate work — enabling handoffs like procurement → finance approval without custom integrations.
- **Subagents** — A common (though not formally standardized) pattern where a parent agent spawns child agents, each with its own fresh context window, to handle work that exceeds one context window or can be parallelized. A child completes its task and returns a result, keeping the parent's context clean.
- **Governance trend** — MCP and A2A both started at individual companies (Anthropic and Google respectively) and were contributed to the Linux Foundation as open standards, signaling industry-wide convergence around these primitives.