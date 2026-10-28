# Open Source Security in the Age of AI

Video ID: `5WlmyncEcNM`

## Summary
The video examines the growing security crisis in open-source software, which now makes up ~90% of enterprise codebases. AI has dramatically accelerated vulnerability discovery, but remediation — the harder problem — hasn't kept pace, creating a dangerous gap that attackers can exploit. The video introduces two coordinated efforts, Lightwell and Akrites, designed to close that gap by connecting discovery, remediation, validation, and disclosure into a unified pipeline.

## Key insights
- **Open source is critical infrastructure running on a best-effort model** — 90% of enterprise code is open source, much of it maintained by small volunteer teams never designed to support global infrastructure at scale.
- **AI has collapsed vulnerability discovery timelines** — work that took skilled researchers weeks now takes minutes; Anthropic's Project Glass Wing found 2,300 vulnerabilities across 400 projects, including a 27-year-old bug no human had caught.
- **Attackers have the same discovery tools** — the speed-up is symmetric, making the real race about who reaches remediation first: a patch or an exploit.
- **Finding bugs faster doesn't automatically make anyone safer** — if the ecosystem can't absorb the volume of fixes, accelerated discovery can actually make things worse.
- **Remediation is the hard part** — a safe fix requires mapping affected versions and dependencies, assessing business impact, developing and testing the patch, regression testing, compatibility validation, and production deployment without breakage.
- **Upstream contribution beats private forks** — contributing fixes back to the original project strengthens the ecosystem for everyone; isolated forks create fragmentation.
- **No single actor can secure open source alone** — it requires coordinated effort across AI providers, vendors, cloud platforms, security firms, maintainers, and nonprofits.
- **Lightwell** focuses on discovering vulnerabilities, engineering backported remediations (rather than forcing version upgrades), validating fixes, and contributing them upstream through trusted repositories.
- **Akrites** acts as a shared incident response team — handling coordinated discovery, maintainer engagement, deduplication, and synchronized disclosure so maintainers face one predictable partner rather than chaos.
- **The defining challenge ahead is scale** — the future of open-source security belongs to whoever can remediate vulnerabilities safely, responsibly, and at the volume AI-assisted discovery now demands.