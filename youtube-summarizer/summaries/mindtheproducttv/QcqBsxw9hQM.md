# Malleable Software: When Everyone Can Build, What Makes a Great Product? Dave Killeen

Video ID: `QcqBsxw9hQM`

## Summary
Dave Killeen, Field Chief Product Officer at Pendo, argues that AI has fundamentally changed the game for product builders — not just as a productivity tool, but as a complete redefinition of how software gets built and coordinated. His core claim is that "taste" (human judgment as a competitive moat) is no longer sufficient; the real edge now belongs to those who can spot market signals at scale, bend their workflows around AI systems, and rigorously validate that what they build actually matters to users. He shares his hands-on experience building Dex, a personal AI operating system, as a concrete case study. The talk is most relevant to product managers, founders, and product leaders navigating the AI-accelerated software landscape.

## Key insights
- **The "taste as moat" argument is collapsing.** Dave previously championed the idea that AI is a sous chef and PMs are the head chefs with irreplaceable taste. He now believes this is a "get out of jail free card" that understates how much the game has changed.
- **December marked a turning point.** Andrej Karpathy noted AI had crossed a "threshold of coherence" — models became reliably useful, and the bottleneck shifted from code generation to upfront clarity of thought.
- **Compound engineering applied to knowledge work.** AI in the loop learns from mistakes and compounds in effectiveness over time — Dave extended this concept beyond engineering into his own personal operating model.
- **GitHub Trending is the earliest market radar.** Before a technology becomes a product category or analyst report topic, it starts as a scrappy repo. Dave runs a nightly agent that scans GitHub Trending, checks licensing, rates repos on a 1–10 enthusiasm scale, explains relevance in plain English, and automatically adds ideas to a shared roadmap.
- **Open source is eating defensible features.** Examples: "Twenty" is a fully functioning open-source CRM one person can clone and ship; "Open Design" is an open-source Figma clone built by one developer in one week. Features that felt expensive and defensible are becoming free building blocks.
- **Offline AI is an imminent disruption.** Google's Edge Gallery demo runs a frontier-class model entirely on a phone in airplane mode. Google's "Turbo" compression research was reverse-engineered by the open-source community (using the math paper alone, no released code) to run powerful models on a MacBook Air.
- **Competitors can already point AI at your UI to infer your product.** The same techniques used to reverse-engineer Google's paper can be applied to your help pages, UI patterns, and documentation.
- **The bottleneck is now coordination, not productivity.** When building gets cheap, the constraint shifts to getting the whole organization moving smarter — redesigning the environment, not just handing people tools.
- **Most orgs treat AI as a faster horse.** Buying licenses and hoping people figure it out is equivalent to handing someone a Ferrari without telling them how to take the handbrake off. The answer is intentional redesign of workflows.
- **Ramp's "Glass" as a benchmark.** Ramp built an AI co-worker for every employee that knows them, their team, and information flows across the whole business — agent-to-agent and human-to-agent, eliminating silos.
- **200 brilliant ideas is a coordination problem, not a backlog.** An AI-assisted ideation system produces so many good ideas that the real challenge becomes a system-of-work problem, not an idea-quality problem.
- **Dave's factory: a Kanban board where each column triggers a different Claude skill.** Moving a card to "10X" prompts Claude to channel Steve Jobs and challenge the idea. Moving to "PRD" generates specs agents can execute against. Up to 20 Claude Code instances build in parallel on a VPS.
- **100x multiplier is real.** That system wrote 17,500 lines of code in 2.5 hours — work Dave estimated would have taken 5 engineers 5 weeks.
- **The full system cost ~£240/month** (£60 for VPS + £180 for Claude Code subscriptions to handle 20 instances).
- **Fable (Claude's most powerful model at the time) was blocked for non-US citizens two weeks after Dave used it to build his desktop app overnight.** This underscores the fragility of depending on frontier cloud models and the argument for open, locally-run software.
- **Proof of impact is the final unsolved layer.** Dave admitted he had no analytics on Dex — didn't know who his users were or whether they kept using it — until he integrated Pendo's new Novous.ai product, which auto-instruments a codebase and infers funnels, segments, and onboarding steps without manual tagging.
- **Novous.ai's UX agent caught knock-on bugs.** When building in isolation with AI, a feature can work perfectly on its own while silently breaking core navigation elsewhere. An agent with full codebase context can catch these cross-feature failures.

## Use cases
- **Product managers** who want to scan the competitive landscape faster than their org's formal research cycles allow.
- **Solo builders and indie hackers** using AI to build and ship software without an engineering team — especially around workflow design and open-source leverage.
- **Product leaders in SaaS companies** evaluating how to restructure team workflows and tooling around AI agents rather than treating AI as a bolt-on.
- **Founders with limited runway** who need to compress build cycles and validate faster before spending on engineers.
- **Anyone building internal tools** who is frustrated that existing tools (Jira, Linear) weren't designed for AI-assisted, high-velocity development.
- **PMs responsible for competitive intelligence** who want a systematic, automated approach to market signal detection.
- **Enterprise product teams** evaluating AI-native analytics platforms that can keep pace with AI-assisted development velocity.
- **Leaders facing AI adoption stagnation** — teams that have licenses but no framework for actually changing how work gets done.

## Patterns & frameworks

**1. The Three Moves / Three Pillars**
Dave's overarching framework for competing in the AI era:
- *Out Hunt* — spot market signals before competitors using automated scanning (GitHub Trending, newsletters, open-source repos).
- *Bend the System* — redesign your workflows and tools around AI; don't just use AI inside old processes.
- *Prove Impact* — when building is cheap, the hard question shifts to whether it's worth building at all; instrument and validate ruthlessly.

**2. Truffle Hunting (Market Signal Scanning)**
A metaphor and process: instead of reading newsletters manually, build or use an agent that nightly scrapes GitHub Trending and other sources, filters by relevance to your ICP, rates findings, explains them in plain English, and surfaces actionable ideas. The key shift is from reactive reading to systematic, automated pattern-matching at scale.

**3. Compound Engineering Applied to Knowledge Work**
Borrowed from Karpathy's framing: AI in the loop learns from mistakes and never repeats them, compounding in effectiveness. Dave extended this to personal knowledge work — connecting AI to personal files (goals, CRM data, calendar, Slack) so it continuously improves its prioritization and accountability over time.

**4. The Factory / AI-Triggered Kanban**
A personal operating model where a Kanban board's columns each trigger a different AI skill set. Cards move through stages (idea → 10X challenge → PRD → build) with agents assigned distinct roles (VP of Product, Staff PM, Designer, Tech Lead) and rules ("truths about where the market is going") that govern all agent decisions. Work fans out to up to 20 parallel Claude Code instances.

**5. Rules as Truths / Future-Oriented Agent Constraints**
Instead of planning for today's market, Dave encodes his beliefs about where the market will be in 12 months as explicit rules that govern every agent's judgment. Example rule: "The cost of intelligence is dropping to zero — don't penalize token-expensive ideas today." This makes the system ask "does it fit the world we think is coming?" rather than "can we build it?"

**6. The Shipping Container Analogy (from the book *Reshuffle*)**
Framing AI not as a faster horse (productivity tool) but as a shipping container — a coordination-layer innovation that enables entirely new second-order business models. The book by Sanji Paul Chowdhery argues that AI, like the shipping container in 1960s Singapore, restructures how work gets coordinated rather than just making existing work faster.

**7. Malleable Software**
The talk's central concept: software that conforms to how you work, rather than forcing you to adapt to the software's design. When tools don't fit, you build your own. The practice is enabled by AI lowering the cost of custom tool creation to near zero, making bespoke workflows accessible to non-engineers.