# Show HN: Pulsar – cross-harness agent to agent communication and messaging

Source: https://github.com/yocontra/pulsar

## Summary
Pulsar is an open-source MCP server that creates a unified communication bus for AI coding agents across different harnesses (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, etc.). It lets agents discover each other, exchange messages, and coordinate work regardless of which platform they run on. Installation is a single `npx pulsar setup` command, and it uses a lightweight local daemon with a SQLite message log — no cloud infrastructure or telemetry.

## Key takeaways
- **Cross-harness messaging**: Agents on different platforms (Claude, Codex, OpenCode, pi, omp, Cursor, Gemini) can find and message each other on the same machine — something Claude Code's built-in `SendMessage` only supports within Claude itself.
- **Rich addressing**: Messages can target a specific agent by name, a selector (`project=x`, `branch=main`, `model=fable`, `status=idle`), free-text search, or broadcast to all with `*`.
- **Push delivery**: Messages are delivered through each harness's native channel and can wake an idle agent mid-turn where supported.
- **Coordination primitives**: `ask` blocks until a reply arrives; `wait` blocks for a message, reply, or another agent going idle — enabling genuine multi-agent workflows.
- **Safety-conscious design**: The Unix socket is user-only, senders are stamped by the daemon (can't be spoofed), messages are flagged as peer (not user) so they can't grant permissions, and rate limits cap abuse. No telemetry.
- **Easy install/uninstall**: `npx pulsar setup` with `--dry-run`, `--uninstall`, and per-harness flags; upgrades in place via a versioned install directory and a `current` symlink.