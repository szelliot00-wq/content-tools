# Wayfinder Router: deterministic routing of queries between local and hosted LLM

Source: https://github.com/itsthelore/wayfinder-router

## Summary
Wayfinder Router is an open-source Python tool that deterministically routes LLM prompts to either a local or hosted model based on prompt complexity — without making any model call to decide. It analyzes structural features (length, headings, code blocks, lists) and optional lexical cues (math, reasoning terms) to produce a 0–1 score, comparing it against a configurable threshold in microseconds, fully offline. It acts as an OpenAI-compatible gateway proxy, so existing clients need only change their `base_url` to benefit.

## Key takeaways
- **No model call to route**: Unlike RouteLLM, NotDiamond, or OpenRouter Auto, Wayfinder uses a deterministic structural scoring algorithm — same prompt always yields the same routing decision, with zero API cost or added latency to decide.
- **Fully offline and self-hostable**: The scoring core has no external dependencies; it runs without a network connection and can be deployed as a Docker sidecar or standalone gateway.
- **Drop-in OpenAI proxy**: Any client using the OpenAI SDK just points `base_url` at the gateway; it also supports Anthropic's `/v1/messages` API for Claude Code integration.
- **Calibratable to your traffic**: The `calibrate` command fits a threshold, tiered model, or logistic classifier against your own labeled JSONL data, with cost-aware objectives (`--objective knee`) to maximize savings without collapsing to always-expensive routing.
- **Lexical signals are opt-in by default**: Reasoning/math/constraint term detection is disabled by default because blind testing showed it doesn't generalize without per-traffic calibration.
- **Multiple routing modes**: Binary threshold, tiered (route to N models by score bands), or a fitted classifier; all configurable in `wayfinder-router.toml`.
- **Feedback loop built in**: A `/v1/feedback` endpoint and `recalibrate` command let you continuously improve the routing cut from real user judgments without restarting the gateway.
- **Rich observability**: Every response includes `x-wayfinder-router-model`, `-score`, and `-mode` headers; a `/router` dashboard shows recent decisions; `/v1/savings` tracks realized cost savings vs. always-cloud routing.