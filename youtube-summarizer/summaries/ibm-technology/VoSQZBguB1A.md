# The PHP bug threatening the web. Plus, who's auditing AI?

Video ID: `VoSQZBguB1A`

## Summary
This episode of IBM's Security Intelligence podcast covers three cybersecurity stories: critical PHP vulnerabilities (dubbed "PHP to shell") discovered via AI before patches were available, Anthropic's program embedding external AI model evaluators on its campus, and the hijacking of 333 Tor exit nodes through reused credentials and a Linux backdoor. Panelists Nick Bradley, Don Cohen, and Jim Gwinn analyze the practical implications of each story and debate broader questions around patch management, AI auditing models, and the trustworthiness of anonymous networks.

## Key insights
- **PHP powers ~70% of the web, making it a massive single point of failure.** Versions 8.1 and earlier will not receive patches, leaving countless legacy systems permanently vulnerable and creating a painful dilemma: upgrade and break legacy dependencies, or stay exposed.
- **Information about the PHP exploits leaked before patches were ready**, which inverted the normal responsible-disclosure process and created a window where attackers had actionable exploit details before defenders had fixes.
- **AI tools (specifically Sol 56) were used to discover the PHP vulnerabilities**, raising the broader question of how organizations can proactively use the same frontier AI tools attackers use to harden their own software before release — a "secure by design" imperative.
- **External security audits challenge internal assumptions.** The PHP Foundation had not undergone an external audit in years; having an outside perspective surfaces blind spots that internal teams overlook due to familiarity bias.
- **Anthropic's embedded evaluator program drew skepticism** from panelists, who viewed its tiered access and publication-approval structure as more of a publicity move than a rigorous accountability mechanism.
- **Jim Gwinn proposed a better model: cross-auditing among competing AI frontier companies**, analogous to how the Big Four accounting firms rotate peer reviews of each other's audit work — a system with a century of refinement that increases public trust through genuine third-party scrutiny.
- **Tor should never be assumed secure.** Panelists universally treat Tor exit nodes as potentially compromised by default; the hijacking in this case stemmed from basic credential hygiene failures, not a sophisticated attack on the protocol itself.
- **Bad actors are not immune to bad security practices.** The reused password that enabled the Tor breach mirrors a pattern seen repeatedly when law enforcement or rival actors compromise threat-actor infrastructure — poor hygiene affects everyone.