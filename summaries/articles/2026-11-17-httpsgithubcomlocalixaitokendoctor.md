# Tokendoctor – See what your Claude Code use overpays

Source: https://github.com/localixai/tokendoctor

## Summary
Tokendoctor is a Claude Code plugin that analyzes your token usage and helps reduce AI costs by up to 38%. It runs entirely on your machine, replays your past sessions at smaller context windows to show potential savings, and applies configuration fixes you approve via diffs — with a full undo capability. The author measured a drop from 412K to 219K tokens per request on their own six weeks of real usage.

## Key takeaways
- **Up to 38% cost reduction** measured on real usage; your mileage varies based on session size, models, and work type.
- `/tokendoctor:sessions` replays your own sessions at smaller context windows before making any changes, so you see your actual savings estimate first.
- `/tokendoctor:optimize` runs 38 configuration checks against Anthropic's docs and proposes fixes, each shown as a diff before applying.
- `/tokendoctor:dashboard` builds a local HTML file showing spend by day, model, reasoning effort, context size, and project — no network required.
- Every change is reversible: `/tokendoctor undo` lists all changes tokendoctor made and restores any of them without a model call.
- The "slide" feature replaces Claude's context summarization with old tool outputs inline, keeping the conversation intact while reducing context size.
- Install via `claude plugin marketplace add localixai/tokendoctor` — it's a Claude Code plugin (~104 stars, MIT license).