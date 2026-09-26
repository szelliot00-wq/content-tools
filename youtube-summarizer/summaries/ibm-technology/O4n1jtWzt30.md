# New frontier AI models, TypeSafe’s Jev AI, & NASA’s IBM collab

Video ID: `O4n1jtWzt30`

## Summary
This episode of IBM's "Mixture of Experts" podcast covers three main topics: the wave of efficiency-focused frontier AI model releases (including Claude Opus 5.5 and GPT-6 Sol), TypeSafe's Jev "system one" model for structured decision-making, and an IBM-NASA collaboration producing computer vision models for lunar surface analysis. The panel — Tim Hwang, David Zax, Kaoutar El Maghraoui, Gabe Goodhart, and Martin Keen — examines the shift in AI competition from raw model intelligence toward system-level efficiency and cost reduction. The episode also serves as a farewell for host Tim Hwang.

## Key insights
- **The AI race has shifted from capability to efficiency.** New frontier models (Claude Opus 5.5, GPT-6 Sol) are being praised not for breakthrough intelligence but for delivering comparable results at dramatically lower token costs.
- **Compute cost opacity remains a major concern.** Panelists note that while consumer-facing prices are falling, it's unclear whether the underlying inference costs have actually dropped or whether VC subsidies are masking a future pricing reckoning.
- **Competition is moving from model intelligence to system intelligence.** Models are increasingly just one component inside larger agentic systems with memory, tools, and code execution — optimizing the full system matters more than benchmark scores.
- **Jev introduces a "system one" paradigm.** Rather than generating verbose token-by-token prose, Jev outputs structured, typed decisions (probabilities, classifications) directly — better matched to how software actually consumes AI outputs and far more hardware-efficient due to reduced sequential decoding.
- **Calibration is Jev's core differentiator.** The model is trained via reinforcement learning for calibrated decisions, meaning its confidence scores are designed to reliably reflect actual accuracy — critical for enterprise automation where overconfident wrong answers are dangerous.
- **Jev benchmarks well against frontier models on decision tasks**, matching top LLMs on navigation problems (e.g., the Wikipedia click game) but in subsecond time vs. multiple seconds for chain-of-thought models — though real-world ground-truth testing is still limited.
- **Hardware and software are converging around efficiency.** Techniques like quantization, KV cache management, speculative decoding, and specialized accelerators are no longer post-hoc optimizations — they increasingly determine whether a model is deployable at all.
- **The IBM-NASA lunar model demonstrates AI's breadth beyond chatbots.** Foundation models can be adapted to scientific domains (crater counting, ice detection) using multimodal representations, enabling faster scientific discovery by reusing pre-trained representations rather than starting from scratch.
- **Crater counting has real scientific value.** Crater density on the moon acts as a clock for estimating the age of the solar system and Mars — AI acceleration of this analysis has genuine cosmological significance.
- **Foundation models are modality-agnostic.** As long as data can be represented as vectors, the same mathematical foundations that power text models can be applied to satellite imagery, scientific sensor data, and other non-text domains.