# Why Does AI Need Access to the Web?

Video ID: `IRtSdLX_Obw`

## Summary
The video explains why LLMs need real-time web access to remain useful after their training cutoff, since their knowledge is frozen at release while the world keeps changing. It introduces the concept of a "knowledge layer" fed by a "web data infrastructure layer" that scrapes, structures, and delivers fresh web data to AI models at inference time. The core argument is that the biggest reliability problem in production AI isn't model intelligence — it's bad, outdated, or hallucinated data flowing into the system.

## Key insights
- **LLMs are static snapshots:** A model's knowledge freezes on its last day of training, making it blind to new products, prices, laws, and events from that point forward.
- **Hallucination is often a data problem, not an intelligence problem:** When asked about things it doesn't know, an LLM fills gaps with plausible-sounding but fabricated answers drawn from its training data.
- **AI agents amplify the risk:** Unlike humans, agents don't second-guess strange answers — they act on them confidently and at scale, and errors cascade through multi-agent pipelines quickly.
- **GIGO (garbage in, garbage out) is the core failure mode:** The biggest production AI failures stem from wrong, stale, or made-up data, not from weak models.
- **Direct web scraping is unreliable:** Websites block bots with CAPTCHAs and anti-bot tech, and raw HTML is token-heavy and hard for LLMs to parse correctly.
- **Trustworthy web data requires five properties:** It must be grounded (cited sources), deep (full context, not snippets), fresh (real-time), correctly formatted (markdown/JSON, not raw HTML), and timely (delivered before inference completes).
- **Data freshness varies by type:** E-commerce prices and stock can go stale within minutes; news within hours; static content like blog posts decays much more slowly — and each requires a different refresh strategy.
- **A dedicated web data infrastructure layer is the solution:** It sits between the open web and the knowledge layer, handling bot detection, formatting, and delivery latency so the LLM receives clean, reliable context.
- **The hardest problem in AI today is the data layer, not the model:** Getting real-time, reliable, structured web data to an LLM at inference time is the key bottleneck to building useful, trustworthy AI systems.