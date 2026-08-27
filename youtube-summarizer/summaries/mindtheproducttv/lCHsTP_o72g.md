# Four mistakes scaling teams make - Julia Barham (Author and Product Executive)

Video ID: `lCHsTP_o72g`

## Summary
Julia Barham, author of *The Product Management Playbook* and a product executive at Progressive Insurance, joins the Mind the Product podcast to discuss four common anti-patterns that emerge when teams and products scale. Her core argument is captured in the mantra "don't scale chaos" — meaning that as products grow, the operating model must mature alongside them or teams will amplify existing problems rather than solve them. The conversation covers organizational ambiguity, product-market fit timing, technical debt, and portfolio thinking. The video is most relevant to product managers at scaling startups and mid-to-large enterprises, as well as product leaders building or coaching PM teams.

## Key insights
- **Don't scale chaos**: When a product starts gaining volume, teams often scale their existing dysfunction rather than updating their operating model to match the product's maturity.
- **Context breakdown at scale**: As teams grow, new members lack historical context. Artifacts (strategy docs, roadmaps, vision) must be accessible and durable — if the PM has to be in every room to answer questions, that's a scaling failure.
- **Production support needs process**: Higher volume means more bugs and support tickets. Without a bug severity rubric or SLA framework that lets anyone on the team make triage decisions, the PM becomes a bottleneck — another form of scaled chaos.
- **Data democratization breaks down**: Early teams rely on ad hoc data pulls; at scale, the absence of self-service dashboards floods inboxes and Slack and slows decision-making.
- **Product-market fit takes longer than most expect**: Many teams panic and optimize for growth immediately post-launch. In reality, achieving PMF often takes 2 years, and sometimes up to 5 — Miro and Figma both took approximately 5 years to feel confident they had reached PMF.
- **Growth before PMF creates a leaky bucket**: Investing in customer acquisition before retention is solid drives up CAC while churn erases gains. The right order is: validate retention → validate sustainable business value → then turn on growth.
- **Retention is the strongest signal of PMF**: Dan Olsen, whom Julia interviewed for the book, identifies retention as the clearest indicator — it signals a sustainable customer base.
- **Scaling expensive technical problems costs real money**: Julia spent 9 months resolving latency issues on an inherited platform, ultimately costing the company millions in revenue — a direct result of shortcuts taken at launch that were never fixed before scaling.
- **Architecture principles and non-functional requirements are a PM's responsibility**: Clear architectural guard rails and non-functional requirements (analytics, observability, performance targets) help teams avoid accumulating the kind of debt that becomes catastrophic at scale.
- **Quantify technical debt in business terms**: To avoid looking like a "stick in the mud," PMs should size technical debt with a dollar value — engineering time, contact center costs, lost revenue — turning it into a true business case rather than a technical complaint.
- **Technical debt is about timing, not avoidance**: Taking on debt can be an intentional, valid call during growth mode. The point is to make that decision consciously and know when you'll pay for it.
- **Thinking in portfolios, not backlogs**: PMs who manage only a customer feature backlog and ignore platform/technical work are not thinking holistically. A healthy product portfolio has four slices: (1) optimization, (2) innovation/strategic bets, (3) capability/platform work, and (4) production support / run-the-business work.
- **Reserve capacity for production support explicitly**: One practical tactic is holding back ~20% of team capacity by default for run-the-business work, rather than pretending it doesn't exist and then scrambling.
- **The biggest gap in product management is coaching**: Julia's core motivation for writing the book is that many PMs — especially those who entered the role during the last decade's wave of "product transformations" — never received end-to-end training, leaving them strong in delivery but weak in discovery (or vice versa).
- **AI should assist, not replace, a PM's point of view**: AI is a useful tool for synthesis and research, but PMs who outsource their thinking to AI risk being exposed in executive settings where they lack informed answers. Synthesis should still happen *with the team*, not solely through an AI tool.
- **Product management is a practice, not a title**: Many people exercise PM skills without the title, and the role is inherently wide, ambiguous, and non-deterministic in outcomes even when outputs are predictable.
- **Organizational ambiguity is the least-discussed type**: Beyond problem ambiguity, solution ambiguity, and priority ambiguity, organizational ambiguity (imperfect funding models, unclear team structures, misaligned stakeholders) is a real and persistent condition PMs must learn to navigate rather than wait to resolve.

## Use cases
- A PM who just launched a product and is feeling pressure from leadership to prioritize growth metrics over retention and engagement signals.
- A team that has achieved some traction and is scaling headcount, but finds the PM is still being pulled into every decision — a sign the operating model hasn't kept up.
- A product leader inheriting a platform with performance or quality issues who needs to make the business case for slowing down feature work to address foundational problems.
- An engineering-focused team that ships fast but lacks architectural principles or non-functional requirements, creating invisible risk as volume grows.
- A PM whose backlog is purely feature/customer work, with no explicit slots for platform improvements or run-the-business tasks.
- A junior PM trying to understand why things feel so chaotic at a scaling startup and wanting diagnostic language to name and address it.
- A product leader trying to coach and develop PMs who lack end-to-end product lifecycle exposure.
- A team transitioning from growth mode to efficiency/optimization mode and struggling to realign goals, metrics, and activities accordingly.
- Anyone joining a new team or product domain who needs a repeatable "ways of working" conversation framework to establish clarity quickly.

## Patterns & frameworks

**"Don't scale chaos" (anti-pattern checklist)**
Julia's central mantra. At the point of scaling, audit three things: (1) team context — are artifacts accessible without the PM? (2) production support — does the team have SLAs and triage rubrics so anyone can make the call? (3) customer/business intelligence — is data self-service, or is it bottlenecked through individuals?

**The four scaling mistakes (anti-pattern framework)**
Four discrete failure modes to watch for as a product scales:
1. Not planning for the day you can't be in every room (context/operating model)
2. Obsessing over growth before achieving product-market fit (retention-first sequencing)
3. Scaling expensive, unfixed problems (technical debt compounding at volume)
4. Not thinking about your in-market product as a portfolio (single-backlog tunnel vision)

**Product-market fit sniff test**
Julia includes a signal checklist in her book: indicators that you *don't* have PMF (e.g., high churn, low retention, unclear ICP) vs. indicators that you *do* (strong retention, sustainable business model signals). Dan Olsen's input: retention is the single strongest PMF indicator.

**Four ambiguities of product management**
Framing from the book to help PMs name and diagnose their situation:
1. Problem ambiguity — unclear what problem to solve
2. Solution ambiguity — unclear how to solve it
3. Priority ambiguity — unclear what to work on when everything is urgent
4. Organizational ambiguity — unclear structures, funding, roles, and operating models (the least discussed)

**Ways of working exercise (3 Ps)**
A structured team conversation — typically involving product, business, design, and data leads — covering:
- **Plan**: What is the strategy and roadmap for the next 1–2 years?
- **People**: Do we have the right roles, responsibilities, and skills? Do we need to hire?
- **Process**: How do we plan, estimate, do capacity planning, and run our software delivery lifecycle together?
Most effective when done collaboratively with all partners, not by the PM alone.

**Portfolio model for in-market products (four slices)**
A mental model for allocating team capacity across four categories rather than treating everything as a feature backlog:
1. **Optimization** — improving the existing product experience
2. **Innovation / strategic bets** — defending against disruption, exploring new directions
3. **Capability / platform work** — building internal infrastructure so the team can move faster
4. **Production support / run the business** — planned buffer (e.g., 20% capacity) for bugs, incidents, and maintenance

**Debt-as-P&L framing**
Rather than framing technical debt as a purely engineering concern, treat the product like a P&L whether or not you own one formally. Attach dollar estimates to the cost of debt (engineering time, contact center volume, lost revenue) to make it a business-level conversation and avoid being perceived as blocking progress without cause.

**Product maturity life cycle**
Referenced but not fully detailed: the idea that goals, activities, and metrics should all shift depending on whether a product is at 0-to-1, 1-to-N, at scale, or approaching sunset. Mismatches between the team's mode and the product's actual maturity stage are a common source of dysfunction.