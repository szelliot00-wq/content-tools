# Have we finally solved social engineering? Plus: World Cup fraud, AI IDs and an IBM/OpenAI collab

Video ID: `10XtOi4Lbes`

## Summary
This episode of IBM's Security Intelligence podcast covers three main topics: whether AI-native operating systems can solve social engineering, the World Cup fraud ecosystem ("Operation Fan Trap"), and IBM's new partnership with OpenAI's Daybreak Cyber Partner Program. Panelists Dave Bales, Kimmy Farrington, and JR Rao debate the promise and limitations of LLM-based defenses, while a guest segment with Jayesh Kamath details IBM's new "Security Harness" application security service built on OpenAI's frontier models.

## Key insights
- **Social engineering won't end — it will shift targets.** LLMs integrated into operating systems could filter attacks before humans ever see them (analogous to spam filters), but the attack surface moves to the AI itself via prompt injection and adversarial manipulation rather than disappearing.
- **LLMs are also vulnerable to social engineering.** Meta's customer service agents were recently tricked into handing over Instagram accounts, illustrating that AI systems can be manipulated just as humans can.
- **Behavioral authentication could replace passwords.** An OS-level LLM that learns your communication patterns, browsing habits, and contacts could confirm identity without credentials — and behavioral patterns are much harder to steal than passwords.
- **Human cognitive overload is the attacker's primary weapon.** Attackers only need one mistake across hundreds of phishing attempts; the only scalable counter is automation (AI) meeting automation (attacks).
- **Multiple agents checking each other offers the best near-term defense.** More agents with narrow, specific contexts reduce single points of failure, though each agent is itself an attack vector.
- **World Cup fraud is industrialized, not sophisticated.** Nearly 4,000 malicious domains were identified exploiting World Cup branding — fake tickets, streaming sites, merchandise, and travel packages. High emotion and urgency cause people to drop their guard around major events.
- **Classic advice still applies:** If a deal looks better than the official offer, assume it's a scam. Buy from known sources, and treat urgency in any sales pitch as a red flag.
- **Agent identity is the next unsolved IAM problem.** Estonia is exploring giving AI agents their own personal ID codes for accountability and permission scoping, but an authenticated malicious agent is potentially more dangerous than an unauthenticated one. Scaling identity management to millions of agents will break existing architectures.
- **IBM + OpenAI "Security Harness" enables AI-driven code vulnerability scanning.** The service uses OpenAI's frontier models within an enterprise-controlled harness to scan code, identify chained vulnerabilities, and prove exploitability — work that previously required human security researchers and couldn't scale.
- **The human-AI feedback loop is essential.** Keeping humans "in the loop or on the loop" at critical decision points is the safest near-term approach — harvesting AI's strengths while guarding against hallucination, poisoning, and model drift.