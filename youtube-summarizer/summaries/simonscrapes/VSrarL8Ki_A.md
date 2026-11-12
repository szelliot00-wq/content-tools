# n8n’s New Agent BEATS Dots, Muse & Grok Bot

Video ID: `VSrarL8Ki_A`

## Summary
This video reviews **Nod**, a new personal AI agent from n8n Labs, comparing it against competitors Dots, Muse, Grok Bot, and Claude Duet. The presenter (sponsored by n8n but self-described as honest) argues that Nod differentiates itself through data ownership, model choice flexibility, open-source transparency, and a robust security/trust model. It is most relevant to power users, freelancers, and small business operators who want an autonomous agent to handle multi-step tasks across email, calendars, payments, and third-party apps without ceding control of their data to a cloud provider.

## Key insights
- **Model flexibility**: Nod lets users choose their LLM — Claude (via API key), ChatGPT (via Plus/Pro subscription), any model via OpenRouter, or even a locally-hosted model. Most competitors lock you to their own model (e.g. Claude Duet only uses Anthropic models).
- **Runs on your own machine**: Unlike Grok Bot (cloud computer) or other cloud-first agents, Nod's default compute is the user's own computer, preserving data ownership. A self-hosted server option also exists for 24/7 operation.
- **225 app integrations via Composio**: Out-of-the-box OAuth connections to 225 apps, including the ability to connect **multiple accounts of the same app** (e.g. four separate email inboxes) — a gap the presenter identified in competing agents.
- **Proactive task suggestions**: Within minutes of setup, Nod scanned the presenter's inbox and calendar and suggested a weekly routine for drafting email replies — addressing the common friction of users not knowing what to delegate to an agent.
- **WhatsApp and Telegram support**: Nod bridges desktop and mobile via WhatsApp/Telegram, maintaining one continuous long-running conversation across devices.
- **Security and payment controls**: Every payment requires the user's card security code, which Nod never stores. A vault handles logins and card details, entering them directly into websites without exposing them to the model.
- **Seven documented trust principles**: n8n published explicit trust principles (data ownership, open by default, model choice, etc.) that users can vet — grounded in n8n's enterprise automation track record.
- **Memory system scored 93.2% on LongMem eval**: Tested with 500 questions about months of prior chats in a fresh session, recalling 93.2% correctly.
- **Memory is sourced only from the user's own words**: When storing a memory, a separate memory model writes notes that must quote something the user actually said — preventing injection of false facts from external sources (e.g. malicious emails).
- **Attack resistance**: 216 email-based memory injection attacks against Nod failed 100% of the time. The same attack succeeded 87.5% of the time against Open Claw for comparison.
- **Memory housekeeping worker**: A background job runs every hour to archive outdated or duplicate memories rather than delete them.
- **Self-building skills**: After complex multi-step tasks, Nod writes a "how-to" for future reference (personal details stripped), similar to how Hermes builds skills from conversation history.
- **Task execution test**: Given a vague prompt to find an Apify scraper for SEO/AI search agency leads, Nod independently read the RankSpot website, searched Apify, compared scrapers, and selected the top-rated one (clutch.so scraper, 1,200 users, 4.6 rating) — pausing to request approval before incurring costs.
- **Comparable to Grok Bot on agentic tasks**: Both agents chose the same scraper independently, suggesting Nod has reached parity with one of the market leaders on autonomous task execution.
- **Geographic availability advantage**: Dots Pro excludes UK, Switzerland, and EEA; Claude Duet is US-only with a waitlist; Muse is US-only rollout. Nod works in the UK because it runs locally.
- **Open source**: Full codebase is publicly available, enabling community contributions and user customization beyond what competitors offer.
- **Monthly spending limit**: Users can set a hard cap on monthly LLM/tool spend, with per-task cost visibility.
- **Two noted weaknesses**: (1) No separate conversation threads — all topics live in one long chat; (2) No visible thinking/reasoning logs during task execution, leaving users uncertain about progress. Both are considered likely to be addressed soon given the active GitHub repo (1,000+ commits).

## Use cases
- Freelancers or small business owners managing multiple email inboxes who need automated triage and draft replies
- Anyone who needs to chase unpaid invoices, cancel subscriptions, or request refunds without manual multi-step workflows
- Researchers or sales teams wanting automated lead generation (e.g. scraping directories for agency prospects)
- Users in regions excluded from other personal agents (UK, EEA, Switzerland)
- Privacy-conscious users who want an agent that runs on their own hardware, not a third-party cloud
- Developers or power users who want to customize the agent's behavior via its open-source codebase
- People running locally-hosted LLMs who want a personal agent interface around them
- Users managing bookings, scheduling, or Slack/comms catch-up across many accounts and logins

## Patterns & frameworks

**Trust Principles Framework**
n8n's seven documented trust principles (data ownership, open by default, model choice, etc.) serve as a verifiable contract between the agent and the user. Rather than implicit promises, users can read and vet the principles to decide if they align with their values before granting the agent access to sensitive accounts and finances.

**Vault Pattern (Credential Isolation)**
Logins and card details are stored in a secure vault that types credentials directly into target websites without exposing them to the LLM. This separates authentication from the model layer, so the agent can act on your behalf without the model ever "seeing" your passwords or card numbers.

**Quote-Anchored Memory**
Every memory note must cite a direct quote from the user's own messages. This anchors memory to verified first-person statements, making it resistant to prompt injection via external content (emails, documents) trying to plant false facts.

**Skill Self-Building (Post-Task How-To)**
After completing a complex task, Nod auto-generates a reusable "how-to" with personal details stripped. This creates an evolving personal knowledge base of task procedures, reducing future effort on similar jobs — a pattern also seen in Hermes agents.

**Permission Checkpointing**
Rather than running autonomously to completion, Nod pauses at consequential decision points (spending money, running a paid scraper) to request explicit user approval. This "ask before acting on cost/risk" pattern is embedded at the infrastructure level, not left to model judgment.