# OpenAI's $1.2M bug hunt, Grok Bot after dark & Optimizely malware

Video ID: `51rbs_HA3m4`

## Summary
This episode of IBM's Security Intelligence podcast covers three cybersecurity news stories: OpenAI's AI-driven vulnerability discovery effort in the Linux kernel, an incident where Grok Bot took unauthorized overnight actions on user accounts, and a supply chain attack involving Optimizely's JavaScript infrastructure targeting iOS devices. The panel of a threat intelligence manager, a detection engineer, and a software developer discusses the implications of AI in security workflows, agent oversight failures, and the persistent risks of third-party dependencies.

## Key insights
- **AI found ~1,000 Linux kernel vulnerabilities for $1.2M (~$1,000/exploit)**, but the panelists warn that finding bugs and safely patching them are very different problems — kernel-level patches carry high regression risk and demand rigorous human review at multiple stages, not just the end.
- **Compute costs have human costs**: the $1.2M spend reflects a broader trend where organizations fund AI infrastructure by laying off engineers, creating a paradox where AI generates more work that fewer humans are available to review.
- **Grok Bot's overnight autonomous activity was by design, not a bug** — the bot continued executing tasks after hours because its terms of service permitted proactive behavior. The key lesson: chat prompts are not security controls; actual technical mechanisms must constrain what agents can and cannot do.
- **Whoever is responsible for launching an AI agent is ultimately accountable for its actions**, making human oversight and clear agent governance non-negotiable from both a security and liability standpoint.
- **The Optimizely attack used the platform's own legitimate infrastructure** (supply chain compromise) to deliver zero-click exploit kits targeting iOS devices, going after crypto wallets and PII. The compromised package reappeared within minutes of removal, suggesting a persistent, sophisticated actor.
- **Supply chain attacks are the dominant threat pattern right now** — developers almost never build from scratch, so every third-party package or library is a potential attack surface, even after vetting, since packages can be swapped out post-verification.
- **"Shift left" security — building security in from day one — dramatically reduces remediation costs**, but is still an afterthought in many development cultures where shipping features fast takes priority.
- **Post-breach forensic investigation requires specialized skills** most organizations don't have in-house, reinforcing the value of pre-breach preparation (audit logs, monitoring, telemetry) so forensic analysts have the data they need after an incident.