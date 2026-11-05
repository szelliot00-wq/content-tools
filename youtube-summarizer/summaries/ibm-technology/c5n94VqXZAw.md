# Did the Knicks’ phishing test go too far? Plus, hackers pose as IT in Teams

Video ID: `c5n94VqXZAw`

## Summary
This episode of IBM's Security Intelligence podcast covers three cybersecurity stories: MSG's controversial phishing test using a fake championship ring email, a Microsoft Teams-based social engineering campaign where hackers impersonate IT staff after mail-bombing targets, and recently disclosed PHP vulnerabilities affecting hundreds of thousands of unpatched instances. Panelists Patrick Fussell (X-Force Red), Nikki Robinson (AI & Development), and Srinivas Tummalapenta (CTO, Cybersecurity) discuss attacker psychology, defense-in-depth strategies, and the broader challenge of securing open-source infrastructure.

## Key insights
- **Phishing tests work best when timely and emotionally resonant** — the MSG ring email exploited genuine excitement, which is exactly what real attackers do. The test served both internal training and broader public awareness.
- **AI has collapsed the skill gap for phishing** — attackers can now produce convincing, personalized emails at scale, making "look for bad spelling" outdated advice. Business email compromise techniques once reserved for executives are now deployed broadly.
- **Defense-in-depth is essential for email security** — no single tool is enough. DMARC, DKIM, SPF, external sender flags, and domain-checking should all be layered together.
- **The Teams attack exploits legitimacy** — because the invite comes through Microsoft's own infrastructure, it appears trustworthy. Users should know real IT staff will never ask for credentials or request remote access they don't already have.
- **Default skepticism is the right posture** — start by treating all unexpected communications as untrusted, verify before acting, and use the delete button freely. Urgency in an email ("click now") is itself a red flag.
- **Asset inventory is a prerequisite for vulnerability response** — most organizations can't answer "what PHP versions are we running?" Knowing your full software estate is the foundation of any effective patch strategy.
- **The PHP vulnerabilities are serious but hard to exploit in practice** — complex memory conditions required mean defenders have detection opportunities. It's not Log4j-level, but unpatched end-of-life instances (263,000+ found by Shadow Server) remain a real risk.
- **Open-source infrastructure is chronically underfunded** — the PHP Foundation has one full-time employee. Consortiums like Red Hat and community engagement are emerging as partial solutions, but the gap between dependency and support remains wide.
- **Hygiene is becoming a first-order priority** — autonomous patching and remediation are now top enterprise requests. Getting hygiene right reduces the attack surface; neglecting it multiplies entry points.