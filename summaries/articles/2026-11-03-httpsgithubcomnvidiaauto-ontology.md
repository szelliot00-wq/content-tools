# Nvidia – open-source auto-ontology

Source: https://github.com/NVIDIA/auto-ontology

## Summary
NVIDIA Auto Ontology is an open-source library (Apache 2.0) that builds a semantic context layer from enterprise metadata to improve the reliability of AI agents querying databases. It auto-generates ontologies, reconciles definitions across systems, validates queries against certified lineage, and exposes everything to agent harnesses via MCP, CLI, and API. The stack consists of a Next.js frontend, FastAPI backend, and Postgres with pgvector, powered by NVIDIA NIM endpoints for LLM inference, embedding, and reranking.

## Key takeaways
- **Problem it solves:** Agents retrieving data need trusted semantic context — where data lives, what it means, and where it came from — to produce correct answers, not just fast ones.
- **Four core capabilities:** Discover (generate/connect ontologies), Ground (reconcile inconsistent definitions), Validate (check queries against certified definitions), and Expose (serve context via MCP/CLI/API).
- **Agent-friendly API:** Supports stateful multi-turn conversations via `conversation_id`, SSE streaming responses, and API token auth for scripts/notebooks — not just browser sessions.
- **Flexible model configuration:** Uses a triplet pattern (`_ENDPOINT`, `_API_KEY`, `_MODEL`) per role (reasoning, embedding, reranking), with a shared `DEFAULT_MODELS_*` fallback for simple setups.
- **Deployment options:** Docker Compose for local development, Helm chart for Kubernetes; supports Databricks, Postgres, Snowflake, and DuckDB as source databases.
- **MCP server included:** Agent harnesses like Cursor and Claude Desktop can connect directly to query data through the built-in MCP server.
- **Active development:** 1,352 commits, 87 branches, 1.1k stars, 112 forks as of the snapshot.