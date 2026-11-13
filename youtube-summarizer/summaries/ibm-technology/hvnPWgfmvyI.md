# Why AI Agents Need RAG + Observability

Video ID: `hvnPWgfmvyI`

## Summary
The video argues that AI agents in production operations need two complementary types of context to be useful: documented system knowledge (provided via RAG) and live operational signals (provided via observability). Using a hybrid banking transaction as a case study, the presenter shows how combining runbooks/architecture docs with real-time metrics, logs, traces, and change data allows an agent to give operators specific, evidence-grounded starting points rather than generic troubleshooting advice. The human operator remains in control — the agent accelerates investigation, not replaces judgment.

## Key insights
- **RAG alone is not enough.** Runbooks and architecture diagrams describe how a system *should* work, not what it is doing *right now*. They can be months out of date.
- **Observability fills the temporal gap.** Metrics, logs, traces, topology, and change events answer questions RAG cannot: what changed, where, and when.
- **More data is not the goal — relevant signals are.** The value comes from surfacing the right signals and the relationships between them, not flooding the agent with noise.
- **The two sources are complementary, not redundant.** RAG grounds the agent in documented knowledge; observability grounds it in current reality. Neither is sufficient alone.
- **Correlation is not causation — and the agent should say so.** A well-designed agent separates confirmed evidence from possibilities, keeping the operator's trust and decisions accountable.
- **The agent's output should be structured around three things:** (1) what signals changed and where, (2) what downstream services or workflows are affected, and (3) what the operator should validate next based on runbooks and current evidence.
- **Hybrid environments amplify the need.** When a single user action spans distributed systems, middleware, and mainframes owned by different teams, manually correlating context across tools is slow — this is exactly where an agent adds the most value.
- **The operator stays in control.** The agent retrieves, summarizes, and prioritizes context; the human validates evidence and decides action. The goal is a faster, more complete picture — not automation of the decision itself.