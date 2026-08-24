# What Is a Digital Librarian AI Agent? Connecting SQL & Vector Database

Video ID: `eFf2OvkZxEM`

## Summary
The video introduces the concept of a "Digital Librarian AI Agent" that bridges two fundamentally different data systems: SQL databases (structured, factual data) and vector databases (unstructured, contextual documents). Using a pharmacy insurance denial as a running example, it explains why users often get answers without explanations — the "what" lives in SQL tables while the "why" lives in PDF policy documents. The video then outlines a six-step agentic workflow that an AI can follow to query both systems and synthesize a single coherent answer.

## Key insights
- **The "what vs. why" problem is pervasive.** Structured databases answer factual questions (is this covered?), but the reasoning and context live in unstructured documents (PDFs, presentations, webpages) that SQL can't reach.
- **Two databases, two query types.** SQL handles precise row/column lookups; vector databases handle semantic search to retrieve relevant paragraphs from documents. Effective AI agents must know which tool to use for which part of a question.
- **The six-step agentic workflow:** (1) read and understand the question, (2) decompose it into "what" and "why" components, (3) build the appropriate queries, (4) execute them against each database, (5) compile the results, and (6) synthesize a final answer.
- **LLMs handle reasoning; tools handle execution.** Steps involving understanding and synthesis are LLM tasks, while database querying and result reformatting are handled by external tools (e.g., Python code or database connectors).
- **Agentic workflows go beyond retrieval.** The shift from simple queries to multi-step agents turns siloed data repositories into reasoning engines — delivering grounded answers rather than raw data.
- **The pattern generalizes broadly.** The pharmacy example is illustrative, but the what/why split applies across industries wherever structured records and unstructured policy or context documents coexist.