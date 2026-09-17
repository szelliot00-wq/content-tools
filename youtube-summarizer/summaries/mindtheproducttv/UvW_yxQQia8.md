# What is AI product management, really? Jonathan Evens (AI Product Lead, Google DeepMind)

Video ID: `UvW_yxQQia8`

## Summary
Jonathan Evens, an AI Product Lead at Google DeepMind with over a decade of experience, distinguishes between three types of "AI product managers" — modeling PMs, AI feature/product PMs, and general PMs who use AI tools — arguing that conflating them muddies the field. Drawing on his work transforming Google Search with AI Overviews/AI Mode and building a civic democracy tool (Digital Citizenry) at the Evans Foundation with near-zero resources, he offers a grounded, historically-informed view of what it actually takes to ship AI products well. The conversation covers measuring success, product principles before evaluations, synthetic users, trust-building, and team structure. It is most relevant to product managers, AI practitioners, and founders navigating how to integrate AI meaningfully into products without building gimmicks.

---

## Key insights

- **Three distinct types of "AI PM" exist, and most people conflate them:**
  1. **Modeling PM** — responsible for what a model does, how to measure it, and acceptable error rates. Lives inside frontier labs (Google DeepMind, Anthropic, etc.). Requires genuine ML/technical depth. Further subdivided today: pre-training PM, post-training PM, capability-specific PM (e.g., factuality, long-context, reasoning).
  2. **AI Feature/Product PM** — uses AI as a technology in service of a product. Superpower is deep domain and vertical expertise combined with knowing how to automate/augment specific workflows with AI. This role has exploded in demand.
  3. **PM who uses AI tools** — uses LLMs for productivity (drafting, data analysis, prototyping). Jonathan's view: this is just a regular PM with a better toolkit, not a distinct role title. The term "AI-enabled PM" is, in his words, not really worth using.

- **Domain expertise is undervalued in the AI era.** For AI feature/product PMs, understanding the deep intricacies of a vertical or workflow is more important than ever — yet almost nobody is talking about this. The model may cover 80% of the capability; the last 20% is shaped by how well the PM understands the use case.

- **Product principles must come before evaluations.** "Eval is all you need" is a common refrain, but evaluations are only a translation of product principles into something teachable to the model. Without clear principles, your evals have no foundation. Jonathan cites Google Search as an example: the core tension was reconciling LLMs' tendency to hallucinate with Google's historical brand promise of trustworthy, ranked information.

- **Acceptable error rates are a core product decision.** A key modeling-PM skill that carries forward into AI product work: determining what error rate is acceptable before releasing at a given scale. Google Search used a staged rollout — starting with power users in the Search Generative Experience — partly to study and reduce hallucination rates before broader release.

- **Northstar metrics haven't fundamentally changed; proxy metrics have.** For Google Search, northstar metrics (returning users, need fulfillment, satisfaction, trust in information quality) are largely the same as pre-AI. What's changed is the entire layer of proxy metrics beneath them: side-by-side win rates vs. baseline or competitor, user ratings, behavioral signals (copying answers, following recommendations, clicking citations, thumbs up/down), and reinforcement learning from human feedback (RLHF) loops.

- **Benchmarks don't capture real-world messiness.** AI models are celebrated for beating benchmarks (e.g., math competition problems), but they often fail on the actual messy problems practitioners care about. Jonathan's example: LLMs can solve benchmark math problems but still struggle to help working mathematicians with the problems they're actually focused on. Forward-deployed engineers exist precisely because applied reality is far messier than research benchmarks.

- **Synthetic users have specific, legitimate use cases — but aren't a full replacement for real users:**
  - Cold-start scenarios (no data, no product yet)
  - Privacy-sensitive research (synthetic users have no privacy constraints)
  - Automated regression testing (catching capability degradation when the model or product changes)
  - Edge case coverage
  - Jonathan considers the PM themselves the "first real human user" — QA-ing thoroughly before handing off to even trusted testers.

- **Trust-building in AI products is an old problem in a new context.** At Planet (satellite imagery company), analysts needed to know when to trust automated building/road detection. The solution: a product card explaining capabilities, failure modes, and known gaps. Jonathan argues the same approach applies to consumer-facing AI today — factuality grounding, clear citations, UX design that signals confidence levels, and punting/redirecting on politically sensitive or unclear questions.

- **UX design is a trust lever.** Specific UX choices matter for trust: where citations are placed, which sources are shown, whether text is highlighted (higher confidence) vs. unhighlighted (signals need for verification). The experience of "can I quickly tell if I should trust this?" is a product design problem, not just a model problem.

- **Team structures are becoming a gradient, not a binary.** Jonathan rejects the idea of a single ideal team size. Solo experienced developers can go very far on some problems. More complex, research-heavy, multi-disciplinary problems (like Digital Citizenry — civic AI, policy modeling, unsolved research questions) still require multiple roles. At the Evans Foundation, the "tech and democracy lead" acts as a de facto PM with vibe-coding skills, only pulling in AI research when they hit problems they can't solve alone.

- **Engineering roles are blending with product roles.** The shift from hyperparameter-tuning ML engineers to prompt-iterating, eval-set-building practitioners means the line between engineer and PM is blurring. Engineers handle technical eval dimensions (e.g., image coherence in video); PMs handle product-sense dimensions (e.g., which movements matter to which industries). More prototyping, less hard role separation.

- **Vibe coding and rapid prototyping are emerging PM skills** — specifically for the AI feature/product PM role, not for all PMs. Also valuable: using LLMs as an embedded data scientist to bring evidence to intuition-driven product conversations faster than before.

- **The philosophical framing on AGI:** Jonathan's personal view — if you trained an AI on all human data up to 10,000 years ago, then eliminated humans, the resulting world would be less interesting than ours. Therefore, he believes true complete superintelligence that fully supersedes humanity remains an open question, not a certainty.

- **Critical thinking and adaptability** are the two skills he'd tell his children to develop — skills he believes will persist regardless of how AI advances.

---

## Use cases

- **PMs deciding whether to pursue an "AI feature"** — use the modeling PM vs. AI feature PM distinction to identify which role and which skills are actually relevant to their work.
- **Hiring managers defining AI PM job descriptions** — the three-type framework helps scope roles accurately rather than using "AI PM" as a catch-all.
- **PMs at large companies rolling out LLM-powered features** — the product principles → evaluations → proxy metrics pipeline applies directly.
- **Founders and PMs at resource-constrained startups** — the Evans Foundation case study shows what's achievable with one part-time technical lead and cloud tools, plus targeted AI research help.
- **PMs building consumer-facing AI products who need to manage trust** — the product card / citation UX / grounding approach provides a concrete model.
- **AI researchers or engineers transitioning into product roles** — the distinction between benchmark performance and real-world messiness is a key mindset shift.
- **PMs in regulated or sensitive verticals (health, legal, civic tech, finance)** — the synthetic users framework for privacy-constrained research is directly applicable.
- **Teams setting up evaluation frameworks** — the principle that product principles must precede and ground evaluations is immediately actionable.
- **Product teams working on search, information retrieval, or Q&A products** — the Google Search hallucination/trustworthiness tension and its resolution (staged rollout, grounding, error rate thresholds) is a direct model.

---

## Patterns & frameworks

**1. The Three-Type AI PM Taxonomy**
A mental model for categorizing AI product roles:
- Type 1 (Modeling PM): owns model capability definition, measurement, and acceptable error rates. Requires ML depth. Lives at frontier labs.
- Type 2 (AI Feature/Product PM): uses AI in service of a product. Requires deep vertical/domain expertise + ability to map workflows to AI capabilities.
- Type 3 (AI-enabled PM): standard PM using AI tools for productivity. Not a distinct role category.
*How to apply:* Use when scoping a role, evaluating your own positioning, or hiring. Don't let the label "AI PM" collapse all three.

**2. Product Principles → Evaluations → Metrics Pipeline**
A sequenced approach to building AI product quality systems:
1. Define product principles (what experience are you creating? what is non-negotiable?)
2. Translate principles into evaluations (the first teachable signal for the model)
3. Build proxy metrics that operationalize those evaluations at scale
4. Layer northstar metrics on top (which tend not to change dramatically from pre-AI products)
*How to apply:* Before setting up any eval framework, write down your product principles explicitly. Evals built without this foundation will measure the wrong things.

**3. Staged Rollout by Acceptable Error Rate**
A risk-calibration pattern for launching AI features:
- Determine the error rate (e.g., hallucination rate) that is acceptable for your product's trust profile
- Start with power users / trusted testers at a higher error rate
- Study failure modes, iterate, reduce error rate, expand scale
*How to apply:* Used explicitly by Google Search (Search Generative Experience → broader AI Overviews rollout). Applicable to any AI feature with a trust-sensitive use case.

**4. Synthetic Users for Cold Start + Privacy + Regression**
A structured approach to when synthetic users add value vs. when they don't:
- Use for: cold start (no data/product yet), privacy-sensitive research, automated regression testing, edge case coverage
- Don't rely on exclusively: real user signals (behavioral, qualitative) still needed for product-market fit and RLHF
- PM as first human user: PM acts as the primary real-world QA before any real users see the product
*How to apply:* Map your research needs to one of these categories before defaulting to synthetic or defaulting to real users.

**5. The Product Card / Trust Layer Pattern**
A UX and communication pattern for managing AI trust:
- Document capability boundaries, known failure modes, and unresolved gaps (the "product card")
- Design UX signals that communicate confidence level at a glance (highlighting, citation placement, source credibility indicators)
- Redirect or punt on questions where the model cannot reliably produce trustworthy output
*How to apply:* Originated in B2B geospatial AI (Planet), now applies to consumer AI. Useful for any AI product where hallucination or error is a user-trust risk.

**6. The Makers Manifesto Principles** (referenced, not authored by Jonathan)
A set of guiding principles for ethical AI product building, including:
- Purpose over possibility (build for real problems, not because you can)
- Human accountability over full automation
*How to apply:* Use as a checklist when evaluating whether a proposed AI feature solves a genuine pain point or is a capability-driven gimmick.