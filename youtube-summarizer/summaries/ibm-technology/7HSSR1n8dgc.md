# ADK vs RAG: How to Choose the Right AI Stack

Video ID: `7HSSR1n8dgc`

## Summary
This video explains how to choose between two AI architectural approaches: ADK (Agent Development Kit) and RAG (Retrieval-Augmented Generation). Using a hardware store analogy, the presenter breaks down when each approach is appropriate based on whether your AI needs to *act* or *recall*. The video also covers hybrid systems that combine both approaches for more complex, real-world use cases.

## Key insights
- **The core decision question is simple:** Ask whether your AI needs to *act* (ADK) or *recall information* (RAG). This single question drives most architectural decisions.
- **ADK is built for action and reasoning:** It excels at multi-step workflows, tool use, task coordination, and consistent repeatable behavior — situations where the value comes from logic, not memory.
- **RAG is built for knowledge and accuracy:** It connects the model to documents (PDFs, policies, manuals, databases) to ground responses in facts rather than the model's internal assumptions.
- **RAG shines with high-volume, high-detail, or frequently changing information** that humans can't reasonably memorize, such as legal documents, technical manuals, or large knowledge bases.
- **Most real-world systems use both:** Hybrid architectures let ADK handle task flow and decision-making while RAG supplies accurate, document-grounded information.
- **Use case guide:**
  - ADK → onboarding assistants, workflow automation, IT/HR triage, writing assistance
  - RAG → knowledge search, legal/medical lookup, technical support from documentation
  - Hybrid → legal/engineering co-pilots, healthcare assistants, enterprise task co-pilots
- **The hardware store analogy** neatly captures the relationship: ADK is the *tool aisle* (builds and acts), RAG is the *reference aisle* (informs and grounds) — and the best projects use both.