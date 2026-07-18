# Thinking Machines Lab drops Inkling & Meta’s Muse Spark 1.1

Video ID: `8rGYGFmytQs`

## Summary
This episode of *Mixture of Experts* covers four AI news stories: the launch of Thinking Machines Lab's first model "Inkling," Meta's Muse Spark 1.1 release, OpenAI's GPT 5.6 Soul performance on the ARC AGI 3 benchmark, and an Anthropic paper on internal model representations dubbed "JS space." The panel of IBM engineers debates what these releases signal about the direction of AI competition, the AGI timeline, and model interpretability.

## Key insights
- **Inkling (Thinking Machines Lab)** is a 975B parameter mixture-of-experts model (41B active) that is open-weight and natively multimodal — processing inputs down to the token level rather than bolting together separate vision/audio encoders.
- **The competitive pitch for Inkling is not benchmark supremacy** but a closed-loop fine-tuning platform ("Tinker") that lets the model generate its own synthetic data, run post-training, and reload weights automatically — reframing the question as "best open base + fine-tuning" vs. closed models.
- **Thinking Machines' early emphasis on determinism and reproducibility** (which seemed boring at launch) is now seen as the foundation that enables controlled architectural experimentation and rapid iteration toward frontier performance.
- **Meta's Muse Spark 1.1** targets agent workloads — parallel sub-agents, million-token context with active compaction, computer use, and low cost — positioning Meta as the economical choice for enterprise agent infrastructure rather than the smartest model.
- **Panel skepticism on Muse Spark**: the use of hedging language like "competitive with leading alternatives" was read as a tell that it does not actually beat top frontier models; the closed-weight release was seen as a missed opportunity compared to what an open-weight drop would have generated.
- **ARC AGI 3**: GPT 5.6 Soul jumped from ~0% to 8%, which is notable given benchmark difficulty, but the panel views it as a sign of shrinking distance to AGI rather than arrival — and flags the $19,000 inference cost per task as an unsustainable architectural problem.
- **The AGI definition problem**: the benchmark keeps getting harder each time models approach saturation, raising the question of whether frontier models are already "infant AGI" — the panel consensus is no, because a 12-year-old scores 100% on tasks these models score 8% on.
- **Anthropic's JS-space paper** introduces a Jacobian-based technique to read internal model representations before they project into output tokens — essentially an fMRI for LLMs — with practical implications for detecting hallucinations, deceptive reasoning, and jailbreaks.
- **The consciousness framing in the Anthropic paper was seen as deliberate hype**, but external replication by Google DeepMind's interpretability team (Neel Nanda) on open-source models lends it credibility; the practical value is a readable, editable internal state that agent builders can use for safety and control.