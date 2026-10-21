# The Problem with Jev: Can You Trust AI Decisions?

Video ID: `_yO_Q7qo0HQ`

## Summary
The video critiques a decision-making AI framework called Jev from a cybersecurity perspective, arguing that high-confidence probabilistic outputs are not the same as verifiable, explainable decisions. The presenter contrasts Jev with LLMs — which at least produce inspectable text — and warns that confidence scores can mask corrupted or manipulated inputs. The core argument is that as AI moves from generating text to taking real-world actions, observability and auditability become critical security requirements.

## Key insights
- **Confidence is not proof.** A 97% confidence score tells you how certain the model is given its inputs, not whether those inputs were accurate or trustworthy.
- **Jev is a black box by design.** Unlike LLMs where you can inspect reasoning, challenge outputs, or audit tool use, Jev produces structured decisions without an inherent explanation trail.
- **The attack surface includes the model's inputs.** An adversary who manipulates logs, metadata, training data, or upstream workflows can cause Jev to make confidently wrong decisions — with no visible indicator that anything went wrong.
- **Subtle model drift is hard to detect.** A compromised system that is only slightly biased (e.g., 1% more likely to approve a bad action) may never trigger alarms because each individual decision looks reasonable in isolation.
- **Break big questions into smaller, observable steps.** TypeSafe (the company behind Jev) recommends decomposing decisions into a chain of smaller questions — this improves auditability by letting you inspect intermediate conclusions rather than one opaque final answer.
- **Treat AI as an untrusted component.** Apply standard security controls: input validation, independent signal sources, behavioral drift monitoring, anomaly detection, and audit logging.
- **Keep humans in the loop for high-stakes decisions.** When AI actions have real consequences — blocking accounts, paying invoices, shutting down servers — independent human verification is essential.
- **Observability is the core requirement.** The right question isn't just "what did AI decide?" but "how do I know what it decided, and can I tell if someone caused it to decide wrongly?"