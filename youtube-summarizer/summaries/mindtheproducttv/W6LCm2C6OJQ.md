# How to escape the feature factory: Francois Lopitaux (SVP Product Management, ThoughtSpot)

Video ID: `W6LCm2C6OJQ`

## Summary
Francois Lopitaux, SVP of Product Management at ThoughtSpot, discusses how the shift to AI-native product development is reshaping the entire product lifecycle — from prototyping and evaluation to go-to-market, team structure, and post-launch maintenance. He argues that while AI dramatically accelerates execution speed (2–3x faster development), it introduces probabilistic complexity that demands *more* organizational discipline, not less. The conversation is most relevant to product managers, engineering leaders, and product organizations navigating the transition from deterministic software to AI-powered, agentic products.

## Key insights
- **AI compresses the first 80%, not the second.** Prototyping and hypothesis validation are dramatically faster, but productionization — strong architecture, trust, reliability — still requires the same rigor. Skipping it is "a recipe for disaster."
- **Speed creates chaos without discipline.** Because everyone can now generate code and prototypes, organizations need stricter gates on what ships. The analogy used: driving a Formula 1 car on a public road — you need new controls, not the same ones from the slower era.
- **The new PRD is an eval system.** Because you can't control a chat/prompt-based UI the way you control deterministic flows, your evaluation criteria *become* the specification. Good evals define what "good" means, what to avoid, and what accuracy looks like.
- **Determinism vs. probabilism is the core tension.** Analytics must be deterministic (the same question always returns the same answer), but LLMs are inherently probabilistic. ThoughtSpot's solution is a semantic/context layer that grounds LLM outputs in company-specific definitions (e.g., "what is a new customer?" "what counts as revenue?").
- **Post-launch is now a permanent workstream.** Features are never "done." Model drift, unexpected user behavior, and LLM updates mean teams must continuously monitor, observe, and adapt — not just fix bugs.
- **The eval system is a living quality gate.** ThoughtSpot runs benchmarks (like BIRD and Spider) every time they change a model or add a feature, tracking accuracy, consistency, and relevance of answers.
- **Feature pruning is more critical than ever.** Because generation is cheap, the temptation to accumulate features is higher. Francois explicitly described himself as "a freak about killing stuff" — pruning prevents the codebase from becoming an unmaintainable blob.
- **Teams are organized by product track, not feature.** Each track owns a product end-to-end — past features and upcoming ones — creating natural continuity and customer relationship ownership rather than a feature-factory handoff model.
- **Team sizes will shrink; PM-to-dev ratios will shift.** As coding bottlenecks dissolve, the scarce resource becomes knowing *what* to build. The "two pizza team" is becoming obsolete; execution capacity now outpaces strategic clarity.
- **Flexibility in model selection is the 2026–2027 priority.** With cost optimization becoming the dominant concern (after 2025's "prove AI works" phase), teams need to be able to swap models (e.g., from a frontier LLM to an open-weight model like DeepSeek for classification tasks) without architectural lock-in.
- **The LLM as new intern analogy.** An LLM without business context is like a brilliant intern who doesn't know your company's definitions. Feed it the right context and ontology, and it becomes trustworthy and consistent.
- **B2B2C trust is compounded.** ThoughtSpot powers embedded analytics for enterprise customers who ship it to *their* customers — meaning a trust failure cascades through two brands, raising the stakes for accuracy and reliability significantly.
- **Hiring now requires a GitHub repo.** For new PM hires, Francois requires candidates to submit a Git repo of something they built *and* a video explaining what problem it solves — testing technical ability, communication, and problem-solving orientation simultaneously.
- **Opt-in feature rollout for OEM/white-label customers.** Because embedded customers control their own release cadence, new capabilities should be opt-in by default, not pushed broadly — respecting the downstream customer's ability to train and adopt.

## Use cases
- **Product managers building AI/LLM-powered products** who need a framework for replacing the traditional PRD with an eval-driven specification process.
- **Engineering and product leaders worried about moving too fast** — this provides a concrete argument for why discipline and architecture standards become *more* important, not less, as AI accelerates development.
- **Analytics or data product teams** dealing with the determinism vs. probabilism tension — where answers must be consistent but the underlying model is generative.
- **B2B SaaS companies with embedded or OEM products** navigating how to ship features to customers who then ship to *their* customers — managing rollout control, branding flexibility, and trust.
- **Product org designers** evaluating how to restructure teams — whether to organize by feature, stack, or outcome — and how to handle post-launch ownership as products require ongoing AI maintenance.
- **Hiring managers recruiting PMs** looking for a modern signal of PM readiness beyond traditional interview formats.
- **Any team choosing between LLM providers or model tiers** and needing justification for building model-agnostic architecture to enable cost optimization.
- **Product managers considering feature sunsetting** — especially relevant as AI-generated code lowers the barrier to shipping and increases the risk of feature sprawl.

## Patterns & frameworks

**The Eval-as-PRD Framework**
Instead of writing a traditional requirements document, you define success through an evaluation system: what does a correct answer look like, what behaviors are unacceptable, and what benchmarks (e.g., BIRD, Spider for SQL analytics) can you run against every change. The eval *is* the spec. Used every time a new model ships, a feature changes, or a new LLM is adopted.

**The Semantic/Context Layer (Trust Architecture)**
A structured ontology of business definitions — what counts as a "new customer," how "revenue" is defined — baked into the system before queries reach the LLM. This grounds probabilistic outputs in deterministic business logic, ensuring consistency across users and building the trust required for enterprise adoption. Analogized as giving your "new intern" the company handbook.

**Track-Based Product Organization**
Teams own a *product track* (an end-to-end product area) rather than a feature set or a technical stack. This creates continuity: the team discusses last month's shipped feature and next month's upcoming one in the same customer conversation. It prevents the feature-factory antipattern where teams ship and abandon, and makes post-launch monitoring a natural part of the workflow rather than a separate cost.

**Two-Tier Success Measurement**
1. *Customer-side*: adoption, return usage, qualitative interviews — is the product delivering value?
2. *System-side*: sampled, anonymized monitoring of answer quality, relevance, and follow-up question rates — is the product drifting or degrading?
These run in parallel as a continuous early warning system rather than as a point-in-time launch evaluation.

**Flexibility-First Model Architecture**
Build your AI product to be model-agnostic: abstract the LLM layer so you can swap providers (frontier → open-weight → specialized models like DeepSeek for classification) as cost/performance tradeoffs shift. Framed as the key competitive posture for 2026–2027's cost-optimization phase, after 2025's "prove the value" phase.

**Pruning Discipline ("The Tree Model")**
Treat a product like a tree: branches need to be cut deliberately so the tree grows in the right direction. With AI lowering the cost of building, the discipline of *removing* features becomes the counterbalancing force. Applied at version milestones (v1 → v2 → v3 of a capability) rather than waiting for the product to become unmanageable.