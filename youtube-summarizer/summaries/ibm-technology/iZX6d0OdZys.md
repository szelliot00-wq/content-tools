# What Is MLflow? Tracing AI Agents & LLM Workflows

Video ID: `iZX6d0OdZys`

## Summary
This video introduces MLflow as an observability platform for multi-agent AI systems, explaining why traditional HTTP-level monitoring is insufficient for debugging LLM workflows. It covers MLflow's core concepts — traces, spans, and LLM-as-a-judge evaluation — using a mortgage lending application as a running example. The presenter closes with four production-readiness tips that go beyond notebook demos.

## Key insights
- **Standard monitoring misses AI-specific failures.** A 200 OK response tells you nothing about whether an agent called the wrong tool, an MCP server returned empty data, or a stale prompt wasted tokens.
- **Traces and spans are the core primitive.** A trace is a full record of one request; spans are its individual steps (LLM calls, tool invocations, DB queries) arranged in a parent-child tree with inputs, outputs, latency, and token counts.
- **Four silent failure modes to watch for:** silent tool failures (agent proceeds on empty data), cascading latency (can't identify the bottleneck), context overflow (cryptic failures surfaced as generic timeouts), and nondeterminism (bugs that won't reproduce locally).
- **LLM-as-a-judge enables qualitative evaluation.** A second model can grade outputs on tool call correctness, call efficiency, relevance, safety, and natural-language compliance guidelines — critical in regulated domains like lending.
- **The prompt registry adds version control for system prompts.** Treat high-performing prompts like code: register them, version them, and audit changes over time.
- **Four production tips:** (1) use Postgres/MySQL + object storage instead of the default file backend; (2) enable async trace logging so span export doesn't add latency to user responses, and sample traces under heavy load while keeping 100% of errors; (3) point LLM judges at your own endpoint in enterprise/air-gapped environments and budget inference costs carefully; (4) run evaluations in CI as quality gates, not just in notebooks.
- **Open Telemetry compatibility prevents lock-in.** Traces can be dual-exported to Jaeger, Grafana Tempo, or other backends your platform team already uses.
- **One-line auto-instrumentation for supported frameworks.** `mlflow.langchain.autolog()` captures all LangChain/LangGraph operations automatically; custom glue code can be instrumented with the `@mlflow.trace` decorator.