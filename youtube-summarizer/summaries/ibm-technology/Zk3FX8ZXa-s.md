# Granite 4.1, IBM Bob & building a quantum ecosystem

Video ID: `Zk3FX8ZXa-s`

## Summary
This episode of IBM's "Mixture of Experts" podcast covers three major AI topics: IBM's new Granite 4.1 model family and the IBM Bob agentic coding system, DeepMind's DeLoCo distributed training paper, and DeepSeek V4's release. The hosts — researchers and architects from IBM — discuss how enterprise AI is shifting toward composable, cost-efficient, specialized model architectures rather than monolithic general-purpose models. A bonus segment with IBM's Director of Quantum Partnerships explores how IBM is building collaborative ecosystems to pursue quantum advantage.

## Key insights
- **Enterprise AI is pluralistic, not monolithic:** IBM's Granite 4.1 positions specialized models (vision, speech, language, embedding) as composable building blocks that complement general reasoning agents rather than competing with them.
- **Enterprises care about practical tasks over flashy capabilities:** The vision models, for example, are optimized for table and chart understanding — exactly what businesses need — not generative image creation.
- **"Token maxing" is a real budget problem:** Companies are blowing through expensive AI token budgets on trivial tasks; IBM Bob and Granite 4.1 aim to right-size token usage by routing tasks to appropriately priced models.
- **IBM Bob acts as an intelligent orchestrator:** It routes tasks to the right model — frontier models for hard reasoning, smaller fine-tuned specialists for routine work — keeping costs sustainable at enterprise scale.
- **Legacy code modernization is a unique IBM moat:** Bob treats COBOL and mainframe code as first-class citizens, a capability competitors cannot easily replicate, critical for banking and finance sectors.
- **The agent era is transitioning to agent infrastructure:** Agents are evolving from experimental demos into governed, cost-controlled infrastructure, with general agents distilling common patterns into cheaper, deterministic sub-agents over time.
- **DeepMind's DeLoCo challenges the single-site training assumption:** The paper proposes distributed low-communication training across multiple data centers, achieving 88% "goodput" vs. 27% in classical setups, potentially reducing waste from hardware failures.
- **Training may federalize while inference centralizes:** Distributed training can tap stranded compute across locations and hardware generations; inference will likely remain co-located for low latency and KV cache efficiency.
- **Power grid constraints are driving architectural innovation:** Gigawatt-scale single-site clusters are hitting grid limits (e.g., Northern Virginia); distributed training offers a hedge against power and permitting bottlenecks.
- **DeepSeek V4 redefines inference economics:** With only 3% parameter activation (49B of 1.6T), its sparsity-driven efficiency is difficult for closed-source labs to match without rebuilding their serving infrastructure, structurally pressuring API pricing downward.
- **1-million-token context windows force a rethink of RAG pipelines:** Enterprise systems built around chunked retrieval may need to reconsider whether to simply load entire document sets into context now that large contexts are becoming cost-effective defaults.
- **Quantum computing requires ecosystem collaboration:** Advances in quantum require physicists, software developers, chemists, and domain experts working together; IBM's university partnerships (MIT, UIUC, Georgia Tech) reflect this team-sport reality.
- **Quantum advantage is expected in 2025:** Defined as a quantum-containing workflow outperforming classical computing in cost, speed, or accuracy, early examples are expected in chemistry, Hamiltonian simulation, optimization, and machine learning.
- **Chemistry is a natural fit for quantum:** Quantum computers operate on quantum mechanical principles, making molecular simulation a prime candidate for near-term practical quantum advantage.