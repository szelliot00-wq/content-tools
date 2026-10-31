# AI exposes a major web security flaw, plus a new kind of voice model

Video ID: `K8NgeOuZmWU`

## Summary
This episode of IBM's *Mixture of Experts* podcast covers three major AI news stories: the PHP2Shell security vulnerability (discovered using AI), Dessa — a novel voice model from Block trained exclusively on audio, and a new benchmark called Cultural Riddles that tests AI on culturally specific puzzles. The episode closes with a field report from IBM TechXchange, where IBM's Field CTO for Data discusses the "Streamhouse" data architecture and how AI is reshaping enterprise data infrastructure and agent identity management.

## Key insights
- **PHP powers ~70% of the web and is critically exposed.** The PHP2Shell vulnerability allows remote code execution on web servers, and patching is non-trivial because upgrading PHP can break legacy systems built around older versions.
- **AI is accelerating both the discovery and exploitation of vulnerabilities.** Two independent firms (Wiz and Opswall) used AI to find these flaws simultaneously, compressing the window between disclosure and potential attack.
- **Critical open-source infrastructure is severely under-resourced.** The PHP Foundation — steward of a language undergirding the majority of the web — has only one full-time employee, highlighting a systemic problem with how society funds and maintains foundational open-source software.
- **"Modernization" has shifted from a nice-to-have to a necessity.** AI-accelerated exploit discovery means organizations can no longer safely neglect legacy systems; the entire dependency stack now requires active review.
- **Dessa (Block) is trained purely on audio — no text.** It achieves fully duplex conversation (talking and listening simultaneously) and can produce natural back-channeling cues like "hmm," but likely trades factual accuracy for conversational naturalness.
- **Fully duplex voice AI requires entirely new evaluation criteria.** Existing benchmarks measure accuracy and consistency; Dessa-style models need metrics for social grace, interruptibility, and conversational flow — categories that don't yet have established standards.
- **The Cultural Riddles benchmark reveals that models struggle with culturally specific language.** Riddles require metaphorical and contextual reasoning beyond pattern-matching, and most training data skews heavily toward English and Western cultures.
- **Current AI benchmarking has a structural flaw.** Models are incentivized to guess rather than say "I don't know," because a guess has nonzero chance of scoring a point while abstaining scores zero — distorting leaderboard results.
- **The "Streamhouse" architecture addresses the data needs of autonomous agents.** It combines lakehouse strengths with real-time stream processing (via Apache Flink), enabling agents to act on distributed, operational data that a traditional lakehouse wasn't designed to serve.
- **AI is lowering the barrier to streaming architectures.** Writing stateful stream-processing jobs — previously complex enough to deter most developers — is now accessible via AI-assisted coding, unlocking better-performing architectures for smaller organizations.
- **Agent identity is an emerging infrastructure challenge.** Autonomous agents are not people, yet they need credentials; the scale and ephemerality of agent identities requires fundamentally rethinking traditional identity and access management.