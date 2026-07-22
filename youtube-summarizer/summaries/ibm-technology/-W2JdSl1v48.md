# Is Fine-Tuning Still Needed? LLMs, RAG, & LoRA

Video ID: `-W2JdSl1v48`

## Summary
The video examines whether fine-tuning LLMs is still necessary in 2025, using real-world examples like a legal AI company and BloombergGPT to show that frontier general-purpose models have largely caught up to custom-trained ones. It explains why this happened (larger context windows, reasoning models, cheaper inference) and introduces a full stack of weight-free customization alternatives. Fine-tuning is not dead, but it now occupies a much narrower, last-resort role in a modern AI development decision framework.

## Key insights
- **Fine-tuning's edge has eroded:** A legal AI company's custom model was preferred by attorneys 97% of the time over GPT-4 in 2023, but by 2025 seven general-purpose frontier models outperformed it on the company's own benchmark — without any legal-specific training.
- **Three forces closed the gap:** Massive context windows (1M+ tokens vs. the original 2K), reasoning models that "think harder" at inference time, and steadily cheaper/smarter frontier models all reduced the need to bake domain knowledge into weights.
- **RAG is the primary alternative:** Retrieval-Augmented Generation fetches relevant documents at query time and injects them into the prompt, avoiding the need to train documents into the model at all.
- **Context engineering matters:** A well-structured prompt — combining a system prompt, relevant data, format guidelines, and examples — can replicate much of what fine-tuning was used for.
- **Agent skills fill the procedural gap:** Markdown-based skill files package up how-to knowledge and tool instructions, letting any general-purpose model follow domain-specific procedures (e.g., writing SQL against a specific schema) without weight changes.
- **Fine-tuning still makes sense in specific cases:** Low-latency requirements (e.g., real-time voice agents where reasoning models are too slow), knowledge distillation from large teacher models into smaller ones, and reinforcement fine-tuning (RFT) for tasks with programmatically gradable outputs.
- **LoRA is the modern fine-tuning method:** Low-Rank Adaptation trains a small adapter on top of a frozen base model, making fine-tuning far more parameter-efficient than full retraining.
- **Recommended decision order:** Prompt/context engineering → RAG (for fresh or proprietary knowledge) → agent skills (for procedural know-how) → fine-tuning only as a last resort for bottlenecks the rest of the stack can't solve.