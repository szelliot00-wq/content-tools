# I built a vulnerable app and spent $1,500 seeing if LLMs could hack it

Source: https://kasra.blog/blog/i-spent-1500-seeing-if-llms-could-hack-my-app/

## Summary
A security researcher built a deliberately vulnerable book review app (React Native/Expo frontend, Python backend, Firebase) and spent $1,500 testing whether various LLMs could autonomously find and exploit a hidden flag in a user's private reviews. The challenge required discovering a Firebase misconfiguration — a common real-world vulnerability class. Results varied significantly across models, with GPT-5.5 leading at a 70% solve rate and most others failing entirely.

## Key takeaways
- **GPT-5.5 performed best** (7/10 solves, $9.46/solve), consistently zeroing in on Firebase as the attack surface.
- **Cost efficiency varied wildly**: DeepSeek V4 Pro solved 3/10 at only $0.62/solve vs. Claude Sonnet 4.6 at $45.75/solve.
- **The key insight the winning models shared**: correctly identifying Firebase as the exploit vector rather than fixating on the REST API or the React Native app.
- **Guardrails hurt Claude Opus**: it got close multiple times but security refusals terminated sessions before completion — a late-refusal pattern also seen in Gemini 3.5 Flash.
- **Gemini 3.1 Pro Preview refused almost immediately** (median 9k tokens vs. 100k+ for others), making it effectively useless for this task.
- **Persistence mattered**: Claude Sonnet had 5 runs on the right path but hit the $10 budget cap — suggesting higher budgets could improve results.
- **Token usage doesn't correlate with success**: Qwen 3.7 Max used 7.32M tokens per run and solved 0/6; DeepSeek V4 Pro used 194k and solved 3/10.
- **This is not a rigorous eval** — small sample sizes and varying harness setups mean results should be interpreted as directional, not definitive.