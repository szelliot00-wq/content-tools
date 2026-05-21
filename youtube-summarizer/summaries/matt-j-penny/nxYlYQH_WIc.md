# New Cursor Model SMASHES Claude and Codex

Video ID: `nxYlYQH_WIc`

## Summary
The video demonstrates Cursor's newly released **Composer 2.5** coding model, arguing it delivers comparable performance to Claude Opus and GPT-5.5 at roughly 10x lower cost. The presenter runs three live demos — a car wrap lead magnet web app, an AI-generated promo video, and a website update — all completed in under 2 minutes each. It is most relevant to developers, vibe coders, and small business owners looking to maximize AI coding output without paying frontier model prices.

## Key insights
- **Pricing**: Composer 2.5 standard tier is $0.50/M tokens in and $2.50/M tokens out. Claude Opus is $5/$25 and GPT-5.5 is comparable or more expensive out — both 10x+ the cost.
- **Cost per task**: The presenter emphasizes "cost per task" as a more meaningful metric than cost per million tokens. Composer 2.5 is shown to be ~15x cheaper than Opus 4.7 on this metric while matching or beating quality.
- **Speed**: Composer 2.5 built a full-stack lead magnet web app in ~20 seconds, a promo video with iterative frame review in ~2 minutes (vs. ~7 minutes for Claude/Codex), and a website section update in ~10–15 seconds.
- **Demo 1 — Car Wrap Lead Magnet**: From a single prompt, it generated a multi-page web app with image upload, wrap color/finish options, email capture gating, and integration with Google's Imagen 2 (called "Nana Banana 2" in the video) via OpenRouter API — all from scratch.
- **Demo 2 — HyperFrames Promo Video**: Using Remotion/HyperFrames, the model scraped a website, wrote a script, generated a 20-second animated promo video, exported frames for self-review, made corrections, and delivered an MP4 to downloads — for approximately $0.03 USD.
- **Demo 3 — Website Update via Notion**: The model read a Notion knowledge base, extracted mastermind course details, and updated a live website homepage with a new section — in ~10 seconds.
- **Fallback usage**: Cursor allows continued free use of slower models even after premium credits are exhausted, unlike Claude or Codex — useful for users on the $20/month plan who want overflow capacity.
- **Benchmark caveat**: The presenter explicitly downplays benchmarks, noting GPT-5.5 scores slightly higher on one test but that real-world task performance and cost efficiency matter more.
- **Cursor vs. competitors**: Described as more similar to Codex than Claude Code in UI/UX. Shows a to-do list style task breakdown with checkoffs, giving transparency into agent progress.

## Use cases
- **Small business owners** wanting cheap, fast prototypes (e.g., lead magnet tools, landing pages) without hiring developers
- **Vibe coders** who iterate rapidly and need high token limits without expensive API bills
- **Content creators / marketers** generating promotional videos or motion graphics via Remotion/HyperFrames at near-zero cost
- **Developers maintaining websites or internal tools** who want to automate routine updates (e.g., pulling content from Notion and publishing to a site)
- **Teams on budget** who are hitting Claude/Codex usage limits and need a cheaper overflow option
- **Anyone evaluating AI coding tools** on a cost-per-outcome basis rather than raw benchmark scores

## Patterns & frameworks
- **Cost-per-task framing**: Rather than comparing models on token price alone, evaluate total cost to complete a meaningful unit of work. Factors in both token efficiency and output quality. Used here to show Composer 2.5 is ~15x cheaper than Opus 4.7 in practice.
- **Prompt augmentation with a prompting guide**: The presenter pastes a "prompting guide" alongside his core instruction to automatically improve the prompt before the model acts on it — a lightweight meta-prompting pattern for better results without manual prompt engineering.
- **Agent self-review loop**: For the video demo, the agent is explicitly instructed to (1) generate output, (2) export frames and inspect them, (3) make corrections, and only then (4) deliver the final file. This creates a built-in quality gate within a single agent run.
- **Skill injection**: The presenter references adding an "open montage skill" to the prompt — a modular, reusable instruction block that modifies agent behavior (smoother transitions/flow) without rewriting the full prompt. A composable prompting pattern for Cursor agents.
- **Scoped API key hygiene**: Creating a short-lived (1-hour), labeled API key for a test, then deleting it — a lightweight security pattern demonstrated during live demos.