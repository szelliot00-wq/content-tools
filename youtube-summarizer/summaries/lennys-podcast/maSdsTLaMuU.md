# How a handful of people built Grok Bot in 30 days | Roman Ugarte (SpaceXAI)

Video ID: `maSdsTLaMuU`

## Summary
Roman Ugarte, who leads product for Grokbot at SpaceX AI (formerly part of the Cursor team), describes how a small team built Grokbot — an AI "team of bots" product for knowledge workers — in roughly 30 days from first line of code to internal beta, then launched publicly three weeks later. The conversation covers the two founding product decisions that made Grokbot click, the intensive manual onboarding process that shaped the product, how the team thinks about simplicity and "unshipping," and the broader vision of AI bots as genuine colleagues with their own computers. It is most relevant to product managers, founders, and builders working on AI-native products who want to understand go-to-market strategy, product philosophy, and how to build something people actually trust enough to fully delegate work to.

---

## Key insights

- **Small, isolated team = speed.** The core Grokbot team was a handful of people, physically separated in the office with private Slack channels. Roman credits this isolation with enabling the rapid micro-decisions required to ship in ~30 days. A larger group or a longer planning horizon would have killed it.

- **Start fresh, don't retrofit.** The team explicitly chose not to build Grokbot inside Cursor. Adding new form factors to existing products produces a "shipping your org chart" experience — users feel the seams. A clean-slate product with a single consistent vision outperforms a tabbed frankenproduct.

- **Two early non-obvious decisions drove success:**
  1. **Everything runs in the cloud.** No local runtime, no "is my computer awake?" friction. Bots are persistent cloud entities with consistent state regardless of where you access them (phone, desktop, etc.).
  2. **Each bot gets its own computer.** Rather than sharing the user's machine, every bot has its own VM/computer in the cloud. This mirrors how you'd actually onboard a human colleague — you wouldn't ask them to share your laptop and credentials forever.

- **200–300 manual onboardings in two weeks.** The core team personally onboarded early users on 20-minute calls. Each painful session became an immediate product fix to solve before the next call. This surfaced non-obvious patterns (e.g., users organically promoting one bot to "chief of staff" to orchestrate others) without leading the witness.

- **Deliberately diverse early access.** Early users included not just AI tastemakers but a coffee shop owner who became a rich source of Shopify integration bugs and copy feedback — a use case the internally-dogfooding team would have missed entirely.

- **Unshipping is a core discipline.** The team aggressively cut features in the weeks before launch, including internal observability tools, chain-of-thought streams, and developer-facing UI. The rule: if you can't tweet it compellingly, you probably shouldn't build it.

- **"Grokbot can now" > "Grokbot now has."** Framing capabilities as things the bot *can do* (not new buttons or dropdowns added) forces the team to think in terms of genuine capability expansion, not feature accumulation.

- **Automations via natural language, no UI.** Instead of a sidebar with trigger/action dropdowns, users just tell their bot "remind me at 8am every day." 99% of automations on the platform are now created this way. Killing the automation UI was a deliberate unship.

- **Hide the internal mechanics.** Unlike most agent products, Grokbot doesn't show tool calls, browser clicks, or chain-of-thought. Users see a typing indicator and progressive updates, like messaging a colleague. Feedback confirmed no one wanted the raw stream.

- **"Chief of staff" pattern emerged organically.** SpaceX employees spontaneously started promoting one bot to manage the others — fanning out tasks, coordinating work. The team observed this without imposing it, then gently encouraged the pattern in the product once external users independently arrived at the same behavior.

- **Sales team was an unlikely power-user group.** Sales tools (e.g., Salesforce) often lack well-supported MCPs/APIs. Because Grokbot has its own computer and can click pixels, it unlocked workflows other AI tools couldn't. Each computer-use infrastructure improvement triggered an immediate outpouring of appreciation from the sales team.

- **Recruiting use case: always-on talent sourcing.** The recruiting team used Grokbot to: find co-authors of conference papers not indexed on Google Scholar, add new names to a spreadsheet daily, research SpaceX connections, and auto-send Slack intro requests — tasks that were previously entirely manual and where AI is "superhuman."

- **Grokbot within Grokbot.** You can run Grokbot on a bot's own computer for QA testing — one bot runs 10 regression workflows on each new desktop app build and logs results to Notion compared to previous versions.

- **"Info-vore" pattern.** Power users pipe firehoses of information (every mention of Grokbot on X, Slack, email) into their bots. The bot triages, handles low-priority items, surfaces what matters, and can even page the user for truly urgent events. Roman describes this as "always-on chief of staff that survives your focus on high-leverage work."

- **The 100% vs. 90% threshold is categorical.** An AI that gets you 90% there still weighs on you — you're mentally tracking it, expecting to intervene. One that fully completes the task is a qualitatively different experience. This is what Grokbot aims for: "no-look passes" to a trusted colleague.

- **Coding adoption playbook will repeat for knowledge work.** Developers used AI coding tools on nights/weekends, felt the future, then demanded them at work. The same pattern is beginning for knowledge workers — personal Grokbot use cases (controlling a robot vacuum, negotiating Tesla charging rates) will create demand inside companies.

- **Three pillars of SpaceX AI:** (1) coding products (Cursor + Grok Build), (2) general knowledge work (Grokbot), (3) general model training — focused on practical/useful AI, not abstract superintelligence pursuit.

- **Two core company values:** "Delete the product" (remove scaffolding as models get smarter; don't accumulate features) and "Just do the thing" (no ask-for-permission culture; if you see something that needs to happen, go fix it).

- **Moats are discovered, not planned.** Cursor didn't win by engineering a moat strategy. It won by obsessing over what's impossible today, building it anyway, deleting it when it becomes table stakes, and pulling to the next impossible frontier. Distribution and data advantages accrued as byproducts.

---

## Use cases

- **Founders building AI-native products** who need to decide whether to build a new product vs. add to an existing surface.
- **Product managers** deciding what to cut vs. ship, and how to frame capabilities to users.
- **Early-stage teams** thinking about team size, isolation, and speed-to-prototype tradeoffs.
- **Go-to-market leaders** designing early access programs and user onboarding for novel AI products.
- **Sales teams** using AI to automate workflows in tools with no API/MCP support, by leveraging computer-use agents.
- **Recruiting/talent teams** building always-on sourcing pipelines that go beyond LinkedIn to conference papers, co-author graphs, and warm intro automation.
- **Knowledge workers** wanting to delegate full tasks (not just drafting) to AI — email triage, Slack monitoring, daily digests, QA testing.
- **Power users of AI tools** looking to structure multi-bot systems with a "chief of staff" bot orchestrating specialist bots.
- **Entrepreneurs/founders** trying to understand moat strategy in fast-moving AI markets where traditional competitive analysis breaks down.

---

## Patterns & frameworks

**1. The "Colleague Pill" decision framework**
When a product debate has valid arguments on both sides, remove yourself from "tech company thinking" and ask: what would you want from a human teammate in this exact situation? The answer is usually unanimous and clarifying. Then build that. Used for decisions like: should bots show internal tool calls? (No — you wouldn't demand second-by-second updates from a colleague.) Should bots have their own computer? (Yes — you wouldn't ask a new hire to share yours.)

**2. "Grokbot can now" framing**
For any feature or capability being considered, complete the sentence "Grokbot can now ___." If it's not compelling enough to tweet, reconsider building it. This reframes the product roadmap away from UI additions ("Grokbot now has a new dropdown") toward genuine capability expansions, and forces honest assessment of user value.

**3. The Chief of Staff / Team of Bots architecture**
Users create 5–10 specialist bots (each with a distinct domain/scope), then promote one to "chief of staff" who orchestrates the others. The chief of staff receives high-level intent, fans tasks out to specialists, and manages coordination. This emerged organically from SpaceX employees and was validated externally before being gently encouraged in the product.

**4. "Pull to the frontier" product strategy (Cursor's repeating loop)**
Identify what's impossible today but will be possible in 3–6 months as models improve. Build it now (with engineering scaffolding if needed). Ship it. Delete the scaffolding when models catch up and it becomes table stakes. Immediately begin building the next impossible thing. Repeat continuously. Moats (data, distribution, trust) accumulate as byproducts of this loop rather than being planned upfront.

**5. The Info-vore Bot pattern**
Connect a bot to every high-volume information feed relevant to your role (Slack, email, Twitter/X mentions, RSS, etc.). Give it a high-level description of your role and priorities. Configure it to: (a) notify you immediately for urgent items, (b) include medium-priority items in a daily digest, and (c) silently handle low-priority items. Progressively upgrade from V1 (Slack + email triage) toward always-on ambient intelligence that pages you only when truly warranted.

**6. Manual onboarding as product research**
For the first ~200 users of a novel AI product, onboard them by hand on live calls. Each painful moment in the onboarding session becomes an immediate next-day fix. Deliberately include non-obvious user profiles (e.g., small business owners) to check Silicon Valley blind spots. Do not lead the witness — observe what patterns users discover independently before encoding them in the product.

**7. "Delete the product" value**
Treat feature removal as a first-class product discipline, not a concession. As models get smarter, scaffolding built to compensate for model limitations should be actively removed. Set the bar: if a capability doesn't need pixels (UI), kill the pixels and let the bot handle it behind the scenes. Applied repeatedly, this keeps the product simple and the UX focused on intent rather than controls.