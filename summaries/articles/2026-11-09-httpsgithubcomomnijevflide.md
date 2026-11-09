# Show HN: Flide: Make Jev-like decision models up to 9.5x faster

Source: https://github.com/OmniJev/Flide

## Summary
Flide is an open-source inference engine for Jev-style decision models that uses "exact state forking" to answer multiple questions about a shared context in a single forward pass. It achieves up to 9.5x faster latency than vLLM and SGLang by computing the shared state once and forking it per question, while guaranteeing each answer is identical to what the model would give if asked that question alone. It serves a `/v1/systemone` API and supports over 30 models including multimodal ones.

## Key takeaways
- **Exact state forking** is the core innovation: one shared context state is computed once and forked per question, eliminating redundant computation when multiple questions share the same context.
- **Up to 9.5x faster** than vLLM and SGLang on certain workloads (e.g., Senova on MultiRC hits 28.1×); speedups vary significantly by model and workload type.
- **Drop-in API** via `/v1/systemone` supports structured decision types like `choice` (pick from labeled options) and `noul` (yes/no urgency signals).
- **Broad model support** covers 30+ models from multiple providers (Perplexity, Qwen, Gemma, etc.), with text, image, and video inputs depending on the model.
- **Session caching** (`--session-cache-gb`) lets agents reuse earlier request states, so only new tokens need processing on follow-up steps.
- **Deterministic outputs** — `--batch-invariant` flag ensures a request gets identical results regardless of what it's batched with, at some speed cost.
- Licensed Apache-2.0 with an accompanying arXiv paper (arXiv:2610.42148).