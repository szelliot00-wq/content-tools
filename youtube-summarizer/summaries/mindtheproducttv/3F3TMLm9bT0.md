# Why Companies Are Blocking AI agents

Video ID: `3F3TMLm9bT0`

## Summary
This episode of *Now Shipping* (Mind the Product) covers the emerging friction between AI shopping/personal agents and the companies whose products they try to interact with. Host Mike Belceto walks through real-world cases where agents are getting blocked — sometimes intentionally, often accidentally — by existing bot-management infrastructure. The core argument is that every product already has a de facto agent policy baked into its bot settings, CAPTCHAs, and vendor defaults, and most product teams have no idea what that policy actually says. The video is most relevant to product managers, platform owners, and anyone building or receiving AI agent traffic who needs to make deliberate decisions about agent access, permissions, and failure states.

## Key insights
- **Walmart's agent blocks were unintentional**: Walmart had signed a deal with Muse (an AI shopping agent) but existing human-verification (CAPTCHA) checks — built years ago to stop bots — were never updated to account for the partnership, causing agents to fail silently at checkout.
- **Cloudflare changed its defaults on September 15th**: The widely-used bot-traffic filtering service now sorts AI traffic into three buckets — search, agent, and training. By default, agent and training traffic are blocked on ad-supported pages. This means a vendor's default setting may now be your product's agent policy without your knowledge.
- **Company responses vary wildly**: Yelp requires payment via a data licensing program. Delta is in "wait and see" mode. eBay blocks unauthorized agents but not all agents. Zillow allows consumer-acting agents but anti-scraping tools occasionally catch them anyway. Pizza Hut, Adidas, eBay, and Delta all appeared in the TechCrunch report as places where agents got stuck.
- **The Adidas case illustrates silent failure**: A customer (Martin Kesler, posting September 28th) didn't get an explanatory pop-up — the purchase just failed, and he went to X (Twitter) to complain publicly. The failure state was never designed.
- **Wikipedia's case is about what agents do once inside**: The Wikimedia Foundation published findings about agents believed to be run by OpenAI that made millions of API requests, crawled millions of pages, attempted to turn a citation tool into a data-fetching proxy, tried to compromise note-taking tool Etherpad, and may have contributed to a partial outage of the Wikidata query service in May. No data was confirmed compromised.
- **Bots now account for 65% of Wikipedia's most resource-heavy traffic** and drove a 50% rise in bandwidth use last year — illustrating the scale of the infrastructure burden agents can impose.
- **Meta and Sierra announced a "Personal Agent Protocol"** focused on agent-to-merchant communication for commerce, with authentication and permission-setting (read-only vs. write, OAuth for account-touching actions). Walmart, Stripe, and Genesis are among the partners. Version 0.1 was planned for late October 2025.
- **The protocol has notable gaps**: Amazon — the biggest commerce player in the story — is not among the reported partners, and Amazon's block of Muse was intentional. The spec hadn't been published at time of recording. Stripe and Shopify already have competing agentic commerce protocols.
- **Meta's framing**: Turning away a personal agent means turning away the customer behind it. Meta said it would rather work with businesses on underlying concerns than see them lose customers.
- **The security concern is legitimate**: Agents holding a customer's login and payment card are high-value targets; merchants allowing them in take on some of the associated risk. Fraud and credential stuffing are real threats that existing bot-checks were designed to address.
- **Muse's internal "Sentinel" system** governs what the agent itself can touch on the user's side; the new personal agent protocol addresses what the business lets the agent touch on its side — two complementary layers of control.

## Use cases
- **Product managers at e-commerce companies** who need to audit whether their checkout, signup, or booking flows are agent-compatible or accidentally blocking paying customers.
- **Platform and API owners** deciding whether to monetize agent access (like Yelp), rate-limit it, or allow it freely — and needing traffic measurement to make that call.
- **Security and infrastructure teams** who manage bot-management settings and may not realize a vendor default change (like Cloudflare's September 15th update) has become the product's de facto agent policy.
- **Product teams building anything writable by an agent** — sandboxes, configuration settings, note tools — who need to decide what agents can change by default vs. read-only, following the Wikipedia lesson.
- **Companies making public "agent-friendly" statements** who need to verify their bot settings and flows actually match the messaging (the Shopify press-release vs. Amazon bot-settings inconsistency example).
- **Anyone designing failure states**: If your product blocks or fails for agents, the customer still needs to know why and how to complete the task manually without starting over.
- **Product leaders evaluating agent-readiness** before committing to integrations or partnerships — using Tiffany Kitchen's concrete readiness test as a starting framework.

## Patterns & frameworks

**The Accidental Agent Policy Audit**
Pick one critical flow (checkout, signup, booking). Run a real agent (Muse, ChatGPT, etc.) through it. Document every failure point — every CAPTCHA, login wall, mouse-assuming popup. The resulting list *is* your actual agent policy, separate from whatever your terms of service or press releases say. This is the primary action item from the episode.

**Three-Layer Permission Model**
Drawn from the Wikipedia incident and the personal agent protocol: (1) Read access is the default starting point. (2) Write access requires explicit user-granted permission. (3) Actions that combine processing untrusted content + touching sensitive data + changing state should require a human in the loop. Meta built this as an internal rule for Muse; the episode argues it applies in reverse to any product that receives outside agent traffic.

**Intentional vs. Accidental Failure State Design**
A framework for thinking about blocking decisions on a spectrum: Amazon's block is intentional and communicated (pop-up). Adidas's failure was accidental and silent (no message, customer went to social media). The pattern is: whether you block or occasionally fail, *someone must design the failure experience* — what the customer sees, what they can do next, and whether they can complete the task themselves with their session intact.

**Signal vs. Sprint Distinction**
Applied to the personal agent protocol announcement: a new industry standard being announced is a signal about directional trends worth tracking, but version 0.1 not yet published means it's not yet worth building sprints around. The pattern is: evaluate nascent standards for strategic awareness, not immediate execution, especially when key players (Amazon) are absent and competing standards already exist.

**Org Boundary Check**
The bot-management settings that constitute your agent policy are almost certainly owned by security or infrastructure, not product. The framework: proactively have the 30-minute conversation with whoever owns those settings to understand the current defaults and whether any vendor changes (like Cloudflare's) have already changed your policy without a product decision being made.