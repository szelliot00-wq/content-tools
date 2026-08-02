# Running Kimi K3 on MI355X at Better Performance per Dollar Than B300

Source: https://www.wafer.ai/blog/kimi-k3-mi355x

## Summary
Wafer ran Kimi K3 (a 2.8T parameter open-source model) on AMD MI355X GPUs and benchmarked it against NVIDIA B200 and B300 configurations. The MI355X achieved 952 tok/s aggregate throughput per node and 48 tok/s per dollar — crushing the B300's 33 tok/s/$ despite the B300 winning on raw throughput. Getting there required fixing two ROCm-specific bugs: a missing `top_k_renorm_prob` definition breaking speculative decoding, and a head-count mismatch preventing the fast AITER MLA prefill kernel from loading.

## Key takeaways
- **MI355X wins on performance per dollar**: At ~$2.50/GPU-hr vs $6.00 for B300, the MI355X delivers 48 tok/s/$ versus the B300's 33 tok/s/$ and the B200's 7 tok/s/$.
- **Kimi K3's 2.8T parameters demand hardware with high VRAM**: Only the MI355X (288GB/GPU) and B300 (288GB/GPU) can serve it on a single 8-GPU node; B200 requires two nodes (TP16).
- **Speculative decoding gave a major throughput boost**: Adding DSpark spec-dec yielded ~2.2× single-stream improvement and +18% peak aggregate on ROCm, once a missing kernel definition was patched with a plain PyTorch fallback.
- **Prefill (TTFT) remains AMD's weak spot**: Cold prefill on MI355X was ~51s vs ~23s on B300 for a 172k-token input, though a zero-padding fix to the AITER MLA kernel narrowed the gap 2–3×.
- **AMD's software gap is closing fast**: Kimi K3 shipped with day-0 AMD support, and the remaining bugs were minor framework issues — fewer than previous models required — suggesting the CUDA moat is eroding.