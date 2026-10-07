# How AI Models Scale Beyond a Single GPU Across LLM Workloads

Video ID: `qZBibWYcKH4`

## Summary
This video explains how large AI models — too big to fit on a single GPU — are deployed at scale using distributed inference across many GPUs. It covers the three core production constraints (model memory, KV cache growth, and request throughput) and walks through the main parallelism strategies used to address them. It closes by describing how real deployments layer multiple techniques simultaneously under a single orchestration layer.

## Key insights
- **Frontier models require hundreds of GPUs**: A trillion-parameter model needs ~2TB of memory, far exceeding the ~288GB of the largest single GPU, so distributed inference is unavoidable at scale.
- **Three production constraints must be solved together**: Whether weights fit in memory (model footprint), growing conversational memory (KV cache), and concurrent user capacity (request throughput).
- **Data parallelism** handles throughput by running full identical model replicas on separate GPUs and routing requests intelligently — no inter-GPU coordination needed.
- **Pipeline parallelism** splits the model by layers across GPUs (like an assembly line); keeping requests continuously flowing prevents most GPUs from sitting idle.
- **Tensor parallelism** splits individual layers horizontally across GPUs, each computing a partial result and combining via a "collective operation" — requires high-bandwidth, low-latency interconnects within the same server.
- **Expert parallelism** applies to Mixture-of-Experts (MoE) models, spreading specialized subnetworks across GPUs; each token is dispatched to ~8 of 256 experts, reducing compute per token but increasing GPU-to-GPU network traffic.
- **Prefill/decode disaggregation** separates the two inference phases onto dedicated GPU pools because they stress different hardware resources — prefill is compute-bound; decode is memory-bandwidth-bound. This only pays off with fast enough inter-pool networking (plain TCP/Ethernet usually isn't sufficient).
- **Real deployments use multi-dimensional parallelism**: Tensor parallelism within a server, pipeline parallelism across servers, data parallelism across replicas, expert parallelism for MoE models, and phase disaggregation — all managed by an orchestration layer that routes requests, balances load, and handles hardware failures.