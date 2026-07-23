# GPT-Red: Can AI red teams stop prompt injections?

Video ID: `g4CNcUAqM4Q`

## Summary
This episode of IBM's Security Intelligence podcast covers three cybersecurity topics: OpenAI's internal automated red-teaming model GPT Red, an open-source scam interception tool called Scam Buster, and Bruce Schneier's essay on AI widening the gap between cybersecurity skills and abilities. Four panelists — host Matt Kazinsky, Michelle Alvarez, Nick Bradley, and Kimmy Farrington — discuss the practical implications of each development for both defenders and attackers. The overarching theme is that AI is a powerful force multiplier, but one that cuts both ways and must be wielded with intentionality.

## Key insights
- **GPT Red achieves dramatic results against prompt injection:** Fake chain-of-thought attacks dropped from 95% effective on GPT 5.1 to just 10% on GPT 5.6, with GPT Red credited for that improvement. It outperformed human red teamers 84% vs. 13% in head-to-head testing.
- **Specialized AI beats generalist AI for security tasks:** The panel frames GPT Red as a "brain surgeon" model — purpose-built for one problem — rather than a general-purpose model, and sees this specialization as the right direction for AI security tooling.
- **Adversarial parity is inevitable:** Anything built for defenders will be replicated by attackers. The Cobalt Strike analogy was raised: open-weight models with no safeguards give adversaries a path to their own prompt-injection LLMs.
- **Red-teaming models offer better guardrails than classifiers:** OpenAI argues that robustness should come from resistance to malicious instructions, not from refusing legitimate requests by default — a meaningful critique of over-cautious classifier-based safety approaches.
- **Scam Buster flips social engineering back on attackers:** The tool poses as a victim to string scammers along while quietly harvesting their TTPs, infrastructure, and IOCs for threat intelligence and law enforcement handoff — a rare AI application the panel found genuinely convincing for combating social engineering.
- **AI-vs-AI scam loops are coming:** The panel anticipates scammers deploying their own AI filters to detect and skip AI-generated "victims," potentially creating automated adversarial loops — though even tying up attacker resources has some defensive value.
- **The skill-vs-ability gap is widening on both sides:** Schneier's point that gaining skills instills a moral code was debated, but the panel agreed that AI granting ability without skill affects defenders and attackers equally — both sides risk being unable to function when AI can't fill the gap.
- **Ability without skill may make attackers less precise but more chaotic:** Nick argued low-skill attackers are easier to catch; Kimmy countered they're more dangerous precisely because they don't know what they'll trigger.
- **The practical takeaway: don't let AI make you lazy.** The panel's consensus rule of thumb — attributed to a prior guest — is to ensure you could still do your job if AI disappeared tomorrow. Use AI as a force multiplier, not a replacement for foundational skill.
- **Entry-level practitioners bear the greatest risk** from de-skilling; experienced professionals should focus on helping newer colleagues build genuine foundations rather than relying entirely on AI-assisted workflows.