# Knowing When Not to Use AI: AI Agents vs Rules vs ML

Video ID: `_ZqSFVi6UDY`

## Summary
The video argues that AI should not be used indiscriminately, framing software problem-solving as a choice between four distinct systems: humans, rules/code, machine learning, and generative AI. Each system has specific strengths, trade-offs, and ideal use cases, and the most effective solutions deliberately match the right system to the right problem. The central thesis is that the most important AI skill is knowing when *not* to use it.

## Key insights
- **Four distinct systems, not a hierarchy:** Humans, rules-based code, ML, and generative AI are parallel options — not a progression. Treating them as a ladder leads to over-engineering.
- **Humans excel at judgment, not scale:** High-stakes, ambiguous, or accountability-heavy decisions (hiring, medical, legal) need humans. But humans can't review millions of credit card transactions per second.
- **Rules/code wins on determinism:** Payment processing, input validation, and access control demand exactness and speed. Introducing AI here adds unnecessary risk and complexity for zero benefit.
- **ML is for pattern recognition in structured data:** When rules become too complex or conditions shift (e.g., fraud detection, demand forecasting), ML handles evolving patterns better than static logic — but requires ongoing monitoring for model drift.
- **Generative AI suits unstructured, flexible, reasoning tasks:** LLMs shine at document Q&A, summarization, and multi-step workflows, but non-determinism makes them unsuitable where correctness must be guaranteed every time.
- **Tolerance for non-determinism is the key decision variable:** Before using an LLM, ask how much error or variation is acceptable. If the answer is "none," reach for code or ML instead.
- **Hybrid systems are the norm in production:** The best agents combine all four approaches — e.g., use a calculator tool for arithmetic, ML for trend detection, and an LLM only for generating the final natural-language report.
- **Most production failures stem from choosing the wrong system, not a bad model.** Architectural fit matters more than model quality.