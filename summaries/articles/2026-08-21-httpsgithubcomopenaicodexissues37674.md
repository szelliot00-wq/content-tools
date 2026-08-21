# Codex on AWS bedrock bug causing 10x charges

Source: https://github.com/openai/codex/issues/37674

## Summary
This is a GitHub issue (#37674) filed against the OpenAI Codex CLI reporting that the native Amazon Bedrock provider for GPT-5.6 Sol lacks explicit prompt cache controls, causing every request to re-write the full prompt prefix instead of reading from cache. One user observed $1,182 in cache-write costs (85% of total spend) over just four days, and another reported a 5x daily cost increase after upgrading to version 0.147.0. A contributor identified the root cause and posted a workaround, and an OpenAI team member has since attributed it to a newly-enabled web search tool invalidating the Bedrock prompt cache.

## Key takeaways
- The Codex CLI sends a `prompt_cache_key` but omits `prompt_cache_options` and `prompt_cache_breakpoint` fields required for explicit caching on Bedrock, so every request rewrites the full prompt (~88K tokens on average) rather than reading from cache.
- Real-world cost impact was severe: 3,656 requests over four days generated 171.94M cache-write tokens costing ~$1,182, with cache writes accounting for 85% of total model spend.
- Upgrading from v0.146.0 to v0.147.0 appears to be a trigger — one user saw their cache write-to-read ratio jump from 0.08 to 8.84 and daily costs rise 5x; rolling back to 0.146.0 restored a 97% cache-read rate.
- An OpenAI contributor (celia-oai) identified the likely cause as a newly enabled web search tool invalidating the Bedrock prompt cache, and is working with the Bedrock team on a fix.
- **Immediate workaround:** disable the web search tool by adding `web_search = "disabled"` to your Codex `config.toml`; Codex can still perform web searches via shell commands.
- A community patch exists (scottleibrand's fork) that adds explicit cache breakpoints at stable and recent-history boundaries, achieving a 97.77% aggregate cache-read ratio in production testing.
- The fix requires: (1) serializing `prompt_cache_options` for GPT-5.6-capable Bedrock providers, (2) adding a `prompt_cache_breakpoint` field to input content blocks, and (3) surfacing per-turn cache-read/write telemetry so users can diagnose cache misses without digging through AWS Cost Explorer.