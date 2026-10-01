# Can you trust your chatbot? Inside three AI-powered cyberattacks

Video ID: `dHn0qzSDMO0`

## Summary
This episode of IBM's Security Intelligence podcast covers three AI-enabled cyberattacks reshaping the threat landscape: the "Dark Sourcery" campaign poisoning AI chatbot responses with malicious content, a lone threat actor using LLM-assisted tools to exploit critical vulnerabilities across multiple platforms, and an AI agent swarm that breached hundreds of PaperCut print management instances across 48 countries. The panel — cybersecurity professionals from IBM — connects these attacks to longstanding security fundamentals while highlighting how AI accelerates attacker capabilities. The episode also marks the final appearance of host Matt Kosinski, with Patrick taking over going forward.

## Key insights
- **AEO (Answer Engine Optimization) poisoning is the new SEO poisoning.** Attackers seed the web with fake content so AI chatbots like ChatGPT and Gemini cite it in responses — e.g., fake customer support numbers. 91% of regular chatbot users don't verify AI-provided answers, making this highly effective.
- **AI is a force multiplier for attackers.** A single threat actor used LLM-generated scripts to exploit critical vulnerabilities in Ubiquiti, WordPress, and Zyxel devices within ~20 days of patches being released, stealing documents from at least one Western government.
- **AI agent swarms enable attacks at unprecedented speed and scale.** One threat actor deployed hundreds of agents to compromise 440 PaperCut instances across 395 organizations in 48 countries — going from zero to remote code execution in roughly four hours.
- **Even attackers can't fully control their own agents.** The PaperCut attacker attempted to limit which countries were targeted; the agents ignored those constraints and hit unintended targets anyway — a sign that agent controllability is unsolved for defenders and attackers alike.
- **Basic cyber hygiene remains the most effective defense.** Multi-factor authentication, rapid patch deployment, zero trust architecture, least-privilege access, and network segmentation would have blunted all three attacks discussed.
- **People over-trust AI the same way they over-trusted early search results.** The panel draws a direct parallel to SEO poisoning and War of the Worlds-style information manipulation — the attack vector is new, the human vulnerability is ancient.
- **Agents inherit the same trust problem humans have, potentially at machine scale.** If an AI agent consumes poisoned web content without verification, it compounds the disinformation problem — and most organizations haven't thought through agent-level access controls.
- **"AI is the most helpful insider threat we've ever had"** — a recurring panel observation that AI's broad system access and user trust make it a uniquely dangerous attack surface when misconfigured or compromised.