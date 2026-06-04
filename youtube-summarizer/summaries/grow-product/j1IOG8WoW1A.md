# ChatGPT Has 900M Users. I Run Their International Growth. Here's What Worked.

Video ID: `j1IOG8WoW1A`

## Summary
This episode features Abi Mujal, an international growth PM at OpenAI, giving an unprecedented inside look at how OpenAI PMs actually work — specifically demonstrating his Codex setup, a custom internal dashboard he built, and personal automation workflows. The core argument is that Codex has transformed PMs from document writers into builders, enabling them to own features end-to-end at 70–80% completion without engineering support. The episode also covers what drove ChatGPT's growth to 900M weekly active users internationally, particularly in non-Western markets. Most relevant to PMs, growth practitioners, and anyone building AI-powered workflows.

---

## Key insights

- **Codex as agent, not chatbot:** Abi frames ChatGPT's evolution in three stages — chatbot (launch), collaborator (with connectors/tools), and now agent (Codex), where you can delegate entire job functions end-to-end, not just get help with tasks.

- **The internal growth dashboard:** Abi built a single web app in Codex that consolidates 7–8 data sources (Tableau, Databricks, etc.) into one view showing country-by-country metrics — WAUs, penetration, growth trends, strengths/risks, competitive benchmarks — with an automated daily refresh at 9 AM. Previously, his team spent hours manually loading dashboards. The core insight: the unlock isn't having the data in one place, it's the **synthesis layer** — Codex adds a TLDR on top that no raw dashboard provides.

- **PM → builder shift:** Abi, who studied CS but hadn't coded since college, now takes features to 70–80% completion by pulling from the actual ChatGPT GitHub repo, pointing Codex to the most similar existing feature, doing a few iterations, and opening a PR for engineers to finish. Key workflow tip: ask an engineer "what's the most similar thing we've already built?" and use that as the reference point.

- **PRDs replaced by prototype + companion doc:** Abi has moved away from writing traditional PRDs. Instead he builds a prototype first, then writes a short companion FAQ doc that answers the 10 questions a stakeholder would have when viewing the prototype. The prototype is the main show; the doc is supporting material.

- **Daily Slack triage automation:** Given OpenAI's extreme Slack dependency (even some external partners are brought into Slack), Abi built a daily automated digest that scans key channels, flags unread messages from important people, and highlights things he hasn't responded to. Delivered once each morning.

- **Weekly update automation:** Codex pulls from Slack, Google Drive, Notion, and dashboards to auto-draft his weekly stakeholder update, which he then reviews and edits before sending.

- **Codex limitations acknowledged:**
  - Signal-to-noise separation is still imperfect — he always reviews Codex-drafted Slack updates before sending, never auto-posts.
  - Ambiguous data queries fail — e.g., "tell me about WAU growth" can pull B2C or B2B numbers incorrectly. Precision in prompts and pointing to specific dashboards is essential.

- **Computer use for personal life:** Abi used Codex's computer use feature to triage WhatsApp Desktop after returning from India — it read 1,700+ messages, identified two actionable items (a client meeting request and a friend's dinner cancellation), and drafted a WhatsApp reply by cross-referencing his Google Calendar, leaving the message in the composer for him to review before sending. The full loop ran in ~1 minute 8 seconds.

- **Tax filing AB test:** Abi built a 1040 tax filing web app using Codex that ingests tax documents and outputs a completed, IRS-ready form. He ran it in parallel with his accountant — Codex caught an income source the accountant missed. He still used the accountant for liability, but used it as a verification/audit layer.

- **International growth drivers for ChatGPT's 900M WAUs:**
  - Early product-market fit was in knowledge workers and students — but these segments represent only 10–20% of working adults in Brazil and under 10% in India, vs. 40–60% in the US/Germany.
  - **Search launch** was the first major unlock for non-knowledge workers — removing the arbitrary knowledge cutoff made ChatGPT useful for everyday queries.
  - **Image generation** was the second breakthrough — multimodal interaction resonated with users who don't primarily engage via long-form text. Image gen lowered the barrier from needing to read/write paragraphs to just creating visually compelling output.
  - India is now OpenAI's second-largest and fastest-growing market.

- **Image Gen 2 as step-change:** Abi describes it as the largest ELO jump of any model release. Key improvements: precise fine-grain edits, multi-image storytelling, better character consistency across frames, real-time web search integrated into generation, and dramatically improved multilingual text rendering (e.g., correct Japanese manga characters, books with text in Hindi/Bengali/Marathi/Malayalam). Use "thinking mode" for higher-fidelity, more realistic outputs.

- **Codex harness as the real differentiator:** Abi argues the industry spent years talking about the model, then the product, but the true unlock is the **harness** — the connectors, skills, and context configuration that powers what Codex can actually do. The harness is what enables multi-source data pulls and complex automations.

- **Experiment review skill built by the team:** Growth engineers built a shared Codex skill that automates the entire experiment lifecycle — writes the hypothesis, monitors the experiment, drafts the postmortem, and surfaces recommendations for the review meeting. Anyone who cares most about the workflow can author a skill, not just engineers.

- **Breaking into OpenAI:** Abi's path combined deep international PM experience (Meta election integrity, Nubank in Brazil/Mexico/Colombia, learning Portuguese) with actually building an AI product (a Chrome extension for real-time multilingual translation built on OpenAI APIs). He emphasizes the builder attitude — going out and constructing something — was as important as pedigree.

- **Eval as the currency of progress at frontier labs:** At OpenAI, getting researchers excited about a problem requires framing it as an eval — a rubric defining the problem space, test scenarios, expected outputs, and a measurable hill-climbing goal. PMs don't need to run evals end-to-end, but must understand what they're trying to achieve and speak the language.

---

## Use cases

- **Growth PMs** managing international or multi-market portfolios who need to synthesize data across many dashboards and data sources.
- **PMs at any company** who want to reduce time spent on recurring deliverables (weekly updates, stakeholder reviews, prep decks) through automation.
- **PMs who want to prototype faster** without waiting on design or engineering bandwidth — particularly for early-stage feature validation.
- **Product leaders at non-US companies or working in emerging markets** (India, Latin America, Southeast Asia) thinking about how to drive adoption beyond knowledge worker segments.
- **Anyone building for markets outside the US/Western Europe** who needs to think about multilingual text rendering, multimodal interaction patterns, and non-knowledge-worker use cases.
- **PMs trying to break into AI-first companies** who need to understand what skills and experiences actually differentiate candidates.
- **Small businesses and content creators** who want to use Image Gen 2 for studio-quality infographics, social content, and charts without hiring agencies.
- **PMs evaluating whether to write PRDs vs. build prototypes** as their primary alignment artifact.
- **Anyone handling sensitive personal data with AI** (taxes, calendars, messaging) who wants a framework for thinking about data safety and control permissions.

---

## Patterns & frameworks

**ChatGPT evolution arc: Chatbot → Collaborator → Agent**
The product has moved through three distinct phases as capabilities expanded. In agent mode (Codex), you delegate job functions rather than get assistance with tasks — it runs end-to-end without step-by-step guidance.

**The Synthesis Layer principle**
When data lives in multiple sources (7–8 dashboards in Abi's case), the unlock isn't consolidation alone — it's adding a TLDR/insight layer that no raw dashboard provides. Build tools that combine data *and* interpret it.

**PM as 80% builder**
Rather than handing fully-defined specs to engineering, PMs use Codex to build to 70–80% completion using real codebases, then hand off. Steps: (1) ask an engineer for the most similar existing feature, (2) point Codex to that reference, (3) iterate locally, (4) open a PR for engineering to finalize.

**Prototype + Companion Doc (PRD replacement)**
The prototype is the primary communication artifact. A short companion FAQ doc addresses the ~10 questions stakeholders will have when viewing it (null hypothesis, success metrics, safety/legal considerations). The doc supports the prototype, not the other way around.

**Context is king in Codex prompting**
Effective Codex prompts require three elements: (1) clear output format desired, (2) explicit input sources/connectors, and (3) criteria for what "important" looks like (e.g., "flag anything about blockers or eval metrics"). Generic prompts on ambiguous data tables fail.

**Human-in-the-loop control spectrum**
Codex offers a dial from "review every action" to "run autonomously." For consequential outputs (sending messages, posting updates), Abi always builds in a review step by specifying it in the prompt — Codex drafts, human approves. This is a deliberate design choice, not a limitation.

**International growth segmentation model**
Frame international expansion around the percentage of the working population that are knowledge workers. High-knowledge-worker markets (US, Germany: 40–60%) respond well to text-heavy, productivity-focused AI. Low-knowledge-worker markets (Brazil: 10–20%, India: <10%) require multimodal, search-first, visually intuitive entry points. Product strategy should differ accordingly.

**Eval as PM currency**
At frontier labs, proposals gain traction when framed as: here's the problem → here's a rubric for measuring it → here are the test scenarios and expected outputs → here's where we are vs. where we want to be. This is the language that gets research teams to prioritize a problem.

**Skill authorship principle**
Shared Codex skills (reusable, automated workflows) should be built by whoever cares most about the workflow — engineer, analyst, or PM. Ownership follows motivation, not job title.