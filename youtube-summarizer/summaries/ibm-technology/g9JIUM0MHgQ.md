# CLI vs MCP: How AI Agents Choose the Right Tool for the Job

Video ID: `g9JIUM0MHgQ`

## Summary
This video compares two methods AI agents use to interact with external systems: CLI (Command Line Interface) and MCP (Model Context Protocol). Through practical demonstrations involving file operations, Git commands, and web page fetching, the presenter illustrates the strengths and weaknesses of each approach. The core argument is that neither tool is universally superior — the right choice depends on the nature of the task, with CLI excelling at direct, well-understood operations and MCP shining when abstraction, authentication, or governance is needed.

## Key insights
- **CLI leverages built-in model knowledge**: AI models are trained on vast amounts of CLI examples (Stack Overflow, man pages, etc.), meaning they already know commands, flags, and syntax without needing any schema loaded into context.
- **MCP has a token cost problem**: Every MCP tool's name, description, and JSON schema is loaded into the context window upfront — the GitHub MCP server alone injects ~55,000 tokens for 80 tools, even if only one or two are ever used.
- **CLI wins for direct, well-mapped operations**: Tasks like file management, Git operations, and text processing are where CLI shines — commands are concise, composable via pipes, and the model needs no extra guidance.
- **MCP wins when raw tools fall short**: The web page demo showed CLI failing badly on a JavaScript-rendered (Next.js) site, requiring multiple workarounds and 2,000+ tokens, while MCP's headless browser tool solved it in one call with ~250 tokens.
- **MCP handles complexity CLI can't easily manage**: Authentication (OAuth, token refresh), per-user access control, shared credential management, and audit trails are built into MCP's protocol — bolting these onto CLI is difficult and manual.
- **Command composability is a CLI advantage**: CLI tools can be chained together in a single line using pipes, whereas MCP tool calls are independent and cannot be natively composed the same way.
- **The best answer is to use both**: Modern AI agents already use CLI and MCP side by side, selecting the appropriate tool based on the task — CLI when commands directly map to the job, MCP when abstraction or governance justifies the overhead.
- **A practical red flag**: If an agent starts reverse-engineering a JavaScript framework just to read a webpage, it's a clear sign it chose the wrong tool for the job.