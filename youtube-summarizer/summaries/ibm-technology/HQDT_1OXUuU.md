# Fable 5, GPT-5.6 and the high stakes of AI safeguards. Agentic ransomware, ClickFix reigns supreme

Video ID: `HQDT_1OXUuU`

## Summary
This episode of IBM's Security Intelligence podcast covers three major cybersecurity topics: the release of Anthropic's Fable 5/Mythos 5 and OpenAI's GPT-5.6 Sol with their new AI safeguards, the emergence of JADEPUFFER (debated as the "first agentic ransomware"), and ClickFix's rise as the dominant social engineering attack vector. The episode closes with a deep dive from researcher Itzhak Chimino into UnregStealer, a targeted browser-based credential theft campaign hitting Latin American financial institutions.

## Key insights
- **AI safeguards are necessary but insufficient**: Guardrails only constrain good actors — malicious models like WormGPT already exist with no restrictions, and open-weight models (e.g., Zhipu AI's GLM 5.2) further lower the barrier by making frontier-level capabilities publicly available.
- **Overly strict classifiers can backfire**: Some reports indicate that new model safeguards have degraded performance, effectively penalizing legitimate users while doing little to stop determined bad actors.
- **Agentic ransomware is inevitable regardless of JADEPUFFER's classification**: Even if JADEPUFFER isn't truly "agentic," the pattern — LLM-driven attack kill chains operating at machine speed — was a predictable evolution and will only become more capable and common.
- **Speed is the key threat from agentic attacks**: What took human attackers days (e.g., gaining domain control) can now happen in seconds, compressing the window defenders have to detect and respond.
- **ClickFix works because it bypasses all technical controls**: By manipulating users into self-executing malicious commands, it sidesteps AV, EDR, and email filters entirely — and the tech industry inadvertently trained users to accept terminal commands from help desks, making the lure plausible.
- **Developers are high-value ClickFix targets** because compromising a developer machine enables supply chain poisoning at the source, amplifying the blast radius far beyond a single endpoint.
- **UnregStealer uses human-gated payload delivery**: The stealer kit is only served to select victims (not sandboxes), making automated detection largely ineffective and signaling a human operator choosing targets based on value, not volume.
- **Locking down browser extension installation is the single highest-leverage defense** against UnregStealer — a Chrome extension allow-list policy breaks the most critical link in the attack chain before the stealer ever reaches the page.