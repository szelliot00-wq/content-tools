# Don't be an a**hole! - Simonetta Batteiger

Video ID: `RnXGLynKPK0`

## Summary
Simonetta Batteiger, a co-active coach and product leader, delivers a talk urging product managers to actively resist building harmful, untrustworthy tech products. Her core argument is that trust is not an optional quality feature — it is the foundational architectural requirement for any product, especially in the age of AI and agentic systems. She warns that without explicitly codifying what "good" looks like, AI agents default to average, biased, or harmful outputs (slop, hallucinations, sycophancy). The talk is most relevant to product managers, product leaders, and anyone building AI-powered or agentic product experiences.

## Key insights
- The tech industry has introduced a wave of harmful new phenomena: "slop," hallucinations, sycophancy, enshittification, flattened diversity in AI outputs, environmental harm from data centers, and AI-linked psychosis and deaths.
- Product leaders consistently cite "positive impact in the world" as their primary source of motivation and joy — yet the products being built often contradict this.
- Trust has two dimensions (from Stephen Covey's *The Speed of Trust*): **character** (integrity and intent) and **capability** (the results you actually produce). Both must be designed in deliberately.
- The Starbucks South Korea case study: an AI-generated marketing campaign used a slogan tied to a military massacre cover-up ("Tank Day"), resulting in a 26% revenue drop in one week from credit card payments — equivalent to a ~$580 million annual mistake. No human caught it before launch.
- Without explicit context about what "good" looks like, AI agents default to the statistical average — which is slop, bias, and hallucinations.
- The eco-conscious shopper example: an agent without context buys a $3.99 sweatshop T-shirt shipped internationally; with explicit values (cotton, fair labor, small business, $99 budget), it delivers a trustworthy purchase experience.
- A radiologist example of good AI design: doctors speak their diagnosis first, and the AI only intervenes when it disagrees — preserving human skill and adding a safety layer without causing skill atrophy.
- A hiring system example from talent.com (government contract): explicitly blocking the model from seeing proxy bias signals (zip codes, commute time, resume gaps) is not a constraint — it *is* the product, because provable fairness is what enables the sale.
- Ecosia gained 40% more US users partly by preserving user choice to disable AI summaries in search — a direct win against Google's forced AI defaults.
- Agentic purchasing is emerging: agentic buyers need explicit trust signals like rate limiting, supply chain transparency, and structured data to make purchase decisions.
- The EU AI Act's foundational paper outlines trustworthiness dimensions: human autonomy, prevention of harm, fairness, and explicability — and includes concrete governance examples (pages 32+).
- "Trust over short-term gain" must be a first-class design principle, not an afterthought.
- Every step of the product lifecycle (discovery → analysis → build → scale → business) now involves agentic co-creators, and trust must be explicitly designed into each step.
- The Makers Manifesto (a collaborative project among product coaches and thought leaders) is emerging as a framework for building positive, trustworthy products.

## Use cases
- **AI product teams** deciding how much autonomy to give agentic systems in customer-facing flows (purchasing, content generation, hiring, medical imaging).
- **Product managers building marketing automation** who need human review gates to prevent culturally harmful outputs (like the Starbucks case).
- **Hiring platform builders** working with government or regulated clients who need to prove algorithmic fairness.
- **Healthcare product teams** integrating AI diagnostics, where human-first workflows with AI as a disagreement signal can prevent skill atrophy.
- **Search and discovery products** looking to differentiate by preserving user control and choice rather than forcing AI defaults.
- **Leaders making hard prioritization decisions** between short-term revenue and long-term user trust.
- **Coaches and product leaders** helping teams articulate not just what they will not do, but what they actively want to say yes to.
- **Engineering and design teams** architecting AI systems who need to think about authorization layers, identity verification, consent, fallback mechanisms, kill switches, and logging/explicability.
- **Anyone building with or for agentic systems** who needs to explicitly codify values, vision, and acceptable outcomes so agents don't default to harmful averages.

## Patterns & frameworks

**The "Yes/No" Coaching Tool**
A co-active coaching technique: when facing a difficult decision, explicitly articulate (1) what you do *not* want to stand for, and (2) what you *do* want to say yes to. Forces clarity on values before action. Applied here to product strategy: what harms am I refusing to build, and what positive impact am I designing toward?

**The Trust House Metaphor**
A layered architecture metaphor for building trustworthy products:
- *Foundation*: Character-based trust — integrity, intent, honesty, "do no harm," codified principles.
- *Ground floor*: Capability-based trust — explicit specs of what "good" looks like, measurable outcomes, reliability.
- *Upper floors*: The positive vision — the actual product value customers pay for.
Without the foundation, the whole house collapses. Without the upper floors, you've only avoided harm but built nothing of value.

**The Speed of Trust (Stephen Covey)**
Two-axis trust model: (1) Character = integrity + intent; (2) Capability = skills + results. Both dimensions must be present for trust to exist. Applied to product: your tech must be honest *and* reliably produce good outcomes.

**The Decision Stack (Martin Eriksson)**
A hierarchical product strategy model requiring explicit articulation of: Vision → Strategy → Goals → Principles. Each layer gives AI agents and human teams the context needed to make aligned decisions. Without this stack, agents fill gaps with averages.

**Trustworthy AI Design Dimensions (EU AI Act foundational paper / Akshay Core)**
A checklist framework for AI trustworthiness covering: explicability, transparency, non-bias, privacy-centeredness, human autonomy, prevention of harm, fairness, and societal benefit. Provides a concrete spec rather than vague good intentions.

**Prompt Ledger's Layered Trust Architecture**
A technical framework for building trust into every layer of the stack: authorization controls → identity verification for agents → explicit consent/context → fallback mechanisms → kill switches → explicability logging (input → process → output) → operational controls → defined trust outcomes.

**Human-First AI Workflow Pattern (radiologist example)**
Design pattern: require humans to form and commit to a judgment *before* AI input is revealed, with AI only surfacing when it disagrees. Preserves human skill, adds safety, avoids over-reliance and skill atrophy.

**Trust as a Core Feature (not a constraint)**
Reframe: design limitations that prevent bias or harm (e.g., blocking proxy variables in hiring) are not restrictions on the product — they *are* the product differentiator and the commercial enabler.