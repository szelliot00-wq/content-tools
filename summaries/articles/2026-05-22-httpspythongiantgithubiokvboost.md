# Show HN: KVBoost – chunk-level KV cache reuse for HuggingFace, 5–48x faster TTFT

Source: https://pythongiant.github.io/KVBoost/

## Summary
KVBoost is a drop-in Python library for HuggingFace Transformers that dramatically reduces Time to First Token (TTFT) through chunk-level KV cache reuse and several complementary optimizations. It requires no model rewrites or fine-tuning, and achieves 5–48x faster TTFT compared to the HuggingFace baseline. It also enables running large models (32B+) on consumer-grade GPUs with as little as 8GB VRAM via AWQ layer streaming and CPU paged decoding.

## Key takeaways
- **Chunk-level KV cache reuse** eliminates redundant prefill for shared prompts, reducing TTFT from 850ms (baseline) to 210ms.
- **Multi-turn cache hit rates** improve significantly with conversation depth, reaching ~85% by turn 5+.
- **FlashAttention-2 integration** provides an additional 3–5x TTFT speedup over vanilla HuggingFace via memory-efficient tiled CUDA kernels.
- **AWQ Layer Streaming** enables 32B+ models to run on 8GB VRAM by streaming 4-bit quantized weights from host memory over PCIe.
- **CPU Paged Decoding** offloads KV cache to system RAM, preventing OOM errors on long contexts.
- **Zero-friction adoption**: `pip install kvboost`, MIT licensed, no architecture changes or fine-tuning required.