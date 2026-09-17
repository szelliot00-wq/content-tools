# Cloudflare/Security-Audit-Skill

Source: https://github.com/cloudflare/security-audit-skill

## Summary
Cloudflare's `security-audit-skill` is an open-source GitHub repository providing a coding-agent skill that transforms an AI agent into a structured security auditor. It runs a six-phase audit process covering reconnaissance, coverage-led hunting, candidate validation, structured output, record verification, and reporting. The skill originated as the seed for Cloudflare's internal vulnerability discovery harness and has since evolved into a multi-stage, fleet-wide system.

## Key takeaways
- The skill orchestrates isolated agents through six distinct phases: reconnaissance, hunting, validation, structured output, independent record verification, and reporting.
- Findings are classified into three verdicts: `confirmed` (full source trace), `needs_validation` (unresolved fact, no severity), and `rejected` (disproved candidate).
- Multiple audit runs against the same repo are additive — prior ledgers and findings are used to target gaps and revalidate changed source without treating stale work as covered.
- The repo includes domain-specific attack class files covering AI/LLM, web/auth, client-side, supply chain, cloud/deployment, memory safety, and more.
- Two zero-dependency validators (`validate-findings.cjs` and `validate-coverage-ledger.cjs`) run automatically at key phases to enforce schema correctness.
- The project is MIT-licensed, publicly available with 8.1k stars and 454 forks, and maintained by Cloudflare's security AI research team.