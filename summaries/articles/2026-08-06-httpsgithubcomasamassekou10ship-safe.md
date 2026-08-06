# Ship Safe, an open source security scanner for coding agents

Source: https://github.com/asamassekou10/ship-safe

## Summary
Ship Safe is an open-source CLI security scanner (MIT licensed, `npx ship-safe`) designed for the agentic AI era. It runs locally to detect vulnerabilities across application code, AI agent configs, MCP servers, prompts, secrets, supply chain, and CI/CD pipelines — with no signup required. It ships 27+ specialized security agents that run in parallel, supports AI-assisted fix workflows, and integrates with GitHub Actions via SARIF output.

## Key takeaways
- **One-command scanning**: `npx ship-safe` requires no signup or API key for core checks; AI-backed modes use your configured provider (Anthropic, OpenAI, DeepSeek, etc.).
- **AI-native threat coverage**: Uniquely targets agentic risks — prompt injection, MCP tool poisoning, agent memory poisoning, hallucinated package imports (slopsquatting), RAG poisoning, and managed-agent misconfigs — areas where tools like Semgrep, Gitleaks, and Trivy have no equivalent rules.
- **27+ parallel security agents**: Covers OWASP LLM Top 10, OWASP Agentic AI Top 10, supply chain attacks, CI/CD pipeline poisoning, secrets in git history, mobile security, and more.
- **Interactive fix loop**: The agent proposes diffs and asks before writing; changes are reversible with `ship-safe undo`. Critical findings cannot be suppressed via inline comments.
- **CI/CD integration**: Outputs SARIF for GitHub code scanning; fails builds on critical/high findings with `npx ship-safe ci .`.
- **Noise calibration matters**: The project benchmarks false positives against real OSS projects (express, flask, chalk, requests) — down from 1031 findings to ~73 after v9.6.3 improvements.
- **Complements, not replaces**: Designed to run alongside CodeQL, Gitleaks, and Trivy, each covering different ground; Ship Safe's unique value is what AI coding agents do to your repo and tooling.
- **Free CLI, paid cloud dashboard**: Core scanner is MIT-licensed; Pro/Team tiers add scan history, PR Guardian, and team collaboration via a hosted dashboard.