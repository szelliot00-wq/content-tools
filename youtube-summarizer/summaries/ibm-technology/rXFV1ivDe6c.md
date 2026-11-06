# Are Vector Databases Still Needed? RAG, AI Agents & Search

Video ID: `rXFV1ivDe6c`

## Summary
The video examines whether vector databases are still necessary for AI retrieval tasks, framing the decision as a four-level pyramid: no retrieval, keyword search, vector index in an existing database, and a dedicated vector database. The presenter argues you should only climb to the next level when your workload genuinely demands it, walking through the tradeoffs of each approach including cost, accuracy, and scale.

## Key insights
- **The retrieval pyramid**: No retrieval (large context window) → keyword/agentic search → vector index in existing DB → dedicated vector database. Move up only when the workload warrants it.
- **Long context windows reduce the need for retrieval** at small scale — just paste relevant documents into the prompt — but context bloat degrades model accuracy as corpus size grows.
- **Agentic keyword search can substitute for semantic search**: an AI agent running multiple grep-style searches iteratively can close the accuracy gap without embeddings, since it can refine queries across multiple attempts.
- **Embedding costs are non-trivial**: every document must be chunked and embedded on ingestion, every query must be embedded at search time, and switching embedding models requires re-embedding the entire corpus.
- **The semantic gap is the core argument for vector search**: a user asking "how do I reset my password?" won't match a ticket titled "credentials loop after update" with keyword search, but they are close neighbors in embedding space.
- **Most mainstream databases now include vector search natively**, making a dedicated vector database unnecessary unless you're operating at very high scale (millions of vectors with low-latency query requirements).
- **Dedicated vector databases justify themselves at scale**: they are purpose-built to hold billions of vectors and return results in milliseconds, where general-purpose databases start to strain under memory pressure.
- **The two-question framework**: (1) Is vector search needed at all? (2) If yes, is a *dedicated* vector database needed, or does the built-in vector index of an existing DB suffice?