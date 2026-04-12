# What is AI Technical Debt? Key Risks for Machine Learning Projects

Video ID: `DgXV8QSlI4U`

## Summary
This video defines AI technical debt as the future costs incurred from present shortcuts taken to quickly deploy AI solutions, emphasizing it's growing faster than model accuracy. It explains why this debt is more problematic in the probabilistic and non-deterministic nature of AI compared to traditional deterministic software. The speaker categorizes AI technical debt into four main areas: data, model, prompt, and organizational, offering insights into its manifestations and highlighting the importance of disciplined development practices to mitigate its compounding effects.

## Key insights
- AI technical debt is "future cost from present shortcuts" and the "interest" paid for prioritizing speed over diligent upfront work in AI development, leading to future issues like bugs, refactoring, and maintenance.
- It is significantly worse in AI than traditional software due to the probabilistic, non-deterministic nature of AI systems, where small changes can have widespread, unpredictable effects ("change anything, changes everything").
- Technical debt can be strategic (consciously taken with a plan for remediation) or reckless (resulting from poor discipline, lack of documentation, and no remediation strategy).
- Key forms of AI technical debt include:
    - **Data debt:** Issues like biased, drifted, or poisoned data, and lack of anonymization leading to sensitive data leakage.
    - **Model debt:** Absence of version control, evaluation metrics, rollback capabilities, and security testing for the model itself.
    - **Prompt debt:** Undocumented system prompts, lack of input validation, prompt injection vulnerabilities, data leakage through responses, and insufficient guardrails.
    - **Organizational debt:** Unclear ownership, lack of governance policies, insufficient red teaming, and inadequate planning for latency and scalability.
- Preventing AI technical debt requires adhering to fundamental software engineering principles—starting with requirements and architecture before implementation, testing, deployment, and evaluation—rather than the "ready, fire, aim" approach prevalent in the rush to deploy AI.