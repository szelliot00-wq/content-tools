# Fine-tuning an LLM to write docs like it's 1995

Source: https://passo.uno/fine-tuning-docs-llm/

## Summary
A technical writer experimented with fine-tuning small open-source LLMs (Llama 3.1 8B and Qwen 2.5 7B) to produce documentation in the style of 1990s Microsoft manuals. Using ~192k training examples derived from scanned vintage Microsoft manuals (sourced from Bitsavers), QLoRA adapters were trained on rented cloud GPUs for ~$50 total. The results showed that style transfer worked convincingly — a 7B model trained on 1990s docs could produce period-accurate technical writing even for modern concepts like REST APIs.

## Key takeaways
- **Fine-tuning beats RAG for style transfer**: When the goal is adopting a writing style rather than retrieving facts, fine-tuning is more effective than retrieval-augmented generation.
- **QLoRA is practical and cheap**: Using quantized low-rank adapters on cloud GPUs (Runpod), the entire experiment cost ~$50 and ran over a weekend.
- **Instruct models fine-tune better than base models**: Base models (not trained to follow instructions) failed completely, producing garbage output. Instruct models adapted successfully.
- **Qwen outperformed Llama for style transfer**: Llama's heavy RLHF training made it resist stylistic changes; Qwen adopted the 1990s register more faithfully.
- **More training data beats more epochs**: The 192k-example, 1-epoch model generally outperformed the 40k, 3-epoch model, with less hallucination.
- **Lower rank = stronger style commitment**: A rank-8 adapter, having fewer "dials," committed more fully to the training corpus style. Rank 16 with only 1 epoch introduced hallucinations (e.g., SOAP where REST was expected).
- **Rank and epochs interact**: These hyperparameters behave like a mixer — tuning one without the other can degrade results.