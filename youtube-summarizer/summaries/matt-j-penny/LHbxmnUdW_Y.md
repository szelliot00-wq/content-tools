# 5 Ways To Use Claude Code FREE Forever

Video ID: `LHbxmnUdW_Y`

## Summary
This video is a practical tutorial covering five methods to use Claude Code (an AI coding agent harness) for free or at drastically reduced cost. The presenter argues that Claude Code is simply a harness that can be pointed at any model — not just Anthropic's paid models — enabling users to substitute free or cheap alternatives. The content is most relevant to developers, vibe coders, and small business owners who want to use AI-assisted coding without ongoing API costs.

## Key insights
- **Claude Code is a harness, not a model.** It can be connected to any LLM, including locally-run or third-party models. The intelligence comes from the model, not the harness itself.
- **Method 1 — Ollama (local models):** Download and run a model locally (e.g., Gemma 4, 4B parameters, ~10 GB download). Zero inference cost, fully offline. Tradeoff: requires a powerful computer; smaller models produce lower-quality output.
- **Method 2 — OpenRouter (free cloud models):** Create a free OpenRouter account, generate an API key, and edit Claude's `settings.json` to redirect API calls to OpenRouter's free models. Free-tier users get a limited number of daily messages; depositing $10 unlocks ~1,000 free messages/day without consuming the deposit. Multiple accounts multiplied by $10 each = thousands of free daily messages.
- **Method 3 — OpenCode:** A separate tool (opencode.ai) that is functionally near-identical to Claude Code but free. Comes with its own "Zen" section of free models and also supports OpenRouter integration. Not the Claude Code harness itself, but produces equivalent results.
- **Method 4 — Cursor with Auto Mode:** Cursor is an AI-powered IDE. Its "auto mode" provides virtually unlimited free messages. A $20/month subscription yields what the presenter estimates as $250+ worth of compute value per month, making it extremely cost-efficient for serious vibe coders.
- **Method 5 — Cheap models via OpenRouter:** Rather than using free models, use very cheap paid models. Example: DeepSeek-V4-Flash at $0.20 per million output tokens vs. Opus 4.7 at $30 per million — over 100x cheaper. Still delivers usable results for coding tasks. Implementation is the same as Method 2: just swap the model ID in `settings.json`.
- The `settings.json` hack: Use Claude desktop's chat interface to ask it to find the path to its own settings file, then edit the `ENV` section to override the base URL and model ID.
- Gemma 4 (4B) is recommended as the best balance of file size, hardware requirements, and capability for local use.

## Use cases
- **Developers on a budget** who want AI coding assistance without monthly API bills.
- **Students or hobbyists** experimenting with vibe coding who can't justify paid subscriptions.
- **Small business owners** evaluating AI-assisted development before committing to paid tools.
- **Power users running multiple projects** who hit usage limits mid-project and need a fallback.
- **Offline/air-gapped environments** where cloud API calls aren't possible (Method 1 — Ollama).
- **High-volume automation** where cost-per-token matters and a slightly lower-quality model is acceptable.
- **Anyone already considering Cursor** who didn't know auto mode is essentially unlimited.

## Patterns & frameworks
- **The Harness/Model Separation Pattern:** Claude Code (and similar tools like OpenCode, Cursor) are "harnesses" — scaffolding that manages context, tool use, and agent loops. The model is a swappable component. Understanding this unlocks the ability to mix and match freely.
- **The $10 Deposit Unlock:** A quirk of OpenRouter's pricing — depositing $10 activates a daily free message allowance (1,000/day) without drawing down the deposit. Can be stacked across multiple accounts. This is a known platform incentive structure being used as a cost-avoidance strategy.
- **The settings.json Override Pattern:** A repeatable technique for redirecting any tool using standard OpenAI-compatible API conventions: set `ANTHROPIC_BASE_URL`, `ANTHROPIC_API_KEY`, and a model ID in the environment config. This pattern works for Methods 2 and 5 and is reusable any time a new cheaper model appears on OpenRouter.
- **The Cost-Per-Token Comparison Framework:** Compare target models against a known baseline (e.g., Opus 4.7 at $30/M tokens) to gauge relative value. A model at $0.20–$0.30/M tokens is 100–150x cheaper and may be "good enough" for most coding tasks — a deliberate quality-vs-cost tradeoff decision.