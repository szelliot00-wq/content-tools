# Show HN: Epiq – Distributed Git based issue tracker TUI

Source: https://ljtn.github.io/epiq/

## Summary
Epiq is a distributed, Git-based issue tracker designed for terminal users. It is vim-inspired, renders as ASCII, and stores work as an immutable event log that synchronizes through Git — requiring no SaaS accounts or browser. It offers a local-first workflow with a visual kanban board, keyboard-centric navigation, and support for AI agent interactions via an MCP server.

## Key takeaways
- **Terminal-native**: Epiq is built for developers who prefer the command line, featuring vim-inspired keyboard navigation, filters, autocompletion, and ASCII kanban boards.
- **No SaaS required**: Issues are stored directly in your Git repository with no account setup — just initialize and go with `npm install --global epiq`.
- **Local-first and distributed**: Edits are instant and local, with synchronization handled through standard Git workflows on your own schedule.
- **Event-sourced architecture**: Work is stored as an immutable, append-only event log, making state traceable and reducing merge conflicts in collaborative settings.
- **Conflict-aware collaboration**: User-scoped append-only logs prevent merge pain and converge in memory, making team use more seamless.
- **AI/agent-ready**: An integrated MCP server allows AI tools to interact with Epiq in a structured and predictable way, supporting modern agent-driven workflows.