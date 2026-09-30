# PSSA: A non-transformer language model written from scratch in Rust

Source: https://github.com/Sparticle62ops/pssa

## Summary
PSSA (Plastic State-Space Architecture) is an experimental language model written from scratch in Rust that eschews the transformer architecture in favor of a recurrent state-space design with a hyperbolic episodic memory bank and on-the-fly weight updates. Trained on 12.7M tokens of WikiText-103 and matched parameter-for-parameter against a standard transformer, PSSA achieved lower cross-entropy (3.98 vs 4.43) and lower perplexity (54.4 vs 83.8) on held-out text, while generating tokens roughly 12x faster on CPU. The project is a research prototype with no ML framework dependencies, implementing its own linear algebra and gradient checks in Rust.

## Key takeaways
- **Non-transformer architecture**: PSSA uses a selective diagonal state-space recurrence (same family as S4/Mamba) instead of attention, giving O(n) rather than O(n²) cost per sequence length.
- **Hyperbolic memory bank**: A 512-slot episodic memory in Poincaré (hyperbolic) space allows general and specific memories to remain separable; retrieval is bounded to 4 slots per token at fixed cost.
- **Plasticity / fast weights**: The model rewrites part of its own transition matrix during the forward pass, with novelty-gated writes, refractory rate-limiting on overwrites, and ridge-regression consolidation of fast weights back into the base matrix.
- **Strong small-scale benchmark results**: PSSA reached the transformer's final loss after only ~2M tokens (vs 12.7M), and the held-out gap (0.43 nats) closely mirrors the training gap, suggesting better generalization rather than just better memorization.
- **12x faster inference on CPU**: Because the model carries a fixed-size state, generation cost does not grow with context length; on matched hardware PSSA is also ~4x faster during training.
- **Honest about limitations**: Text quality is poor at this scale ("a barget of the Prian Academy"), the training speed comparison was not hardware-matched, a per-model learning-rate sweep is still pending, and memory-bank ablation results are not yet available.
- **Written entirely in Rust with no ML framework**: All linear algebra is hand-coded; gradients are verified against a scalar reference path to ~3e-8 error; CUDA/cuBLAS and WebGPU backends are optional.