# First findings from Project Glasswing

Video ID: `ftUlJzuzdU4`

## Summary
This episode of IBM's Security Intelligence podcast features host Matt Kosinski and panelists Kimmie Farrington, Dustin "EvilMog" Heywood, and Curtis Pitts discussing early findings from Project Glasswing — Anthropic's initiative giving select organizations access to its Mythos AI vulnerability discovery model. The conversation covers Cloudflare's published learnings from running Mythos against 50+ repositories, a significant CISA credential leak via a contractor's GitHub repo, TeamPCP's alleged breach of GitHub source code, and the 28th anniversary of L0pht Heavy Industries' congressional testimony — all converging on a central theme: the same fundamental security problems keep recurring.

## Key insights

- **The harness matters most.** Pointing Mythos (or any LLM) at a repo and asking it to "find bugs" doesn't work well — context windows overflow and the model wanders. Cloudflare found success by building an orchestration harness that breaks the process into discrete steps handled by specialized sub-agents.
- **Specialized, purpose-built agents outperform general ones.** Expecting one massive model to do everything produces noise. Small, focused agents with narrow tasks produce actionable results — echoing the Unix philosophy and microservices architecture debates of past decades.
- **AI safety guardrails created friction.** Mythos sometimes refused tasks and required rephrasing. Panelists noted this mirrors a recurring pattern: controls that introduce too much friction get worked around, which is itself a governance failure.
- **Proof generation and exploit chaining are Mythos's standout capabilities.** It excels at linking small, individually minor issues into full attack chains and writing working proofs of concept — more so than other LLMs.
- **Verify AI output — you own the results.** Mythos returned five supposed vulnerabilities in the curl codebase; only one was real. Treating frontier models as just another scan tool requiring human validation is the right posture.
- **Defense-in-depth over patch speed.** Cloudflare argued that hardening architecture so exploitation is difficult even when bugs exist matters more than compressing patch cycles — making the vulnerability disclosure-to-patch window less critical.
- **The CISA leak was a layered governance failure.** A contractor committed plaintext credentials, tokens, and passwords to a public GitHub repo for months. Panelists emphasized it's never one person's fault — multiple governance controls had to fail simultaneously.
- **SBOMs are only as good as what feeds them.** Many suppliers can't answer basic questions about where their code was developed or compiled, undermining software bill of materials as a supply chain security tool.
- **The L0pht parallel is striking.** The vulnerabilities L0pht described to Congress in 1998 — weak authentication, unencrypted protocols, fragile infrastructure — remain the blueprint for breaches today. The gap between what security practitioners know and what decision-makers act on is still the core unsolved problem.
- **The industry needs to rebuild its junior talent pipeline.** Years of eliminating entry-level roles has destroyed institutional knowledge and stalled the creation of new senior practitioners — identified as a more pressing problem than tooling.
- **Generational cyber hygiene education is essential.** Training end users — and children — on basic security practices reduces the insider threat surface that exists at every internet-connected endpoint.