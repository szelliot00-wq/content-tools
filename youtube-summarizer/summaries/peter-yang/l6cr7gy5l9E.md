# 11 Grok Bots I Still Use Every Day (Steal These Now)

Video ID: `l6cr7gy5l9E`

## Summary
The creator walks through 11 Grok bots he uses daily, built on the Grok AI platform, showing how each one handles a specific life or work domain. The core argument is that AI assistants are most powerful when split into single-purpose bots that can also communicate with each other — functioning like a personal AI team rather than one generalist tool. The video is most relevant to solo creators, entrepreneurs, and busy parents who want to automate repetitive tasks across work and personal life without managing a full team.

## Key insights
- **Dr. Light (bot-maker bot):** A bot that creates and audits other bots. Imported from the Grok marketplace (originally "Dr. Eggbot" by Lauren Tan). Running scheduled checks to ensure other bots' prompts and skills stay optimized. First bot the creator recommends setting up.
- **Chief of Staff:** An orchestrator bot that routes tasks to other bots. Example: told Chief to have Frugal Dad list headphones on Facebook Marketplace, and told Loving Husband to check school newsletters at 4pm on weekdays. Also reads and triages emails, then executes replies using a cloud browser.
- **Advisor bot:** Focused on long-term planning, not daily tasks. Pulls from a Google Doc with long-term goals, then sends a weekly Friday morning briefing covering what to focus on, YouTube performance, upcoming meetings. Integrates with Mercury Bank, YouTube, Granola, Substack, and the creator's website. Recommended "brutally honest advisor" prompt included in the video.
- **YouTube Producer:** Pulls 7-day channel outliers from the creator's channel and similar channels every Monday and Wednesday at 7am. Generates video ideas, thumbnail/title packages, hooks, and rough bullet-point scripts. Saves output to Linear tickets. Directly suggested the Grok bot video based on performance data.
- **Behind the Growth:** Monitors website funnel traffic for behindthecraft.com — visitors, conversion to paid subscribers, traffic sources, A/B tests on headline copy. Pulls data from Vercel and internal analytics. Can generate charts and send reports by email.
- **X Scout:** Crawls X/Twitter for trending AI tweets and the creator's bookmarks without using the paid API — instead logs into X on a cloud computer and browses like a human. Runs every morning to surface key tweets (e.g., Dario Amodei, Sam Altman posts) and unread bookmarks, replacing doom scrolling.
- **Frugal Dad:** Monitors Japan flight prices (specific routes: SFO→Tokyo→Fukuoka→SFO and Tokyo roundtrip) using Google Flights via cloud browser. Lists and renews items on Facebook Marketplace, negotiates with buyers autonomously. Creator sold headphones during filming. Also handles miscellaneous payments (e.g., piano teacher).
- **Weekend Planner:** Sends a family weekend brief every Wednesday via message and email covering local activities (example: Google Endless Summer Festival in Mountain View) and personalized movie/TV recommendations. Uses a `taste profile.md` file built from the creator's IMDb ratings. Creator updates it after each watch (e.g., "Toy Story 5, 9/10") so suggestions improve over time and don't repeat already-seen films.
- **Health Coach:** Sends a Saturday report pulling weight and body fat % from a Withings smart scale and workout data from a custom vibe-coded fitness app with an MCP. Reports total weekly volume (example: 27,000 lbs across 5 sessions), tracks progress toward a 16% body fat goal, and gives nutrition/workout tips.
- **Marie Condo:** The only bot kept since launch. Reviews emails, files, Google Drive, and subscriptions one category at a time and asks "does it spark joy?" Example: flagged Paper Design as an unused subscription to cancel. Always asks for permission before deleting or moving files.
- **Loving Husband:** Reads long school newsletter emails every Sunday and surfaces only actionable items (e.g., "Back to School BBQ — RSVP?"). Helps manage family logistics, errands, and school calendar requests that come from the creator's spouse.
- **Bots can talk to each other:** The creator demoed a multi-bot channel where all bots introduced themselves and then debated who is most useful — illustrating Grok's "Slack for AI" dynamic where bots can coordinate and interact.
- **Proactive scheduling is key:** Most useful bots run on recurring scheduled tasks without prompting — YouTube Producer runs Mon/Wed at 7am, Advisor runs Fridays, Health Coach runs Saturdays, Weekend Planner runs Wednesdays.

## Use cases
- **Solo content creators** who need help tracking YouTube performance, finding video ideas, and scripting without a production team
- **Entrepreneurs with a website funnel** who want automated traffic and conversion monitoring without a data analyst
- **Heavy X/Twitter users** who want daily AI-curated digests without doom scrolling or paying for the X API
- **Parents** who receive long, information-dense school newsletters and need only the actionable items surfaced
- **Budget-conscious individuals** who want passive price monitoring on flights, Amazon, or other platforms
- **People selling secondhand items** who want Facebook Marketplace listings and buyer negotiations handled automatically
- **Fitness-focused individuals** who want weekly accountability reports combining scale data and workout history
- **Anyone with digital clutter** (overflowing email, Google Drive, unused subscriptions) who wants a structured decluttering process
- **People who want a long-term planning partner** rather than just a reactive chatbot — particularly founders and creators with complex goals
- **Anyone new to Grok bots** who wants a starting template for a functional multi-bot personal AI system

## Patterns & frameworks

**Single-responsibility bot design**
Each bot has one clearly defined job. The creator explicitly advises against giving bots too many responsibilities. This mirrors software engineering's single-responsibility principle — it keeps bots focused, debuggable, and easier to improve.

**Orchestrator + specialist hierarchy**
Chief of Staff acts as the top-level router, delegating to domain-specific bots (Frugal Dad, Loving Husband, etc.). This is a hub-and-spoke coordination pattern — one bot manages complexity while specialists execute.

**Proactive scheduled tasks**
Rather than relying on the user to prompt bots, recurring scheduled tasks make bots autonomous. The pattern: define a deliverable → set a cadence → receive it without thinking. Examples: weekly video ideas, Friday planning briefs, Saturday health reports, Wednesday weekend briefs.

**Taste profile as personalization layer**
The creator exports raw preference data (IMDb ratings) → uses AI to synthesize it into a structured `taste profile.md` → feeds that file to bots as a persistent context document. This pattern works for any domain where personal preferences matter (movies, restaurants, workout styles, etc.).

**"Brutally honest advisor" prompt**
A specific reusable prompt: *"Act as my brutally honest advisor. Speak to me like a founder, creator, or leader with massive potential and blind spots that need to be exposed. Analyze my situation objectively and tell me what I'm doing wrong or making excuses about. Hold nothing back, but end on an encouraging note."* Applied to a long-term planning bot, this surfaces uncomfortable truths a standard AI would soften.

**Cloud computer as action layer**
Several bots don't use APIs — they log into web services (Facebook, Google Flights, X) via a cloud browser and interact like a human. This bypasses API costs and restrictions, enabling automation on platforms that don't offer affordable developer access. Tradeoff: requires granting account access to the bot's cloud environment.

**Bot marketplace bootstrapping**
Rather than building every bot from scratch, the creator imports community-built bots (Dr. Eggbot) from the Grok marketplace and customizes them. This lowers the barrier to building a functional multi-bot system quickly.