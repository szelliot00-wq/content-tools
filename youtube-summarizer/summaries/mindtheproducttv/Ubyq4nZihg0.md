# Cursor launches Origin to pounce on GitHub's outage

Video ID: `Ubyq4nZihg0`

## Summary
"Now Shipping" is a weekly AI news show hosted by Mike Belceto, produced by Mind the Product, covering AI developments relevant to product builders. This episode covers three stories: Cursor's launch of a GitHub competitor called Origin (timed with a major GitHub outage), Anthropic's rollout of invisible AI watermarking in compliance with EU law, and Linear's data report revealing how AI is actually changing team behavior at scale. The episode's core argument is that AI is accelerating execution but not improving judgment — teams are doing more, not working less. It is most relevant to product managers, engineering leaders, and founders making decisions about developer tooling and AI adoption strategy.

## Key insights
- Cursor launched Origin on August 18th, a full code-hosting platform (repos, PRs, forking, collaborative editing) that directly competes with GitHub, on the same day GitHub suffered a 6-hour worldwide outage with ~20% global failure rate.
- SpaceX AI acquired Cursor in a $60 billion deal on August 14th, four days before Origin launched — making Origin a strategic statement from SpaceX AI, not just a product launch.
- GitHub has had 257 documented outages in the past year, and there is already visible high-profile user churn, giving Cursor a credible opening.
- Origin is designed to be interoperable with GitHub — your existing repos sit alongside Origin repos — deliberately lowering the switching cost, which is typically the #1 reason users stay on platforms they dislike.
- The developer tools market is now framed as a two-platform fight: Microsoft (GitHub) vs. SpaceX AI (Cursor/Origin), with users potentially self-sorting into camps, similar to the Apple vs. PC dynamic.
- Anthropic is now watermarking every Claude response using an approach called **SynthID Text**, developed by Google DeepMind in 2024. The watermark is invisible to human readers but machine-detectable via a detection API Anthropic is releasing.
- The watermark works by encoding a pattern in low-stakes stylistic choices (e.g., "overcast" vs. "gray") that are otherwise arbitrary in quality terms.
- This is not Anthropic-specific: the EU AI Act's transparency code requires all major model providers to make AI-generated content machine-detectable, and other major model developers have signed the same code of practice.
- Light editing does not remove the watermark; only a complete rewrite does, making it highly persistent.
- Social media backlash was significant, with users threatening to cancel subscriptions — but the host notes this is moot since all major providers will comply, making it an industry-wide infrastructure shift.
- Linear's data report (127,000+ paid users, Jan–June this year) found AI adoption more than doubled across every function: PMs went from 12% → 34% (fastest-growing function), CEOs at 200+ person companies went from 9% → 36% (biggest single jump).
- AI is now authoring nearly 50% of all issues created in Linear; two years ago it was fewer than 1 in 1,000.
- Pull requests shipped are up 111% over two years. Teams using a coding agent went from 21 PRs/week to 65; teams without went from 8 to 10 — nearly all the productivity growth is on the agent side.
- Non-engineers shipping code: PM pull requests tripled from 3% to 10% of all PRs.
- **Planning time did not move.** Time spent on customer research, documentation, and project planning held flat across all functions, even as execution metrics surged everywhere else.
- AI is accelerating how fast teams build, but it is not helping teams decide what to build — judgment, customer discovery, and prioritization take as long as they always have.
- Work volume went up, not down. Linear explicitly calls this **Jevons Paradox**: AI time appeared as a new layer on top of existing work; nothing shrank to make room. Teams are doing more with the same headcount, not saving time.

## Use cases
- **Developer tool purchasing decisions**: Engineering and product leaders evaluating whether to migrate from or supplement GitHub with a new platform.
- **Platform lock-in risk assessment**: Any team whose workflows, context, and muscle memory are deeply embedded in a vendor now owned by a larger player (Microsoft, SpaceX AI) should audit their exposure.
- **AI watermarking compliance planning**: Product teams building on top of LLM APIs (emails, reports, code summaries, content generation) need to plan for their outputs being detectable as AI-generated and communicate that to users.
- **Setting user expectations around AI transparency**: Platforms that help users generate professional or academic content need a clear transparency policy before detection becomes routine.
- **Business case for AI adoption**: Leaders being asked to justify AI investment with time-savings ROI should use the Linear data to reframe the argument — the outcome is more output per person, not fewer hours worked.
- **PM role evolution**: Product managers seeing their share of code contributions triple need to understand what new responsibilities that creates and what skills to develop.
- **AI tooling strategy for cross-functional teams**: Go-to-market, non-technical, and executive teams are rapidly adopting AI features — tooling decisions can no longer be made purely from an engineering lens.
- **Product strategy and roadmap prioritization**: The finding that planning time is unchanged reinforces investing in customer research and judgment capabilities rather than assuming AI will handle strategy.

## Patterns & frameworks

**Jevons Paradox (applied to AI adoption)**
Named economic principle: when a resource becomes more efficient, consumption of that resource tends to increase rather than decrease. Linear's data shows AI made execution faster, but teams filled the freed capacity with more work rather than working fewer hours. Use this to pressure-test any AI ROI argument built on headcount reduction or time savings — the more likely outcome is expanded output at the same cost, not the same output at lower cost.

**Interoperability as a switching cost reduction strategy**
Rather than demanding full migration, Origin is designed to sit alongside GitHub. This is a deliberate product strategy: remove the primary reason users stay on a painful platform (sunk cost and migration effort) by making the new platform additive rather than replacing. A pattern applicable to any challenger product entering a market with entrenched incumbents.

**Timing a launch to a competitor's crisis**
Cursor/SpaceX AI may have deliberately held Origin's launch in reserve and released it during GitHub's worldwide outage. Whether planned or lucky, the result is a case study in launch timing — a challenger's message lands hardest when the incumbent is publicly failing.

**SynthID Text watermarking**
Google DeepMind's technique for embedding an invisible, persistent signature in AI-generated text by systematically influencing low-stakes word choices. The pattern encodes a detectable key that survives light editing but requires a full rewrite to remove. Relevant to any product team making decisions about content provenance, academic integrity tooling, or AI disclosure policies.

**The "judgment work stays human" thesis**
A repeatable observation across the Linear data: AI compresses mechanical execution (writing issues, generating code, drafting PRs) but leaves discovery, prioritization, and customer judgment untouched. This serves as a framework for deciding where to invest AI tooling — focus it on execution tasks and preserve human bandwidth for strategic judgment.