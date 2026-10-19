# The AI Memory Wall: Why LLMs & AI Accelerators Hit a Bottleneck

Video ID: `4b6KpFN7Rio`

## Summary
This video explains the "memory wall" — the growing gap between how fast modern AI chips can compute versus how fast they can fetch data from memory. Over the past two decades, GPU compute has grown ~6,500x while memory bandwidth has only grown ~7x, meaning faster chips don't automatically translate to faster workloads. The presenter uses the roofline model to explain arithmetic intensity and how it determines whether a workload is compute-bound or memory-bound, with practical implications for LLM inference.

## Key insights
- **The memory wall is a widening gap**: Compute (FLOPS) has grown ~6,500x since 2006; memory bandwidth has grown only ~7x. The bottleneck is data delivery, not raw computation.
- **Arithmetic intensity is the key metric**: Defined as FLOPS per byte moved from memory, it classifies workloads as either *memory-bound* (low intensity) or *compute-bound* (high intensity).
- **The roofline model maps workloads to hardware**: The "ridge point" (e.g., 281 FLOPS/byte for a B200 GPU) is the threshold — workloads below it are memory-bound; above it, compute-bound.
- **LLM decode is memory-bound; prefill is compute-bound**: Decode generates one token at a time (arithmetic intensity ≈ 1), requiring large weight reads. Prefill runs large matrix ops (intensity >1,000), saturating compute instead.
- **Batching is the practical fix for memory-bound decode**: Serving multiple requests simultaneously reuses the same loaded weights across many token generations, increasing arithmetic intensity and moving the workload toward the ridge point.
- **More compute doesn't help memory-bound workloads**: Throwing faster chips at a memory-bound problem yields little gain — the real lever is improving memory bandwidth or data reuse.
- **Profile before optimizing**: Use arithmetic intensity estimates and spec-sheet numbers (peak FLOPS, peak memory bandwidth) to locate your workload on the roofline before deciding where to invest optimization effort.