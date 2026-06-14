# Fable 5 launches while Siri partners with Gemini | Now Shipping

Video ID: `rxDDuWyG2vA`

## Summary
*Now Shipping* is a weekly AI news show hosted by Mike BelSito for product managers and builders, produced by Mind the Product. This episode covers three major AI developments from a single week: OpenAI's Codex expanding beyond developers, Anthropic launching Claude Fable 5 with a novel safety routing architecture, and Apple's ground-up rebuild of Siri powered by Google Gemini. The core argument throughout is that AI is shifting the assumptions product teams have long held — about who their users are, how models behave, and what competing with native OS assistants even means. It is most relevant to product managers, designers, and anyone building software products in an AI-saturated landscape.

## Key insights
- **Codex's fastest-growing segment is non-developers:** 20% of Codex's 5 million weekly users are non-engineers (product managers, designers, marketers, bankers, investors), and this group is growing 3x faster than the developer core — despite Codex being launched explicitly as a coding agent.
- **Non-developers use Codex for automation, not code:** They use it to move data between tools, auto-generate specs from research, turn Figma files into structured handoff docs, and build lightweight automations — without writing a single line of code.
- **OpenAI added 6 role-specific plugins across 62 apps and 110 skills:** Examples include a data analytics plugin (Snowflake, Databricks, Tableau), a creative production plugin (Figma, Canva, Shutterstock), and a product design plugin, with more coming for finance, legal, and consulting.
- **Claude Fable 5 is Anthropic's first publicly available Mythos-class model:** It was previously locked behind Anthropic's most restricted research program since April, limited to vetted cybersecurity researchers under tight controls due to concerns about misuse potential.
- **Fable 5 introduces a "safety trapdoor" — a third model state:** When a query touches high-risk domains (cybersecurity, biology, chemistry), classifiers intercept it before it reaches Fable 5 and reroute it to Claude Opus 4.8. The user is notified, and billing adjusts accordingly.
- **This creates a new UX design problem:** Products built on most models only need to handle two states — model helps or model refuses. Fable 5 adds a third: model hands off to a different model with different capability, latency, and output quality. Product teams must explicitly design for this fallback experience.
- **Anthropic's safety concerns are real and contemporaneous:** The same week Fable 5 launched, Anthropic's head of research institute Marina Favaro and co-founder Jack Clark published a blog post suggesting AI labs should consider slowing or pausing frontier AI development and building international monitoring agreements. Mike notes this tension — releasing their most powerful public model while simultaneously sounding an alarm.
- **Apple rebuilt Siri from the ground up at WWDC:** The new Siri can hold back-and-forth conversations with maintained context, pull from personal data (emails, messages, photos), and take real actions inside apps — not just open them (e.g., rescheduling meetings, checking in for flights, adding to shopping lists).
- **Google Gemini is powering the most capable parts of the new Siri:** Apple, known for its tightly controlled ecosystem, chose to partner with Google rather than rely solely on its own Apple Intelligence on-device models for the most demanding tasks.
- **This signals that even Apple can't win the model race alone:** Apple has its own models but acknowledged they operate at a different capability tier than frontier labs, making partnership preferable to competing directly.
- **Siri now threatens traditional in-app engagement:** For years, Siri's limitations were a moat — users had to open apps directly. The new Siri can trigger app features through conversation without users ever opening the app. However, Apple's WWDC announcements typically take 12–18 months to fully ship at scale.
- **Apple's Siri integration is also an opportunity:** Developers can expose specific app capabilities directly to Siri, letting users trigger features conversationally — a potential distribution and engagement gain, not just a threat.

## Use cases
- **Product managers building tools for non-technical users** who need to reconsider onboarding and AI feature sets now that non-developers are using coding agents at scale.
- **Teams building B2B SaaS, collaboration tools, design systems, or PM platforms** who can no longer assume their power users are technical and need to audit who is actually getting value from their product.
- **Product builders using Claude Fable 5 in their stack** who need to map out what happens when a query gets rerouted to Opus 4.8 — especially teams building in security, biotech, chemistry, or research verticals.
- **iOS app builders** who need to start thinking now (not in 18 months) about how their product works inside the new Siri experience and which capabilities to expose via Siri integration.
- **Teams doing user research or competitive analysis** who want to understand how AI is reshaping their user base in real time, not just at planned research intervals.
- **Founders and PMs evaluating model providers** who need to understand the architectural and UX implications of model-switching behaviors introduced by safety systems like Fable 5's trapdoor.
- **Anyone building agentic workflows** who can use Codex's plugins as a reference model for how role-specific agent interfaces can unlock new user segments without changing the underlying product.

## Patterns & frameworks

**The Three-State Model UX Pattern**
Historically, products built on LLMs designed for two states: (1) model helps, (2) model refuses. Fable 5 introduces a third state: (3) model hands off to a different model. BelSito argues product teams must explicitly design for all three states rather than letting the model provider's architecture make UX decisions by default. Applied to Fable 5: if your product touches high-risk domains, design a deliberate fallback experience for the rerouted-to-Opus state.

**"Who's Actually Using Your Product" Audit**
BelSito frames a recurring mental model: in fast-moving AI markets, user segments shift faster than traditional product discovery cycles. The old playbook — find product-market fit with a specific group, then expand — is too slow. The pattern he advocates is continuous monitoring of who is actually getting value from your product, because AI tools are unlocking unexpected user segments (like non-developers in Codex) before teams even plan for them.

**Threat-vs-Opportunity Reframe for Platform Shifts**
Applied to the new Siri: the default reaction is to file it under "Apple stuff to deal with later" or treat it as a competitive threat (Siri replaces app engagement). BelSito's framework is to flip the question — not "can Siri replace my app?" but "what does my app become when Siri is the interface layer on top of it?" This reframe turns a platform shift into a distribution and capability opportunity for teams that move early.

**Safety-Capability Tension as a Product Signal**
BelSito surfaces an implicit framework: when a frontier AI company simultaneously releases a powerful model and publishes warnings about slowing down AI development, that tension is itself signal — either of genuine institutional uncertainty, strategic positioning for an IPO, or both. For product builders, the takeaway is that the safety architecture decisions of AI providers (like the trapdoor) will directly shape your product's behavior, so you need to understand and design around them rather than treat them as invisible infrastructure.