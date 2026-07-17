# Why Risk Should Determine Your AI Architecture

Video ID: `3G6AVkp4Rf0`

## Summary
The video argues that most teams build AI systems backwards — starting with what's easy or fast, then bolting on governance later. The speaker contends that risk level should be the primary driver of AI architecture decisions, not budget or urgency. Using a data-to-wisdom hierarchy and tiered explainability examples, she demonstrates that principles like "fairness" and "transparency" are useless without being operationalized into concrete, risk-calibrated requirements.

## Key insights
- **Easy to build ≠ appropriately built.** The proliferation of AI tools makes bad AI easy; risk-appropriate AI requires deliberate architectural choices made before deployment, not after.
- **Data is not information, information is not knowledge.** Most AI systems operate at the pattern-recognition (data) level while pretending to operate at the knowledge level — missing context and relationships that explain the *why* behind a result.
- **Governance failures are architecture failures.** When a system can't provide an explanation or be audited, that's not a model problem — it's a design problem caused by building first and asking about oversight second.
- **Principles must be operationalized.** "Fairness" and "explainability" on a website are statements of intent. They must be translated into specific functional and non-functional requirements before they can be built, contracted, or audited.
- **Explainability is tiered by risk.** Baseline (low stakes, e.g. Netflix) → Enhanced (shows sources but not reasoning) → Vigilant (full data lineage, traceability, reliability testing — required for clinical or public safety decisions). The tier you need is determined entirely by the stakes.
- **Risk determines the entire delivery stack.** The risk level assigned to a system dictates the architecture, the team skills needed to build it, and the skills needed to govern it — not the other way around.
- **The right question isn't "can we build it?" but "can we defend it six months later?"** High-stakes use cases (clinical decisions, benefits determinations, public safety) require systems that are traceable, contestable, and defensible by design.