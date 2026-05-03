# How RAG, GraphRAG, and Context Engineering Improve AI Performance

Video ID: `pN-LfxNFiTc`

## Summary
This video explores why context — not model intelligence — is often the biggest limiting factor in AI performance. The presenter introduces the concept of "context engineering," which involves designing systems that deliver the right data to AI models at the right time, with proper permissions and governance. It breaks down the four pillars of effective context engineering and explains how techniques like RAG, GraphRAG, agentic RAG, and context compression work together to improve AI outcomes.

## Key insights
- **Context is the real bottleneck:** Modern frontier AI models have strong reasoning capabilities, but they frequently produce confidently wrong or generic outputs when they lack relevant, specific context.
- **Context engineering is more than prompt engineering:** It is the practice of building entire systems that discover, filter, and deliver the right data to AI models at runtime — across distributed, heterogeneous data sources.
- **Four pillars of good context engineering:** Connected access (querying data where it lives), a knowledge layer (adding meaning and relationships to raw data), precision retrieval (filtering by intent, role, and policy), and runtime governance (enforcing access controls at retrieval and response time).
- **Basic RAG has limitations:** Standard RAG works well for simple lookups but lacks structure and relationship awareness, making it insufficient for complex, multi-source queries.
- **Agentic RAG is iterative:** Unlike one-shot RAG, agentic RAG allows the AI to evaluate what it retrieved and go back for more if needed, improving result quality.
- **GraphRAG adds relational precision:** Instead of only finding semantically similar documents, GraphRAG navigates entity relationships and connections, providing more structured and accurate context retrieval.
- **Context compression reduces noise:** Even with large context windows, more irrelevant data leads to worse results. Summarizing and ranking content before sending it to the model maximizes signal and minimizes noise.
- **Governance must be enforced live:** Access controls and permissions need to be applied dynamically at both retrieval and response time — not just at the data storage level — to keep AI systems secure and defensible.