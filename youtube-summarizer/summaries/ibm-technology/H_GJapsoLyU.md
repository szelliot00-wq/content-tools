# Why AI Models Run Faster on Some Chips: The KV Cache Effect

Video ID: `H_GJapsoLyU`

## Summary
The video explains how AI language models use a KV (key-value) cache to avoid redundant computation during token generation, then dives into how three different hardware accelerators — GPU, TPU, and IBM's Spyre — handle the fundamental tension between large-but-slow memory and small-but-fast memory. The core argument is that the same KV cache concept plays out very differently depending on which software layer orchestrates data movement on each chip architecture.

## Key insights
- **Every generated token requires attention over the full context.** Without caching, this would mean recomputing everything from scratch for each new word — the KV cache stores previously computed keys and values to avoid that redundancy.
- **The real bottleneck is data movement, not raw compute.** The system challenge is efficiently shuttling KV data between large/slow memory and small/fast memory close to the compute units.
- **On GPUs, the runtime and kernels share orchestration.** The serving runtime (e.g., vLLM) manages KV block allocation using a virtual-memory-style paging scheme; attention kernels handle how data flows through on-chip resources.
- **On TPUs, the compiler takes more control.** It pre-plans how to tile data and pipeline fetches — loading the next tile from HBM into VMEM while still computing on the current one.
- **On IBM's Spyre, orchestration is fully explicit.** Each core has a 2 MB software-managed SRAM scratchpad (not a hardware cache), and the compiler generates the exact load/store instructions to keep it fed from 128 GB of LPDDR5.
- **Same model, different behavior across chips.** Two accelerators running identical models can have very different throughput because the memory hierarchy and the layer responsible for orchestrating it differ fundamentally.
- **The right question when comparing accelerators isn't just FLOPS.** It's how efficiently each chip moves the model's memory state — especially relevant for long-context, decode-heavy workloads.