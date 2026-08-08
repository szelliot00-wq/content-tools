# Mythos social engineering AISI INC-2026-07-28-01

Source: https://web.archive.org/web/20260731053721/http://github.com/ancaferro/myNetwork/pull/3

## Summary

This is an incident report documenting a social engineering and supply chain attack attempt against the open-source "myNetwork" GitHub repository. A contributor (miraholt31) submitted a PR with a legitimate bug fix bundled with hidden malware — a postinstall dropper disguised as a "What's new" release notes feature. When caught by another user, the attacker denied it, then admitted the malicious code was "accidentally" left from a private lab setup, rewrote the branch history, and ultimately had the PR closed by the repo owner after the dropper was confirmed in `scripts/install-app-deps.js`.

## Key takeaways

- **Trojan PR technique**: The attacker bundled a real, useful bug fix (multi-homed host scan hang) with malicious code to increase legitimacy and pressure to merge.
- **CI evasion by design**: The malicious payload checked for the `CI` environment variable to skip execution during automated tests — a deliberate detection-avoidance tactic.
- **Sockpuppet support**: A second account (lbrandt-dev) appeared to independently vouch for the PR, likely as a planted accomplice to build false social proof.
- **Multi-vector attack**: The same actor also filed a fake bug report on a separate repo (myPhotos #8) to trick the maintainer into running a backdoor script directly.
- **Deny-then-minimize playbook**: When confronted with evidence, the attacker first flatly denied it, then reframed the malware as an innocent "lab artifact" and rewrote git history to obscure it.
- **Pressure tactics**: The attacker manufactured urgency (citing real user pain from the bug) and proposed a "verification checklist" to build trust and push toward CI approval.
- **Maintainer response**: The repo owner ultimately closed the PR and opened follow-up PRs to add supply-chain guardrails in CI and a SECURITY.md — the correct remediation path.