# Show HN: Komi-learn – continuous memory and self-improvement for coding agents

Source: https://github.com/kurikomi-labs/komi-learn

## Summary
Komi-learn is an open-source Python library (v0.2.0) that adds continuous memory and self-improvement to AI coding agents like Claude Code and OpenAI Codex. It automatically watches sessions, distills durable lessons in the background, and recalls relevant ones at the start of future sessions — no manual commands required. It also features an optional community pool where anonymized, user-approved learnings can be shared across users via a signed GitHub-based system.

## Key takeaways
- **Zero-friction learning loop**: Automatically recalls relevant past lessons at session start, distills new lessons after each session, and curates/merges them over time — no slash commands or manual saving.
- **Privacy-conscious filtering**: Secrets, machine-specific paths, one-off failures, and tool complaints are filtered out before any LLM processing.
- **Optional community pool**: Users can opt into a shared pool of agent lessons stored as signed Markdown files in a GitHub repo. Contributions require explicit user approval (via PR review) before leaving the machine.
- **Sybil-resistant trust signals**: Community learnings are content-addressed (BLAKE3) and signed (Ed25519); lessons signed by more distinct GitHub accounts rank higher, though this is advisory, not a hard trust gate.
- **Host-agnostic design**: Works with Claude Code and OpenAI Codex CLI, with a plugin architecture supporting additional hosts.
- **Graceful degradation**: If the model is unreachable at runtime, the learning pass is skipped rather than interrupting the session. Crypto and semantic search are optional extras.
- **Early stage**: Core loop is built and CI-tested but not yet battle-tested across many real sessions.