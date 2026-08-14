# AI & Data Science Periodic Tables: How They Work Together

Video ID: `jAkB_qeATag`

## Summary
This video explains how data science and AI are deeply interdependent, using two custom "periodic tables" as a teaching framework. The hosts walk through a concrete document Q&A use case to show how 12 elements from both tables combine into a working pipeline. They then extend the example into a feedback loop that uses drift detection and synthetic data to improve the system over time.

## Key insights
- **Data science underpins AI**: Embeddings and LLMs are only as good as the cleaned, structured data beneath them — garbage in, garbage out applies directly to AI systems.
- **The relationship is now bidirectional**: AI models are increasingly used to label data and generate synthetic training data, creating a loop where data feeds models and models feed back into data preparation.
- **The Data Science Periodic Table** organizes elements by data maturity (rows: raw → prepared → modeled → validated insight) and function (columns: acquisition, preparation, modeling, generation, evaluation), with a quantum addendum for quantum-specific techniques.
- **The AI Periodic Table** has five groups (reactive, retrieval, orchestration, validation, models) and four rows (primitives, composition, deployment, emerging), covering everything from prompts and embeddings to multi-agent systems.
- **A RAG-based document Q&A pipeline** can be built from just 12 elements: ETL, data ingest, cleansing, structuring, encoding, and governance on the data science side; embeddings, vector database, RAG, prompt construction, LLM, and guardrails on the AI side.
- **Governance (Go) is load-bearing**: Without enforcing permissions at both the data retrieval and output stages, a system can leak documents an analyst isn't authorized to see.
- **Static pipelines degrade**: Query distributions shift over time, so adding drift detection (DR), synthetic data generation, and fine-tuning (Ft) closes the loop and lets the system self-improve without manual intervention.