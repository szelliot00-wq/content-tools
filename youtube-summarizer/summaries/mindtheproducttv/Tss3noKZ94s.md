# How Fin builds at the edges when agents own the middle: John Moriarty (Fin)

Video ID: `Tss3noKZ94s`

## Summary
John Moriarty, Director of Design at Fin (formerly Intercom), recounts how the company went all-in on AI-assisted development over the past year, tripling R&D productivity and shipping nine major product launches in two months. His core argument is that when AI agents "own the middle" of the build process (execution), human roles must shift to the edges — upstream into strategy and problem framing, and downstream into quality, standards, and judgment. The talk is most relevant to product managers, designers, and engineering leaders navigating how AI changes not just how teams work, but what products themselves fundamentally are.

## Key insights
- **Productivity tripled in one year.** Fin set a goal to double R&D productivity; they ended up tripling it (measured by PRs per person per month across design, research, engineering, and PM).
- **94% of PRs are authored by Claude Code; 19% are auto-approved** with no human reviewer in the loop — metrics that were already two months old at time of delivery.
- **Result: 9 major product launches in 2 months**, shipping 39% faster with twice the number of product changes.
- **Progress was flat for the first few months**, then December 2024 model improvements caused a sharp inflection. The lesson: adoption curves are non-linear.
- **The gap between fast and slow teams is widening weekly.** Not adopting AI at pace means moving backward, not standing still.
- **"Agents own the middle" — roles split toward the edges.** PMs move further upstream (strategy, customer conversations, roadmap ownership). Design splits — further upstream *and* further downstream (contributing directly to frontend). Engineering splits — tackling larger end-to-end projects *and* building the technical foundations.
- **Iteration cycles compress dramatically.** The same design → build → review loop still exists, but what took weeks now takes days, enabling parallel workstreams with the same headcount.
- **New bottlenecks are human, not technical:** problem framing, decision-making, quality judgment, and product coherence across a surface everyone is simultaneously contributing to.
- **Design's role shifts from gatekeeper to orchestrator.** Fin's design team is letting go of UI ownership to focus on setting standards, raising org-wide capability, and owning the "what's worth building" question.
- **Design systems become AI infrastructure.** Fin built "Surge Intelligence" — a design system that codifies taste, components, and patterns in a format Claude can consume and apply. The better the system, the better everything agents produce from it.
- **Getting to 80% quality is now instant and almost free.** The risk is no longer slow execution — it's quality degrading silently as volume accelerates.
- **A designer prototyped "Procedures"** (a product merging probabilistic and deterministic workflows in a text-based interface) end-to-end with an engineer, using real customer data, at a speed that previously would have required PRDs and weeks of discussion.
- **The UI itself is increasingly not the product.** Fin can be configured and run entirely via API/terminal. Interfaces are thinning; agents are displacing entire categories of UI.
- **"Topics Explorer" is already likely redundant.** A well-designed UI for surfacing and acting on customer conversation signals is being replaced by Operator, an agent that simply does the task when you drag in a file and ask.
- **Operator renders bespoke, generative UI on demand** — not hard-coded screens, but ad-hoc interfaces spun up for specific users and tasks. Navigation screens, settings screens, dashboards — entire product categories are collapsing.
- **Vague briefs produce vague outcomes at speed and in every direction.** Clarity of direction becomes the highest-leverage skill when agents can execute instantly.
- **"Taste can't live in your head."** If quality standards only exist in a few individuals, they won't survive the pace. Standards must be codified into foundations and guard rails.

## Use cases
- **Product leaders** deciding whether to restructure the product triad or redefine role boundaries in an AI-accelerated org.
- **Design leaders** figuring out how to stay relevant and add value when engineers and PMs can ship credible UI without them.
- **Engineering managers** thinking about how to route senior engineers toward high-leverage foundational work versus AI-handled execution.
- **PMs** who want to take on more roadmap ownership and prototype-driven discovery without waiting on design/engineering cycles.
- **Design system teams** looking to extend their systems to serve AI agents as consumers, not just human engineers.
- **Anyone auditing their product portfolio** to identify which UI surfaces and product categories are candidates for agent displacement.
- **Org leaders** making the case internally for deliberate, team-wide AI adoption investment rather than leaving it to individual initiative.
- **Teams experiencing quality degradation at speed** — the "silent 80%" problem where everything looks credible but coherence erodes.

## Patterns & frameworks

**"Agents own the middle; humans build at the edges"**
The core mental model. Execution (the middle of the product development process) is increasingly automated. Human value concentrates at the upstream edge (what to build, why, for whom) and the downstream edge (quality, judgment, coherence, standards). Roles don't disappear — they migrate.

**The Edges Split (role bifurcation)**
Each discipline in the triad splits in two directions simultaneously: PM goes further upstream *and* gains more roadmap ownership; Design goes further upstream *and* further downstream into frontend contribution; Engineering goes toward larger ambitious end-to-end projects *and* toward foundational infrastructure work. No role becomes singular — each becomes dual.

**Design systems as AI infrastructure**
Rather than design systems serving human engineers, they now serve AI agents as primary consumers. Components, patterns, and taste must be codified in machine-readable formats. Fin calls this "Surge Intelligence" — encoding design and engineering decisions so Claude can apply them consistently across the org. Higher-quality foundations produce higher-quality agent output.

**"Codifying taste" / Guard rails over gatekeeping**
Quality doesn't scale through review bandwidth — it scales through baked-in standards. Rather than relying on design or senior engineers to catch issues at review time, quality criteria are encoded as Claude skills, code review rules, and system-level guard rails. This decouples quality from headcount.

**Deliberate pauses by design**
When execution is no longer the bottleneck, the natural pauses that used to allow reflection (waiting for build to complete) disappear. Teams must explicitly design checkpoint moments into their process to ask: "Are we still solving the right problem? Is this pointing in the right direction?" These don't happen automatically — they must be engineered in.

**Five calls to action for builders (Moriarty's closing framework)**
1. *Get hands-on* — fluency is the entry point, not a nice-to-have.
2. *Make AI capability a shared org standard* — individual excellence compounds less than collective infrastructure.
3. *Obsess over direction clarity* — agents amplify the quality of briefs; vague in = vague out at speed.
4. *Codify taste into foundations* — quality must survive pace without adding review burden.
5. *Interrogate what should exist at all* — shipping is now easy; the hard question is whether a feature or product category should exist.