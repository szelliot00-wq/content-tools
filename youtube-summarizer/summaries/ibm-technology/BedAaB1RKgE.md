# MCP vs ADK: How Modern AI Agents Connect and Work Together

Video ID: `BedAaB1RKgE`

## Summary
This video explains the difference between MCP (Model Context Protocol) and ADK (Agent Development Kit), two tools that address distinct problems in AI agent development. MCP, created by Anthropic, standardizes how agents connect to external tools and data sources. ADK, from Google, is a Python framework for building, structuring, and orchestrating agents. The two are complementary rather than competing technologies.

## Key insights
- **MCP solves connectivity**: It defines a standard protocol (using JSON-RPC) for how AI agents communicate with external tools, APIs, databases, and files — replacing one-off custom integrations with a reusable, model-agnostic interface.
- **ADK solves orchestration**: It provides the full framework for building agent logic — defining behavior, memory, tool use, reasoning loops, and multi-agent coordination.
- **MCP has three core primitives**: Tools (callable functions like web search or SQL queries), Resources (readable data like files or docs), and Prompts (reusable prompt templates).
- **ADK has multiple agent types**: LLM-driven agents for flexible reasoning, and deterministic workflow agents (sequential, parallel, loop-based) for predictable, hard-coded execution paths.
- **ADK's runner/yield model improves debuggability**: Agents yield control back to the runner at each step, making behavior traceable and testable compared to ad hoc agent code.
- **ADK supports multi-agent architectures**: A root orchestrator can delegate to specialized sub-agents (e.g., research agent, writing agent, validation agent), each with a defined role.
- **They work together**: ADK is tool-framework agnostic at the integration layer, meaning MCP servers can be plugged directly into ADK agents as tool sources.
- **MCP is model-agnostic**: Any LLM that speaks MCP (Claude, GPT, Gemini, local models) can use the same MCP servers — write once, reuse everywhere.
- **The right question isn't "which one?"** — it's "what problem am I solving?" Use MCP for standardized external connectivity, ADK for building the agent's internal structure and logic.