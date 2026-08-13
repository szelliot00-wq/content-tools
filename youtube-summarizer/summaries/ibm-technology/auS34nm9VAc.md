# The OWASP LLM Top 10 has a few surprises for you

Video ID: `auS34nm9VAc`

## Summary
This episode of IBM's Security Intelligence podcast covers the 2026 OWASP Top 10 for LLM Applications, new CISA SBOM guidance, and highlights from Black Hat 2026. Three panelists — host Matt Kosinski, Seth Glasgow (Cyber Range Executive Advisor), and Ryan Anschutz (X-Force IR North America Lead) — discuss how AI agents are emerging as a major new attack surface, why security lists are only useful when operationalized, and what defenders should actually do about these risks.

## Key insights
- **Excessive agency jumped to #3 on the OWASP LLM list** (up three spots), reflecting growing recognition that AI agents should be treated like privileged identities — the risk isn't the model itself, but what it can do.
- **Prompt injection is #1 in practitioner concern but nearly absent from real incident databases**, likely because heavy defensive investment has suppressed incidents — a "defensive bias" that makes it look solved when it's just contained.
- **Misinformation is underrated by practitioners but overrepresented in incident data.** Users are conditioned to expect some AI hallucination, which makes them blind to intentional poisoning or model drift — especially dangerous when an agent acts on bad information at machine speed.
- **The OWASP project leads' core message: stop trying to build an unfoolable model; build the system around it so that when it fails, nothing critical breaks.** This is cyber resilience applied to AI — defense in depth, not perfection.
- **"Intent collusion" is a novel and dangerous attack technique** demonstrated at Black Hat: rather than tricking an agent into doing something obviously wrong, attackers persuade it that their goal *is* the user's goal. A malicious calendar invite alone was shown to trigger credential theft, data exfil, and code execution.
- **The controls that actually worked against agentic attacks were the ones AI had no vote in** — least privilege, segmentation, hard boundaries, and identity controls. Classic principles, not AI-specific solutions.
- **92% of organizations that experienced an AI-related breach lacked proper access controls** on their AI implementations, reflecting a widespread rush to deploy before securing.
- **Both the OWASP list and SBOMs share the same failure mode: treated as checklists rather than operational tools.** The panelists recommend using the OWASP list as a tabletop exercise foundation (can you detect, contain, and reconstruct an attack?) and integrating SBOMs directly into vulnerability management workflows.
- **AI agents compress attacker dwell time dramatically** — an agent operating on stolen credentials can move far faster than a human attacker, shrinking the window defenders have to respond.