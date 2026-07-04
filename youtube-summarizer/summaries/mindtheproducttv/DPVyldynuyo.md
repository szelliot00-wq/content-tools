# How Figma and Anthropic are accelerating product teams | Now Shipping

Video ID: `DPVyldynuyo`

## Summary
"Now Shipping" is a weekly AI news show for product managers hosted by Mike Belceto of Mind the Product. This episode covers three major developments: Figma's Config announcements that blur the line between design and code, Anthropic's release of Claude Sonnet 5 as the new default model with near-flagship performance at significantly lower cost, and converging AI regulation from the EU and US state governments. The episode is most relevant to product managers, designers, and engineering leaders who build digital products and need to stay current on tooling shifts and compliance obligations.

## Key insights

- **Figma Code Layers**: Figma announced "Code Layers" at their annual Config conference, which brings live, executable code directly onto the Figma canvas. Teams can clone a repository and run it alongside design layers — designers and engineers now share a single canvas simultaneously, targeting the long-standing design-to-dev handoff problem.
- **Figma AI Skills**: Figma also announced "AI Skills," which let teams encode their own workflows, conventions, and processes into reusable agent instructions. These skills can connect to external tools like Notion, GitHub, Slack, and Atlassian products, giving the agent context about what the team is working on. Belceto frames this as Figma becoming an agent platform.
- **Figma's strategic motive**: Code Layers may be as much about Figma's survival as it is about team productivity. If AI coding agents can generate components without opening Figma, Figma risks being bypassed entirely. Keeping engineers inside the canvas is a defensive product move.
- **Sonnet 5 pricing vs. Opus 4.8**: Opus 4.8 cost $5/M input tokens and $25/M output tokens. Sonnet 5 launches at $2/M input and $10/M output (introductory pricing through August 31, 2026), stepping up to $3/$15 after that — still less than half the Opus price.
- **Sonnet 5 capability**: Sonnet 5 performs close to Opus 4.8 on most tasks, meaning teams are not trading down in quality to access the lower price point. Belceto argues this changes the calculus for teams that previously had to "flex down" to cheaper models at scale.
- **Adaptive thinking on by default**: Sonnet 5 ships with adaptive thinking enabled by default, allowing the model to work through multi-step problems end-to-end using tools, rather than stalling halfway through a task. Zapier's engineering team validated this, noting a two-part job that previously stalled now completes.
- **Agentic feature re-evaluation**: Teams that shelved agentic features because Opus pricing made cost-per-task unworkable should revisit those decisions. Sonnet 5 may make previously uneconomical features viable.
- **Introductory pricing caveat**: The $2/$10 pricing is not permanent. After August 31, 2026, it moves to $3/$15. Teams building product margins around AI call costs should not lock in assumptions based on the launch price.
- **EU AI Act simplification package**: The Council of the EU gave final approval on June 29, 2026 (Parliament approved June 16). The key update is a delay: the toughest requirements for high-risk AI systems — covering hiring, credit scoring, performance evaluation, and healthcare — were pushed from August 2026 to December 2027 because technical compliance standards aren't ready. Transparency rules (chatbot disclosures, labeling AI-generated content) still take effect in August 2026.
- **Connecticut CART Act**: Connecticut signed the Connecticut Artificial Intelligence Responsibility and Transparency Act, requiring employers to disclose when AI is used in hiring, performance reviews, promotions, and terminations. Critically, the law explicitly states that AI use is not a defense against employment discrimination claims — closing the "the algorithm did it" argument. The anti-discrimination provision takes effect October 1, 2026; full employer disclosure obligations kick in October 1, 2027.
- **Historical bias context**: Amazon famously scrapped a recruiting tool that penalized resumes containing the word "women's." Credit scoring and healthcare AI have also shown documented racial bias. These cases are the regulatory backdrop motivating both EU and US laws.
- **US state regulation trend**: Colorado (2024), Illinois, and Connecticut have all passed AI hiring rules. California is moving, and the federal government has signaled interest in a national standard. Belceto predicts more states will follow.

## Use cases

- **Product managers at companies using Figma** who want to reduce sprint friction between design and engineering by adopting Code Layers.
- **Design leads** looking to codify their team's conventions once so they don't have to re-explain them to every new tool — Figma AI Skills is designed for this.
- **Engineering managers and PMs** evaluating whether to switch from Opus 4.8 to Sonnet 5 to reduce AI infrastructure costs without meaningful capability loss.
- **Teams that previously killed agentic features** due to Opus-level cost-per-call — the Sonnet 5 economics may make those features viable again.
- **Product teams experiencing incomplete AI outputs** (users starting multi-step flows that stall) — adaptive thinking on by default in Sonnet 5 may resolve this without code changes.
- **Product and legal teams at companies using AI in hiring, HR, or performance management** in Connecticut, the EU, or any regulated market — compliance deadlines are now on the calendar.
- **Founders and PMs building HR tech, recruiting tools, credit scoring, or healthcare AI** who need to design compliance instrumentation (logging, decision documentation, bias auditing) into their architecture now.
- **Any team operating in the EU** that needs to understand which AI obligations are still on schedule (transparency/labeling in August 2026) vs. delayed (high-risk system documentation to December 2027).

## Patterns & frameworks

**The "translate gap" problem in design-to-dev handoff**
The recurring friction pattern where designers produce specs in one tool and engineers rebuild them in another, leading to mismatches, clarifying questions, and production inconsistencies. Figma Code Layers directly attacks this by collapsing both into a single canvas. The framework implied: reducing translation layers between disciplines reduces rework and speeds delivery.

**Encode-once, run-everywhere (Figma AI Skills)**
Rather than re-explaining team conventions to every new tool, you define your process once as an agent skill, and the tool executes it on demand with full context from connected systems (GitHub, Notion, Slack). The implicit framework: treat team process as a reusable artifact, not tribal knowledge re-explained at every onboarding or tool adoption.

**Cost-ceiling analysis for AI feature viability**
Belceto repeatedly uses the framing of "does the cost per call pencil out?" as the decision gate for whether to build or ship an agentic feature. The pattern: (1) identify desired feature, (2) estimate call volume at scale, (3) multiply by model price, (4) compare to product margins, (5) decide go/no-go. Sonnet 5's pricing changes the outcome of this analysis for many teams that previously said no.

**Capability-to-cost ratio as model selection signal**
The framework for evaluating model upgrades: don't ask "is this cheaper?" — ask "am I getting similar capability at a lower price?" A cheaper model with worse output is a tradeoff; near-equivalent output at lower cost is a structural improvement. Sonnet 5 is framed as the latter relative to Opus 4.8.

**Compliance as product architecture, not just legal review**
Belceto's closing argument frames AI regulation not as a legal department problem but as a product design constraint. The pattern: teams that build logging, decision documentation, and bias auditing into their systems now will be positioned for compliance; teams that defer will face expensive retrofits. The implication is that compliance requirements should inform data models, audit trails, and disclosure flows at the architecture stage.