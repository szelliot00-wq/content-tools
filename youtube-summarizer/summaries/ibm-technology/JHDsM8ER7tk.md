# Can you social engineer an AI? Plus: AI worms and the nonhuman identity problem

Video ID: `JHDsM8ER7tk`

## Summary
This episode of IBM's Security Intelligence podcast covers three cybersecurity topics: Meta's AI customer support agent being social-engineered into handing over Instagram account credentials, a University of Toronto research project creating a self-replicating AI worm, and the Sofos State of Identity Security 2026 report highlighting nonhuman identity (NHI) vulnerabilities. The panel — Claire Nunez, Jeff Kroom, and Nick Bradley — explores what these stories reveal about AI's current limitations and the evolving threat landscape.

## Key insights

- **AI lacks "street smarts" / wisdom.** AI agents can be highly knowledgeable but naive — they follow instructions literally and won't question suspicious requests unless explicitly told to. The panel distinguishes between intelligence (which AI has) and wisdom (which it doesn't yet have).
- **Prompt specificity is critical for AI security.** Customer-facing AI agents will do whatever they're instructed to do. Organizations must explicitly define what agents *cannot* do, not just what they can — otherwise helpfulness becomes a vulnerability.
- **Social engineering works on AI just as it does on humans.** Help desk password resets are already one of the most reliable human social engineering attacks; AI agents face the same risk, just at scale and speed.
- **The AI worm is a logical evolution, not a surprise.** As LLMs shrink in size and become more portable, self-replicating AI malware becomes increasingly viable. The same capability used offensively (find and exploit vulnerabilities) can be flipped defensively (find and patch them).
- **Open-source AI models remove guardrails.** Attackers using open-source models avoid oversight from providers like Anthropic or OpenAI, making abuse harder to detect or prevent — and that ship has already sailed with millions of models publicly available.
- **Nonhuman identities are a blind spot.** 41% of identity breaches involved nonhuman identities (service accounts, API keys, AI agents), yet only ~1/3 of organizations audit or rotate them. Unlike user accounts, nobody actively watches these.
- **Ephemeral, least-privilege identity management is the solution.** AI agents should be provisioned with just-in-time, minimal permissions that expire immediately after use — but most organizations and agentic frameworks (e.g., OpenClaw) aren't built this way yet.
- **AI is a "fast fool."** Speed amplifies mistakes — an AI agent with broad permissions can make a catastrophic error far faster than a human would, because there's no human-paced gate to catch it.
- **The arms race is already underway.** Attackers are using AI regardless of whether defenders choose to. Opting out means falling behind; the only viable path is using AI defensively at least as aggressively as attackers use it offensively.