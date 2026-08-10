# What Is Chunkless RAG? How Docling & AI Agents Navigate Documents

Video ID: `vRZNJWw78BQ`

## Summary
The video explains the limitations of traditional chunk-based RAG (Retrieval Augmented Generation) when applied to large, structured documents like annual reports. It introduces "Chunkless RAG" as an alternative approach where an AI agent navigates a document's preserved hierarchical structure — rather than searching over flattened text chunks — to find precise answers. The approach relies on Docling, a tool that reconstructs the semantic tree structure from PDFs, enabling agents to reason through the document the way a human reader would.

## Key insights
- **Chunking destroys document structure.** Splitting a document into fixed-size text blobs severs headings from their paragraphs, tables from their explanatory text, and eliminates the relationships the author deliberately built in.
- **Similarity search has no spatial memory.** A chunk retrieved by vector similarity has no idea where it came from in the document, making it hard to answer questions that depend on context or span multiple sections.
- **Documents are trees, not flat text.** Authors organize content into titles, sections, subsections, tables, and references — a hierarchy that contains the answer to most questions if you navigate it correctly.
- **Chunkless RAG replaces matching with reasoning.** An agent reads the document outline, infers which branch of the tree likely holds the answer, opens just that section, and follows references as needed — mirroring how a human expert reads a report.
- **Context is preserved automatically.** Because the agent walked the tree to reach a paragraph, it retains the heading path above it — something a similarity-retrieved chunk entirely lacks.
- **Docling is the enabling layer.** PDFs store layout instructions, not semantic structure. Docling reconstructs the hierarchy (sections, reading order, intact tables) from a PDF, producing the structured object the agent needs to navigate.
- **The tradeoff is latency and complexity.** Tree navigation requires multiple model calls instead of one vector lookup, so it's slower and more expensive — worth it for long, precision-sensitive documents, not for fuzzy search across millions of short ones.
- **Hybrid systems are the practical answer.** Use similarity search to identify the right document within a large corpus, then use structure-based navigation to find the precise answer within that document.