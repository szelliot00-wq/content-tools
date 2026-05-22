# CAG vs Long Context: How AI Models Use and Remember Information

Video ID: `B_RrXwDupIg`

## Summary
The video explains two alternatives to RAG for giving LLMs access to external knowledge: long context (stuffing documents directly into the prompt) and Cache Augmented Generation (CAG), which pre-computes a KV cache to avoid reprocessing documents on every query. It covers how context windows have grown dramatically (from 1K tokens in 2020 to 2M by 2024), the trade-offs of each approach, and how major LLM providers now offer prompt caching as a managed service that makes CAG practical without custom infrastructure.

## Key insights
- **Long context = simplicity, but repeated cost.** Every query reprocesses all documents from scratch — 10 queries means reading the same docs 10 times, multiplying both cost and latency.
- **CAG pre-computes once, reuses many times.** The KV cache (the model's internal representation of processed documents) is saved after the first pass and loaded for all subsequent queries, yielding reported speedups of 10–40x.
- **The "lost in the middle" effect is a real limitation of long context.** LLMs attend better to information at the beginning and end of a context window; content buried in the middle suffers degraded retrieval accuracy.
- **CAG requires a stable knowledge base.** When source documents change frequently, the entire KV cache must be recomputed, eroding the latency and cost savings.
- **Use case fit matters:** Long context suits one-off or low-frequency queries (e.g., analyzing a single document). CAG suits high-frequency, repeated queries against stable data (e.g., an HR chatbot over company policies).
- **Prompt caching makes CAG accessible.** Providers like Anthropic and Google now manage KV cache infrastructure automatically; repeated requests sharing the same prompt prefix can receive up to ~90% token cost discounts.
- **Neither approach eliminates RAG.** When the knowledge base is too large to fit in any context window, or data changes constantly, retrieval pipelines remain necessary.