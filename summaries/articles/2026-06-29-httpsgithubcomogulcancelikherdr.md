# Herdr: Agent multiplexer that lives in your terminal

Source: https://github.com/ogulcancelik/herdr

## Summary
Herdr is an open-source terminal multiplexer built specifically for AI agent workflows, written in Rust. It combines tmux-style persistent sessions, panes, and tabs with native agent-awareness — a sidebar that shows each agent's state (blocked, working, done) at a glance. Unlike GUI-based agent managers, it runs entirely inside your existing terminal as a single binary with no dependencies, and exposes a Unix socket API so agents can orchestrate it programmatically.

## Key takeaways
- **Agent-aware sidebar**: Herdr tracks agent states (blocked/working/done/idle) by reading process names and terminal output, with no configuration required.
- **Persistent sessions with detach/reattach**: Like tmux, the server keeps running when you detach; agents continue working and you can reconnect later, including over SSH.
- **Terminal-native, no GUI**: Single Rust binary, no Electron, no web dashboard — runs inside any terminal you already use, including as a nested client inside tmux.
- **Broad agent support**: Out-of-the-box detection for Claude Code, Codex, GitHub Copilot CLI, Cursor, Devin, Amp, OpenCode, Grok CLI, and more (15+ agents listed).
- **Agents can use Herdr too**: A local Unix socket API lets agents create workspaces, split panes, spawn helpers, and read output — enabling agent-driven orchestration.
- **tmux-like keybindings**: `ctrl+b` prefix model with familiar bindings for tabs, panes, splits, and workspaces; mouse support throughout.
- **Multiple install paths**: curl installer, Homebrew (`brew install herdr`), mise, Nix flake, or direct binary download; stable and preview channels available.
- **Dual-licensed**: AGPL-3.0 for open source use; commercial licenses available for organizations that can't comply with AGPL.