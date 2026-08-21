# AI Agents vs Business Rules: Which Should Make Decisions?

Video ID: `i1ZmNUbRGD4`

## Summary
This video explains the fundamental differences between business rules engines and AI agents as decision-making tools, using a refund approval system as a running example. Business rules are deterministic and explicit, while AI agents are probabilistic and context-driven. The video argues that neither has superseded the other, and that the most effective real-world systems combine both in a hybrid architecture.

## Key insights
- **Business rules are deterministic:** They evaluate fixed boolean conditions against structured facts and always produce the same output for the same input — making them predictable, auditable, and cheap to run.
- **AI agents are probabilistic:** Built on LLMs, they sample from a probability distribution over possible responses, which means the same request can yield different outcomes on different runs.
- **Use business rules when logic can be pre-defined:** Loan eligibility, insurance pricing tiers, and refund policies with clear conditions are ideal — inputs are structured and the correct answer is already known.
- **Use AI agents when logic can't be written down in advance:** Unstructured or messy input (free text, photos), unanticipated edge cases, or decisions requiring contextual judgment (e.g., someone returning dumbbells for "being too heavy") call for an agent's generalization ability.
- **Rules engines have compliance advantages:** The triggering condition is inherently the explanation, making them audit-friendly and easy to unit test branch by branch.
- **The hybrid pattern is the practical answer:** Run the rules engine first (fast and cheap) to handle clear-cut cases; escalate only ambiguous or complex cases to an AI agent, which can also invoke tools like vision models or order history lookups.
- **Deterministic guardrails wrap the agent:** The agent's recommendation isn't necessarily final — a rules-based guardrail can route high-stakes decisions to a human-in-the-loop before a final decision is reached, keeping the agent's judgment in check.