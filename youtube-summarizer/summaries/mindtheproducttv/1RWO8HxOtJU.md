# Four questions to ask before building AI into your product—Kendra Vant (Chief Product Officer, Tapi

Video ID: `1RWO8HxOtJU`

## Summary
Kendra Vant, Chief Product Officer at Tappy (an Australian/New Zealand maintenance-as-a-service company), argues that the core challenge of building AI into products is not whether the model can do a task, but who or what provides the "reliability layer" — the scaffolding that catches and corrects the model's inevitable inconsistencies. Drawing on a Princeton research paper (from the "AI Snake Oil" authors) showing that LLMs have become more accurate but not more consistent, she proposes four diagnostic questions product teams should ask before committing to an AI feature. The conversation also covers the widening gap between prototyping speed and production readiness, the advantage of small companies over legacy-heavy enterprises, and how product sense and system-design thinking are becoming the hardest-to-replicate differentiators in an AI-augmented world. Most relevant to product managers, CPOs, and engineering leaders evaluating whether and how to embed generative AI into customer-facing products.

---

## Key insights

- **Accuracy vs. consistency is the key distinction.** A Princeton paper (from the "AI Snake Oil" researchers) found that LLMs have become more accurate but have not become more consistent — asked to do the same task five times, they will not give the same answer each time. This is the root cause of why AI feels magic in some products but unshippable in others.

- **Every AI product has a reliability layer — the question is who builds it.** When Kendra uses Claude for her own work, she is constantly correcting it, re-prompting, and pointing out errors. She is the reliability layer. Consumer-facing AI tools (Copilot, Cursor, Glean) are designed for highly motivated users who will do this work willingly. B2B software users — like Tappy's property managers — are not. They just want it to work, first time, every time.

- **The "can the model do this?" question is wrong.** The right question is: "Can the model do this reliably enough for my users, and can I afford to build and maintain the layer that makes it reliable?" A demo-path happy path is almost always achievable; production-grade reliability at scale is a different engineering and cost problem entirely.

- **The reliability layer is expensive and often underestimated at scale.** Teams frequently build reliability layers (evals, model-checkers, human review loops, guardrails) that work fine at demo scale but cost more than the product revenues when run at production scale. This is a common and serious planning failure.

- **Framing matters when communicating risk to non-technical stakeholders.** Saying "the model is right 85% of the time" sounds impressive. Saying "the model will be wrong 15% of the time" sounds alarming. Same number, very different reactions. Kendra recommends leading with the failure framing to force honest conversations about graceful degradation.

- **The "first 80% / second 80%" problem.** Getting from zero to prototype now takes hours to days instead of weeks to months. Getting from prototype to production-ready, scalable, reliable software still takes a very long time. The multipliers are asymmetric, and this creates a dangerous gap between what executives see in demos and what engineering can actually ship.

- **Customization as intentional reliability-layer delegation.** There are cases where letting users configure and customize a product means they become the reliability layer for their own edge cases — and in doing so, they lock themselves in because the product now works exactly the way they need it to. This is a legitimate product strategy, but it makes scaling harder and typically belongs in a tiered/enterprise pricing model.

- **Small companies have a structural advantage right now.** Without large legacy codebases or large install bases to maintain, small teams can move extraordinarily fast. Kendra notes this is "never been a better time to be a small company."

- **Legacy code debt is heavier than ever.** The gap between what's possible on a greenfield codebase with AI tools and what's possible when maintaining a large legacy system has widened. One CEO example: a large company's AI investment was mostly consumed by rewriting the existing codebase to stay current, not building new capabilities.

- **Product sense / product judgment is the hardest thing to replicate with AI tools.** Kendra describes this as the ability to recognize a path that works now but will fail later, drawn from accumulated experience with previous failures. She is genuinely uncertain how early-career product people accumulate this judgment when the tools short-circuit the slow, failure-rich learning process.

- **System design thinking is the new engineering differentiator.** AI tools can write code faster than many engineers, but they cannot do system design for a product that exists only conceptually in human minds. Understanding computer science fundamentals and software patterns — not just writing code — has become a stronger differentiator than it was 5–10 years ago.

- **Product people must be software-literate, not software engineers.** Kendra would not hire a PM who isn't comfortable with Git and able to interrogate the codebase directly. But she is careful to distinguish between "understands how software is built" and "can securely build production software" — the latter remains a deep engineering discipline that AI tools do not eliminate.

- **LLMs are getting better at saying "I don't know," but it costs money.** Running multiple models to cross-check answers is one reliability technique, but it multiplies cost 3x or more. This is a core tension for usage-based pricing products.

---

## Use cases

- **CPOs and product leaders evaluating AI feature proposals** from executives or board members who have seen a demo and assume it can be built quickly and cheaply.
- **Product managers writing specs for AI-powered features** who need to account for reliability engineering as a first-class deliverable, not an afterthought.
- **Engineering and product teams doing cost modeling** for generative AI products — particularly before committing to a build based on demo-scale performance.
- **Product teams explaining AI development timelines to non-technical stakeholders** who don't understand why the prototype wasn't the product.
- **PMs at B2B SaaS companies** where end users are professionals who expect software to "just work" and have no interest in co-creating with an imperfect AI.
- **Teams deciding whether to build AI customization features** and trying to understand when user-as-reliability-layer is a strategic asset vs. a scaling liability.
- **Founders and product leaders at small companies** who want to understand their structural advantage over larger incumbents in the current AI moment.
- **Senior product people mentoring or hiring junior PMs** who are wondering what skills are becoming more or less important in an AI-augmented world.
- **Any product person who needs to push back on AI hype** internally without being "the one who always says no."

---

## Patterns & frameworks

**The Reliability Layer Framework**
The central mental model of the talk. Every AI product has a reliability layer — someone or something that catches the model's inconsistencies and errors. The framework asks you to identify: (1) who that layer is in your product, (2) whether they are willing and able to perform that role, and (3) whether you can afford to build and sustain it at scale. Options are: the user, the engineering team (via evals/guardrails/model-checkers), or human operators in the background. If none of these are yet identified, you have a demo, not a product.

**Four Questions Before Building AI Into a Product**
A pre-build diagnostic checklist:
1. *What are users papering over when they use AI like this?* Closely observe how motivated users of analogous AI products actually behave — they are likely doing more error-correction than they realize. Will your users do the same?
2. *Who provides the reliability layer — the user, engineering, or nobody?* If the answer is nobody, you are at demo stage.
3. *When the reliability layer fails, what does it cost in customer trust?* Think about graceful degradation: will failures be tolerable or product-killing?
4. *What will it cost to maintain the reliability layer at scale?* Evals, model-checkers, and human review loops that work at demo scale often become unaffordable at production scale.

**Accuracy vs. Consistency Distinction**
A diagnostic lens borrowed from the Princeton AI Snake Oil paper. A model can improve in accuracy (getting the right answer more often) while not improving in consistency (giving the same answer when asked the same question repeatedly). Reliability engineering is largely about solving the consistency problem, not the accuracy problem.

**The 80/20 Inversion (Prototype vs. Production)**
The observation that AI has dramatically compressed the first 80% of product development (ideation → prototype → living PRD) while barely compressing the second 80% (production-readiness, scalability, reliability). This creates a dangerous perceptual gap between what non-technical stakeholders see and what shipping actually requires.

**Reframe Risk as Failure Rate, Not Success Rate**
A communication pattern for talking to business stakeholders about probabilistic systems: always state the failure rate ("wrong 15% of the time"), not the success rate ("right 85% of the time"). Same number, but the failure framing forces honest conversation about fallback plans and cost.

**Work Backward From Failure**
A design pattern for determining whether an AI feature is viable: (1) identify how the system will go wrong, (2) design a graceful recovery path for that failure, (3) build the cost of that recovery into your model. If you cannot describe the failure mode and a recovery path, you are not yet ready to build.

**Five Whys for Problem Articulation**
Kendra's practical recommendation for improving reliability thinking: force yourself to answer "why" and "how will it go wrong" to five levels of depth before building. Write the answers down. Then explain them to a human colleague (not an AI, which will validate anything you say). The exercise reveals whether you have genuinely articulated the problem space or are still operating on a shallow prototype-level understanding.