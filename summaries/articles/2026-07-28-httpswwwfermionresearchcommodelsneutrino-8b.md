# Neutrino-1 8B

Source: https://www.fermionresearch.com/models/neutrino-8b/

## Summary
Neutrino-1 8B is an 8.19B-parameter open-weights language model released by Fermion Research on July 27, 2026, built on Qwen3-8B and stored in a proprietary ternary-family weight format that compresses the model to a single 3.88 GB file — roughly 8x smaller than an fp16 equivalent. The compact format enables it to run on hardware ranging from H100 datacenter GPUs to 8 GB consumer GPUs and 16 GB MacBooks from one artifact without conversion. It supports speculative decoding via a paired 0.6B draft model, achieving up to 763 tok/s on H100, and is available publicly under Apache 2.0 via pip, GGUF/llama.cpp, and MLX.

## Key takeaways
- **Extreme compression:** All 252 transformer linear weights use a ternary-family coded format, shrinking the model to 3.88 GB on disk (downloaded as 2.56 GB) vs. ~16 GB for fp16 — weights stay bit-packed and are decoded inside matrix kernels at runtime.
- **Single artifact, all platforms:** The same container file runs on CUDA GPUs, Apple Silicon (MLX), and x86 CPUs with no conversion step.
- **Strong throughput:** 396 tok/s plain single-stream on H100, 33.7 tok/s on Apple M5 (MLX), and 30.7 tok/s on an NVIDIA L4 — fitting within 4.68 GiB VRAM at 4k context.
- **Speculative decoding up to 1.93x speedup:** Paired with the 0.6B draft model (328 MB), output is token-identical to plain greedy decode; 27,648 consecutive tokens verified with zero divergences.
- **Laptop-friendly drafting:** Both models fit in one MLX process under 6 GiB on a 16 GB M5 MacBook.
- **Competitive benchmarks:** MMLU 72.1, IFEval instruction-strict 80.2, BFCL v3 68.9, GSM8K 53.4 (thinking disabled, shipped artifact).
- **Fully open:** Apache 2.0 license, no waitlist or gating, available immediately on Hugging Face and via `pip install fermion-research`.