# The AI cost of JavaScript frameworks

Source: https://nolanlawson.com/2026/10/28/the-ai-cost-of-javascript-frameworks/

## Summary
Nolan Lawson built a benchmark to measure the real AI cost of building with different JavaScript frameworks, pushing back against "vibes-based" framework choices in the agentic coding era. He had Claude Opus 5.5 build the same Pokémon app 5 times each across 12 frameworks/meta-frameworks, then measured cost, time, tokens, lines of code, and Lighthouse performance metrics. The results show meaningful differences between frameworks — particularly between MPA and SPA approaches — with Angular and SvelteKit being the most expensive and Angular producing the most code by a significant margin.

## Key takeaways
- **MPA frameworks win on cost and performance:** Hono+htmx and Astro were the cheapest ($2.67–$2.76/run) and fastest to build, while Angular ($4.97) and SvelteKit ($4.28) were the most expensive.
- **Angular is a significant outlier:** It cost nearly 2x Hono+htmx, took the longest (17.2 min median), generated the most code (~2,000 lines vs ~1,370 for Hono+htmx), and had the worst TBT (103ms) and LCP (1,954ms).
- **Vanilla JS (no framework) underperformed:** Using raw Vite without a UI framework was neither the cheapest nor the best performer, suggesting some framework structure actually helps agents.
- **Lighthouse quality scores were nearly identical across frameworks**, so performance differences emerged mainly in JS bundle size, TBT, and LCP — metrics that broadly punish SPAs over MPAs.
- **Code size has direct monetary consequences in the AI era:** More lines of code means more tokens on every future edit, making conciseness a literal cost factor, not just an aesthetic preference.
- **Results are stochastic:** LLM randomness caused high variance between runs of the same framework, so single-run comparisons are unreliable — the author ran 3–5 iterations per framework.
- **The main argument:** Framework choices should be evidence-based, especially now that developers aren't hand-typing code and DX preferences matter less than actual measurable outcomes.