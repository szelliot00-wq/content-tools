# A single function Jev-like wrapper for LLMs, including vision models

Source: http://allanrbo.blogspot.com/2026/09/a-jev-like-wrapper-for-llms-including.html

## Summary
Allan Riordan Boll's blog post describes a Python implementation of a Jev-style LLM wrapper that works with both text and vision models. The core technique uses LLM token log probabilities to classify structured questions with a single generated token, making inference fast and cheap. The author extends the Jev request format with an `attachments` field for images, enabling real-time webcam frame analysis using a local Gemma 4 12B model or OpenAI's API.

## Key takeaways
- **Log probability trick**: By requesting only 1 output token and reading `top_logprobs`, you can turn an LLM into a fast structured classifier without parsing free-form text.
- **Vision model support**: The technique works with multimodal models — you can attach base64-encoded images alongside text state to ask visual questions.
- **Performance**: Running locally with Gemma 4 12B on an RTX 3090 yields ~1 FPS for 3 questions per webcam frame; OpenAI's API achieved ~0.2 FPS (limited by per-question connection overhead).
- **KV caching opportunity**: Since all questions share the same state prefix, backends that support KV caching can avoid reprocessing the shared context on each question.
- **Jev question types supported**: The wrapper handles `choice` (pick one option), `noul` (true/false probability), and `score` (ordinal scale) question types.
- **Dual-backend compatibility**: The script abstracts differences between llama.cpp (Chat Completions endpoint) and OpenAI (Responses endpoint) to support both transparently.
- **Flexibility over efficiency**: Specialized CV models would be faster, but this approach lets you define detection conditions in plain English without retraining.