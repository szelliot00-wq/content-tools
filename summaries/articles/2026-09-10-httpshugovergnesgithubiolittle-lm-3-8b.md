# Training a 3.8B LLM to 0.384 CORE for $998 – Hugo Vergnes

Source: https://hugovergnes.github.io/little-lm-3-8b/

## Summary
Hugo Vergnes trained a 3.8B-parameter LLM from scratch, achieving a CORE score of 0.384 in 43 hours for $998 on rented B200 GPUs. The project explores the practical space between toy models and research-lab-scale training, documenting what optimizations worked, what failed, and how hardware and architectural choices affected cost-efficiency. The final model outperforms GPT-2 (0.2565 CORE) by a significant margin, demonstrating that meaningful LLM training is now accessible to a single engineer with a modest budget.

## Key takeaways
- **A trapezoidal LR schedule** (warmup 5%, hold flat, then linear cooldown over last 50%) keeps the model learning until the final step — cosine decay wastes the tail end of compute budget.
- **Muon optimizer for matrix parameters** converges faster per token than AdamW despite a ~25% per-step overhead, which dilutes to ~4% with gradient accumulation.
- **ClimbMix dataset** produced dramatically faster convergence than FineWeb-Edu.
- **FP8 training + vocab padding** (50,257 → 50,304) together added ~33% throughput with minimal quality cost.
- **Fused linear cross-entropy loss** (Liger) is 6% slower per step but frees ~8 GB VRAM, enabling larger micro-batches that more than compensate.
- **Value embeddings** (721M params, 19% of total) improved CORE by 3.2% at essentially zero throughput cost since they are lookup operations, not matrix multiplications.
- **Context length matters for evaluation, not training**: the 1024-token run scored 0.338 because 3 of 22 CORE tasks were effectively unscorable due to prompt truncation; switching to 2048 tokens boosted CORE to 0.384 with only 9% throughput loss.
- **Local data shards beat streaming** — network variability during long runs costs more than the one-time download.
- **Config-driven infrastructure pays off**: expressing experiments as YAML diffs rather than code branches made iteration fast and cheap.
- **B200s offered better value than H100s** at this scale, achieving ~25% MFU (FP8) and 2.59× the throughput of an RTX 5090 on the same code.