# DeepSeek-V4-Flash Update

Source: https://api-docs.deepseek.com/updates/

## Summary
DeepSeek released DeepSeek-V4-Flash into public beta on July 31, 2026, marking a significant upgrade in agent capabilities over the previous V4-Pro-Preview. The model uses the same architecture and size as V4-Flash-Preview but was re-post-trained, and natively supports the Responses API format with Codex adaptation. This changelog also documents the full history of DeepSeek API model upgrades dating back to May 2024.

## Key takeaways
- **DeepSeek-V4-Flash is now in public beta** — use model name `deepseek-v4-flash` with no changes to the API calling method.
- **Significantly improved agent benchmarks** vs V4-Pro-Preview: Terminal Bench 82.7, NL2Repo 54.2, DeepSWE 54.4, DSBench-FullStack 68.7, among others.
- **Same architecture as V4-Flash-Preview** — only re-post-trained, not a new model architecture.
- **Responses API support** is natively built in, with specific Codex adaptation.
- **V4-Pro API and APP/WEB models are unchanged** by this release; official V4-Pro release is coming soon.
- **Legacy model names** (`deepseek-chat`, `deepseek-reasoner`) were deprecated as of April 2026 and now point to V4-Flash non-thinking and thinking modes respectively.
- Benchmarks for Code Agent tasks used DeepSeek Harness minimal mode with `topp=0.95` and `temperature=1.0`.