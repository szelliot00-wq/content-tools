# Why AI Models Pause to Think: Test Time Compute Explained

Video ID: `DAlC8mL5ZlI`

## Summary
This video explains "test time compute" — the practice of allocating a compute budget to AI models at inference time rather than only at training time. It covers three core mechanisms (chain of thought, tree search, and self-consistency) that allow models to reason more carefully before committing to an answer. The video also addresses trade-offs like latency, cost, and overthinking, and explains how modern systems adaptively route queries based on complexity.

## Key insights
- **Train time compute is a fixed cost (CAPEX); test time compute is a variable cost (OPEX).** Training freezes model weights once, but inference compute is paid per query and can be scaled up or down.
- **Standard LLM inference is a one-way street.** Token-by-token greedy decoding means early tokens lock in a direction — there's no backtracking, which is a root cause of confident hallucinations.
- **Thinking tokens act as a scratchpad.** Reasoning models (trained via RL) generate intermediate tokens to explore and revise before committing to a final answer, unlike standard models that commit from the first output token.
- **Three mechanisms power test time compute:** chain of thought (step-by-step reasoning), tree search (branching paths scored by a verifier), and self-consistency (running N independent chains and majority-voting the answer).
- **Test time compute has its own scaling law.** A 3B-parameter model using inference-time search can outperform a 70B-parameter model on hard math — more than 20x smaller, just by "thinking longer."
- **Overthinking is a real failure mode.** Forcing a reasoning model to deliberate on simple questions can actually hurt accuracy, analogous to second-guessing yourself out of a correct exam answer.
- **Adaptive routing is the practical solution.** Systems like ChatGPT use a picker to route easy queries to fast single-pass inference and hard queries to full reasoning pipelines, balancing cost, latency, and accuracy.