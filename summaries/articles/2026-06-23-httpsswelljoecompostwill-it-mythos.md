# Will It Mythos?

Source: https://swelljoe.com/post/will-it-mythos/

## Summary
"Will It Mythos?" is a benchmark article testing whether other AI models can replicate the bug-finding capabilities of a tool or model called Mythos. The author ran multiple models through a standardized harness (and initially through full-featured agents) to compare performance. Results include a notable surprise around MoE Gemma 4, which found a hard bug but also exhibited unusual looping behavior.

## Key takeaways
- The benchmark's sole purpose is to determine whether other models can match Mythos's performance on a specific task (likely code bug detection).
- Running models inside full-featured agents did not improve performance and often increased cost and token usage significantly — so the author dropped agent testing for most models except Claude.
- Claude models are tested via Claude Code rather than raw API because it's more cost-effective for subscribers, and agent usage doesn't hurt Claude's performance.
- MoE Gemma 4 produced a surprising result by finding a particularly hard bug, but also exhibited a problematic looping behavior more than any other model tested.
- The benchmark corpus has documented bugs, with full details linked in the article.