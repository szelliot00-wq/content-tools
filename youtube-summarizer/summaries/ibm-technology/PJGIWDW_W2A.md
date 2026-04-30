# Is open source safe? Featuring Mixture of Experts

Video ID: `PJGIWDW_W2A`

## Summary
This crossover episode between IBM's Security Intelligence and Mixture of Experts podcasts brings together AI and cybersecurity experts to explore the benefits and risks of open source in the context of AI. The panel discusses open source models versus closed frontier models, the distinction between open-source code and open model weights, and how trust, transparency, and security intersect in AI systems. The conversation also touches on emerging threats like prompt injection in agentic systems and the challenge of model interpretability.

## Key insights
- **Open source is driving AI innovation** because the gap between raw science (math, tensors) and practical utility is unusually small in AI, making open collaboration especially impactful.
- **Open source code ≠ open model weights** — these carry different security implications and should be evaluated separately when assessing risk.
- **"Security through obscurity" is not a reliable strategy** — even closed/proprietary systems can be reverse-engineered, and secrets eventually leak, so security must be designed in, not hidden.
- **The "thousand eyes" argument has limits** — while open source allows more people to find vulnerabilities, AI systems are too large and complex for community review alone to guarantee security.
- **Open weights models can have safety guardrails stripped out** — once model weights are public, bad actors can fine-tune or manipulate them to remove rejection/safety behaviors.
- **Agentic AI systems introduce a major new attack surface** — agent loops effectively act as code interpreters where any text input (including malicious web content) can trigger real-world actions, making prompt injection a critical unsolved threat.
- **Model interpretability remains a core challenge** — unlike traditional software, it's still largely impossible to fully understand how an LLM maps inputs to outputs, affecting trust for both open and closed models.
- **Open weights do allow some interpretability advantages** — researchers can probe and adjust individual weights to gain insight into model behavior, which is a benefit not available with fully closed models.
- **Frontier models are becoming more restricted** — unlike the open $20/month access of the past, some advanced models now require approval or consortium membership, widening the gap between open and closed AI.
- **Open standards like MCP and skill.md** are making open source foundational even to systems built on closed frontier models, meaning there is no escaping open source in modern AI stacks.