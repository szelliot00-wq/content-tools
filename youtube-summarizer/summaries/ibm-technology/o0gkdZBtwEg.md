# How KV Cache Speeds Up LLMs for Faster AI Models on GPUs

Video ID: `o0gkdZBtwEg`

## Summary
This video explains why LLM inference performance degrades under concurrent load and introduces two core techniques — KV cache and paged attention — from the vLLM inference engine that address GPU memory inefficiency. It walks through how transformers generate tokens in two phases (prefill and decode), how naive memory allocation wastes 60–80% of KV cache space, and how paged attention fixes this by borrowing OS virtual memory concepts. The video closes with four practical tuning knobs for production deployments.

## Key insights
- **Two inference phases have different bottlenecks:** Prefill (processing the input prompt) is compute-bound; decode (generating tokens one by one) is memory-bound. KV cache sits in the decode path.
- **KV cache trades memory for compute:** Without it, generating the 1,000th token would require recomputing keys and values for all 999 prior tokens. The cache stores those matrices so each new token only computes its own KVQ and attends over the cached history.
- **Naive memory allocation is wasteful:** Traditional systems pre-allocate a contiguous block sized to the *maximum* possible sequence length per request. If max context is 2,048 tokens but average usage is ~500, ~75% of that reserved space sits empty — research shows 60–80% of KV cache memory is wasted this way.
- **Paged attention fixes fragmentation the same way OSes handle RAM:** KV cache is broken into fixed 16-token pages that can live non-contiguously in VRAM, allocated on demand. A block table maps logical to physical addresses, eliminating internal fragmentation, external fragmentation, and redundant system-prompt duplication.
- **Tune `gpu_memory_utilization`:** Default is 0.9; push to 0.95 on stable workloads for more concurrency, pull to 0.8 if you're hitting OOM errors under burst load.
- **Enable prefix caching:** vLLM hashes KV blocks by token sequence so requests sharing a system prompt reuse the same physical memory. RAG pipelines and multi-turn chat commonly see 75–95% cache hit rates and dramatically lower time-to-first-token.
- **Enable chunked prefill for throughput:** By default, prefill runs to completion before decode resumes, causing token stutter under long prompts. Chunked prefill prioritizes decode batches first, then fills remaining compute with prefill chunks — production deployments report ~50% throughput gains. Pair with `max_num_batch_tokens > 2048`.
- **Speculative decoding helps latency-sensitive workloads:** A small draft model proposes tokens; the large model verifies them in one forward pass. Output quality is mathematically identical to the large model alone, but gains shrink at very high concurrency where the GPU is already saturated.