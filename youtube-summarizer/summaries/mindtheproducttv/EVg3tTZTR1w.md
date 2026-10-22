# How to make your customers stay when anyone can copy your product | Rob Ferguson (VP, Fireworks AI)

Video ID: `EVg3tTZTR1w`

## Summary
Rob Ferguson, VP of Technology & Strategy at Fireworks AI (formerly Global Head of AI at AWS and CTO at Microsoft for Startups), discusses how product teams can build durable competitive moats in an era where features can be copied in days. The core argument is that traditional feature-based moats are nearly dead — defensibility now comes from deep customer relationships, proprietary data, and curated intelligence tailored to specific use cases. The conversation covers infrastructure economics, the shift from SaaS to "work as a service," and how the best AI-native companies approach model selection and measurement. Most relevant to product managers, founders, CTOs, and anyone building AI-powered products who needs to think about long-term differentiation.

---

## Key insights

- **Features are no longer a moat.** Jev (used as a case study) took ~2 years and significant investment to build, yet competitors reached 95–97% feature parity within days of launch. What Jev actually built as a moat was community, cookbooks, documentation, and a point of view — not the classifier itself, which Fireworks had blogged about for $11 a year earlier.

- **Rising above the noise is the real competitive challenge.** Cold email open rates have dropped from ~4% to effectively zero because AI-generated spam has flooded inboxes. Distribution and attention are now the scarce resources, not technical capability.

- **Customer relationship is the most defensible moat.** The energy required to truly know your customer, be present with them, and maintain a direct communication line is hard for competitors to replicate quickly. Spray-and-pray competitors rarely follow through.

- **Data is drastically undervalued.** AI labs (especially closed ones) actively try to discount the value of your data because they want to absorb it. Fireworks ran the math on how much discount they'd need to offer customers if they trained on their data — "it was a lot." Companies are giving away valuable proprietary data for free, improving everyone else's intelligence.

- **Your product doesn't stop at your features — it's the entire experience.** UI quality directly affects AI output quality. A screenshot of a well-designed UI used as a prompt produces better intelligence than a poorly designed one, because the AI infers validation logic, priorities, and context from layout.

- **Domain-specific vocabulary matters for AI.** Rob's example: he plays piano, where a "string" means wire, not yarn. Intelligence that understands your organization's specific language and context gets smarter over time, while generic models get worse as context grows (a "reverse person" problem).

- **The state of the art is always a mixture of models.** Oracle modeling — running every permutation of model combinations across a task set — consistently shows that no single model wins. Different models have affinities (e.g., some better at JavaScript, some at Python).

- **GPU economics are brutal and complex.** ~10,000 GPUs ≈ $1 billion. Even a small model deployment requires 80+ GPUs with replication for service quality. Idle GPU time drives up costs for everyone. This is why serverless inference infrastructure (Fireworks, OpenAI, Anthropic) exists and why self-hosting at scale is impractical for most companies.

- **Model independence > model dependence.** Most companies are "model dependent" — hoping the next frontier model release happens to work for their use case. Fireworks positions itself as the first step toward model independence: understanding trade-offs, customizing intelligence, and controlling costs. Cursor is cited as a key example — they distilled a model that ignored everything unrelated to AI coding, achieving better speed and cost per unit of intelligence for their users.

- **"Done" is the most seductive and dangerous word in product.** The hardest discipline is resisting the pull of a working prototype and asking first: "How will we know when this is actually done?" Teams that skip this conversation ship things that "kind of work" but don't deliver real customer value.

- **Prototypes have changed the quality of product conversations.** The best PMs and designers now show clickable prototypes (even if only one path works) instead of wireframes. This dramatically raises conversation quality — stakeholders can react to something real instead of imagining from a document.

- **Discovery is accelerated; reliability is still hard.** The first 80% of product development (prototyping, defining, aligning) is dramatically faster with AI. The second 80% — making it reliable, shippable, and consistently valuable — remains just as hard.

- **We've moved from SaaS to "Work as a Service."** SaaS promised to keep software updated. The new era promises to actually do the work on the other side. This requires forward-deployed teams that engage directly with customers to understand the hidden contract in the work.

- **AI amplifies both best and worst practices.** It reveals organizational "cobwebs." Teams creating lots of small local improvements that don't add up to anything coherent are falling into a common trap — spaghetti optimization without system-level thinking.

- **Measurement is the great secret to AI improvement.** Reinforcement learning found 4–6% additional video compression gains that PhD researchers had exhausted — purely because compression is innately measurable. Any field where you can break work into small, scorable units can be improved with AI.

- **Fireworks' moat is performance depth + open optionality.** They are the team behind PyTorch, giving them deep internals knowledge. Even a tiny decimal-point error in one of a model's many layers shows up in final outputs. They combine best-in-class training and inference on one platform, with zero data retention (unless explicitly used for training, in which case the model stays yours).

---

## Use cases

- **Founders/early-stage startups** worried about fast-follow competitors copying their product — use the framework to shift focus from features to customer relationships, data assets, and community.
- **Product managers** trying to justify why they need more customer discovery time before shipping — use the "how will we know we're done?" framing to get stakeholder alignment upfront.
- **AI product teams** defaulting to a single LLM for everything — challenge this with oracle modeling and explore mixture-of-models approaches.
- **CTOs evaluating AI infrastructure** decisions (self-host vs. managed inference) — use the GPU economics breakdown to make the build-vs-buy case.
- **Companies spending $15K+/month on inference** — consider model distillation and customization (via Fireworks or similar) to break out of exponential AI cost curves.
- **Management teams setting strategy timelines** — use the forward-deploy team model and direct customer engagement as the organizing principle instead of trying to plan 3–5 years out in a market this volatile.
- **Any team with domain-specific data** — recognize that this data is a genuine asset that closed AI labs want to absorb cheaply; treat it accordingly.
- **Teams doing AI prototyping** — show prototypes to get better conversations, but set expectations before showing them and define "done" criteria in advance.

---

## Patterns & frameworks

**The Moat Hierarchy (implicit)**
Features < Experience < Customer Relationships < Proprietary Data. In the AI era, each lower layer is more defensible than the one above it. Features can be copied in days; data and relationships take years to build.

**Oracle Modeling**
Run every permutation of model combinations on a task set to empirically determine which mixture produces the best results. The answer is always a mixture — no single model dominates across all tasks. Used to identify which models have affinities for which sub-problems.

**Hunch Data vs. Deterministic Data**
A classification framework for deciding which AI techniques to apply. "Hunch data" (non-deterministic, human judgment-heavy) calls for generative/probabilistic AI approaches. "Deterministic data" (receipts, structured outputs with known correct answers) calls for strong evals and measurable pipelines.

**"Find the Seams"**
Break complex work into small, independently measurable sub-tasks. The more granularly you can measure a task, the more you can improve it with AI. Avoid treating large functions as a single atomic unit — understand what's inside the work.

**Model Independence Journey**
Stage 1: Model Dependent (hoping the next frontier model works for you). Stage 2: Model Independent (understanding trade-offs, customizing intelligence, optimizing for your specific use case and cost). Fireworks positions itself as the transition enabler between these stages.

**SaaS → Work as a Service Evolution**
Software (sell artifacts) → SaaS (promise to keep it updated) → Work (actually deliver outcomes for the customer). Each stage requires deeper engagement with the customer and more forward-deployed teams rather than design-and-ship cycles.

**Prototype-First Discovery**
Replace wireframes and written PRDs with clickable prototypes as the first artifact in a discovery conversation. This raises conversation quality, surfaces misunderstandings faster, and reveals edge cases — but must be paired with explicit "how will we know we're done?" conversations before the prototype is shown to customers.

**Build, Measure, Learn (reaffirmed)**
The core loop hasn't changed. What's changed is the speed and tooling for each step. The risk is that "measure" is the step most often skipped or done too locally, leading to uncoordinated point improvements that don't compound.