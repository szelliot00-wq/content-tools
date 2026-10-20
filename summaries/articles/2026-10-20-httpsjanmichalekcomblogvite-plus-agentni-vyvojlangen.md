# Vite+ an excellent toolchain for AI agent development

Source: https://janmichalek.com/blog/vite-plus-agentni-vyvoj?lang=en

## Summary
The author describes switching to Vite+, a unified toolchain that consolidates Vite, Vitest, Oxlint, Oxfmt, and tsdown under a single CLI (`vp`). After struggling with fragmented configs, inconsistent CI/local behavior, and having to explain tooling to AI agents repeatedly, they adopted Vite+ as a standard starting point for new projects. The result was dramatically faster CI (4 min → 50 sec in one monorepo) and a consistent, agent-friendly workflow.

## Key takeaways
- **AI agents need explicit, consistent tooling instructions** — without them, agents guess wrong, mix incompatible tools (e.g., both Prettier and Oxfmt), and create messy setups that require human cleanup.
- **Vite+ consolidates common tasks under one command** (`vp check`, `vp test`, `vp build`), eliminating the per-project "which script does what" problem.
- **Include Vite+ setup instructions in your first AI prompt** — agents don't retain context between sessions, so the repo itself must encode the correct commands.
- **Significant speed gains are possible but not guaranteed** — the author saw CI drop from ~10s to ~1.3s in benchmarks and pre-commit checks fall from 11s to under 2s, though results depend on configuration.
- **CI parity matters** — running the same checks locally and in CI prevents the divergence where an agent sees a green result locally but the pipeline fails.
- **Banning duplicate tools is a practical necessity, not aesthetics** — explicitly prohibiting a second formatter or multiple lockfiles in agent instructions prevents recurring cleanup work.