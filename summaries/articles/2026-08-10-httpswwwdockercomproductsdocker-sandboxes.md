# Docker Sandboxes – Disposable, isolated sandboxes for AI agents

Source: https://www.docker.com/products/docker-sandboxes/

## Summary
Docker Sandboxes is a product that provides disposable, isolated microVM environments for running AI coding agents (Claude Code, Gemini CLI, Copilot CLI, Codex, Kiro, OpenCode) safely and without supervision. Each sandbox gives agents full autonomy to install packages, modify configs, and spin up Docker containers, while keeping the host machine completely protected. It is installable via a single command on macOS or Windows and requires no Docker Desktop.

## Key takeaways
- **MicroVM isolation**: Each agent runs in a dedicated microVM with a hard security boundary from the host, so agents can operate in "YOLO mode" (`--dangerously-skip-permissions`) without risk to the developer's machine.
- **Disposable by design**: Sandboxes are fast to create and tear down in a single command, making them practical for unattended, automated agent workflows.
- **Configurable controls**: Network access, filesystem rules, and credentials are all configurable per sandbox, with org-wide enforcement available via Docker AI Governance.
- **Broad agent compatibility**: Works out of the box with all major coding agents — Claude Code, Gemini CLI, Copilot CLI, Codex, Kiro, and OpenCode.
- **No Docker Desktop required**: The `sbx` CLI is a standalone install (`brew install docker/tap/sbx` on macOS, `winget install Docker.sbx` on Windows).
- **Enterprise extension**: Teams needing centralized policy enforcement (network policies, filesystem controls, MCP governance) can layer on Docker AI Governance on top of the core sandbox product.