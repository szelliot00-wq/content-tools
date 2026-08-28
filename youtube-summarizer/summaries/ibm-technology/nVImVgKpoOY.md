# LLM & AI Agent Benchmarks vs Reality: Why AI Applications Break

Video ID: `nVImVgKpoOY`

## Summary
This video explains why high leaderboard scores don't guarantee good real-world AI application performance. It covers the two pillars of AI benchmarking — model evaluation (accuracy, domain fit) and system evaluation (latency, throughput, cost) — and how both must be measured together. The video also addresses why agents require layered evaluation at every step of their decision chain, not just at the final output.

## Key insights
- **The accuracy-performance-cost triangle**: You can only optimize two of the three simultaneously — a cheap, fast model sacrifices accuracy; a highly accurate, fast model gets expensive; etc.
- **Leaderboard scores are a starting point, not the finish line**: Benchmarks test one controlled thing; production tests everything else, including your specific data and traffic patterns.
- **Two types of evaluation are required**: Model evaluation (is it correct?) and system evaluation (is it fast and scalable enough?).
- **Token distribution shapes benchmark results dramatically**: A RAG workload (4,000 input tokens, 512 output) behaves completely differently from a chat workload (128 in, 1,000 out) — benchmarking with the wrong shape gives misleading numbers.
- **Inference has two distinct phases with different bottlenecks**: Pre-fill (processing the prompt) is compute-heavy; decode (generating tokens one by one) is memory-heavy. Each must be measured separately.
- **Service Level Objectives (SLOs) anchor system benchmarks to real targets**: e.g., 99% of requests under 300ms — these tie performance metrics to actual user expectations.
- **The inflection point is the key capacity planning number**: Latency stays flat under low load, then spikes — the sweet spot just before that spike defines maximum sustainable throughput.
- **LLM-as-a-judge scales open-ended evaluation, but humans must calibrate it**: A powerful model grades outputs using a rubric, but domain experts must verify those grades match real-world quality standards.
- **Agent evaluation requires a pyramid, built bottom-up**: System performance → response formatting → safety/bias → factual accuracy → domain-specific checks. Skipping to the top without the foundation causes the whole system to collapse.
- **Every link in an agent's chain is a potential failure point**: Tool selection, retrieval quality, intent understanding — each step needs its own evaluation, not just the final answer.