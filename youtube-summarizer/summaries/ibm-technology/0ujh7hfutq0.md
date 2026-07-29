# Llama.cpp vs vLLM: Which Local LLM Engine Actually Scales?

Video ID: `0ujh7hfutq0`

## Summary
The video compares two popular local LLM inference engines — llama.cpp and vLLM — explaining their core optimizations and the use cases each is best suited for. It traces the motivation for local LLM deployment (cost, uptime, and privacy) back to Meta's Llama 2 release, then walks through how each engine addresses the hardware constraints of running large models. The central takeaway is that llama.cpp targets consumer/edge hardware while vLLM targets production-scale, GPU-accelerated deployments.

## Key insights
- **Why run local LLMs:** Three main drivers — cost savings vs. paid APIs, avoiding rate limits and outages, and keeping data private on your own hardware.
- **llama.cpp's core innovation is accessibility:** It makes models runnable on consumer hardware through quantization (reducing weight precision from float16 → int8/int4, shrinking VRAM requirements from ~30 GB to ~4 GB), the unified `.gguf` file format (bundles weights, tokenizer, and config into one swappable file), and CPU inference support for machines without a GPU.
- **llama.cpp spawned an ecosystem:** Tools like Ollama and LM Studio are built on top of it and are widely used by developers today.
- **vLLM targets scale:** Designed for multi-user, production workloads with broad hardware support (NVIDIA, AMD, Intel, Google TPUs) and day-one compatibility with models from major open-source labs.
- **Continuous batching:** vLLM processes requests as they complete rather than waiting for a full batch to finish — analogous to adding new pancakes to a griddle as spots open up — improving throughput under concurrent load.
- **Paged attention for KV cache:** vLLM optimizes GPU memory by efficiently managing the KV cache (which can reach dozens of GB), avoiding redundant recomputation for repeated prompts.
- **Speculative decoding:** A smaller "draft" model generates candidate tokens and a larger model verifies them, accelerating inference without sacrificing output quality.
- **LLM-D disaggregation:** An open-source project that splits the prefill and decode phases across hardware for further efficiency gains at scale.
- **Both expose OpenAI-compatible endpoints:** Drop-in replacements for the ChatGPT API, so existing RAG or agent codebases need minimal changes to switch.
- **Practical migration path:** Teams typically start with a paid API, watch costs rise, then migrate to llama.cpp (consumer/edge) or vLLM (production servers/Kubernetes).