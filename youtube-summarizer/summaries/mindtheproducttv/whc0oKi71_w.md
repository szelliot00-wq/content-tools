# ChatGPT now lets businesses build their own AI agent. Here's how it works

Video ID: `whc0oKi71_w`

## Summary
OpenAI launched a beta called "Businesses in ChatGPT" on November 10, 2025, allowing businesses to claim verified profiles and build branded AI agents that converse with customers directly inside ChatGPT. The video argues this represents a fundamental shift in how customers first encounter brands — moving the initial product conversation away from your website and into third-party AI platforms. Host Mike Belsito, from Mind the Product, frames this primarily as a product management challenge, not just a marketing one, covering the mechanics of the feature, its significant gaps, the emerging ads business model, and what product teams should do right now. It is most relevant to product managers, e-commerce operators, and digital marketers navigating AI-driven distribution channels.

## Key insights
- **Businesses in ChatGPT has three components**: a business hub (profile + verification), analytics/insights, and the agent itself — all currently free, though OpenAI has not ruled out charging later
- **Verification requires** a text/phone call to your main business number or a DNS record addition; editing details or publishing an agent also requires a government-issued ID
- **Shopify merchants get a direct integration** via "Shopify catalog," allowing live product feeds with current pricing and availability to flow into the agent automatically
- **Agents operate within guardrails**: they can't give advice requiring a professional license, can't automate high-stakes decisions without human review, and all purchases/bookings/form submissions require explicit user authorization via an approved feature
- **ChatGPT has 1.2 billion weekly active users** as of the video — the scale of the potential audience is enormous
- **The ads business is real and growing**: Digiday reported ChatGPT's ad business hit ~$1 billion ARR by late August 2025; sponsored placements appear in ~26% of responses shown to free and go-tier users
- **Sponsored agents** (announced September 16, 2025) let businesses pay to make their agent the destination for a ChatGPT ad click — this beta extends that concept
- **Analytics are limited and murky**: businesses see mentions, clicks, and "discovery topics" (common themes in conversations citing your site) but do NOT see individual chat transcripts, not even with their own agent; small data is hidden below an undisclosed threshold; clicks don't confirm actual visits or conversions
- **Major open questions at launch**: no published dispute process for two parties claiming the same business, no data export from the hub, no stated data retention policy, no published pricing for sponsored agents, and no clarity on whether sponsoring improves organic mention frequency
- **No human handoff exists**: if the agent can't help, there is no escalation path to a live person — a significant product gap
- **The blue checkmark signals ownership verification, not content accuracy** — OpenAI explicitly says it does not verify every detail a business submits
- **Reddit launched Reddit Reviews the same day** — AI-organized summaries of Reddit discussions about ~10,000 products, explicitly non-pay-to-play, contrasting sharply with ChatGPT's monetization model
- **Legal risk is real**: a 2024 Canadian tribunal ordered Air Canada to refund a customer misled by its own chatbot; "the AI said it" is not a viable legal defense when an agent speaks for your business
- **Attribution problem**: if a customer chats with your ChatGPT agent and buys on your site two days later, your analytics won't connect those events — the funnel has a blind spot
- **Distribution is splitting into two types**: places you can pay to appear (ChatGPT ads, sponsored agents) and places you can only earn (Reddit reviews, word of mouth) — product teams are generally better at the first than the second

## Use cases
- **E-commerce product managers** deciding whether to build and maintain a ChatGPT business agent
- **Support/CX teams** worried about consistency between an on-site chatbot and a ChatGPT agent saying different things about return policies or shipping times
- **Marketing teams** evaluating ChatGPT as an ad channel and understanding what sponsored agents cost/deliver
- **B2B SaaS product teams** who can't yet launch an agent but want to audit what ChatGPT is currently saying about their product
- **Legal/compliance teams** assessing liability when an AI agent makes promises about pricing, availability, or policy
- **Anyone managing a product catalog** who needs to decide whether their pricing, documentation, and policies are machine-readable and up to date
- **Small business owners** evaluating whether claiming a free profile now is worth the ongoing maintenance burden
- **Product leaders** who need to decide internal ownership — who at the company is responsible for how AI describes their product

## Patterns & frameworks

**The Five-Question Audit**
A repeatable, low-cost exercise: open ChatGPT and ask five questions a real customer would ask before buying — what does the product do, what does it cost, how does it compare to alternatives, does it work with existing tools, what do people complain about. Write down every wrong, outdated, or missing answer. Repeat on a recurring basis because model outputs change over time. Functions as an ongoing AI presence health check.

**Paid vs. Earned Distribution Split**
A mental model for categorizing distribution channels: "places you can pay to be present" (ChatGPT sponsored agents, ads) vs. "places you can only earn it" (Reddit Reviews, organic word of mouth). Product teams are typically stronger at paid; earned requires building something people genuinely want to talk about. Useful for prioritizing where to invest time and budget.

**Agent as Product Experience (not a Marketing Asset)**
The idea that a business agent is a customer-facing product with a job, limits, and legal accountability — not just an ad unit to hand off to whoever owns the ad budget. Requires product involvement to define what the agent can promise, what it says when it doesn't know, and when/how it escalates to a human.

**Source-of-Truth Portability**
Keep your product catalog, pricing, policies, and facts clean and in a format you control and can export — don't let any single platform (including ChatGPT) become the only place that data lives, especially since OpenAI has no described data export mechanism. The same clean data should be feedable to any future platform that offers similar capabilities.

**The Cross-Team 30-Minute Audit Meeting**
A tactical framework: gather product, support, marketing, and legal stakeholders, put the five-question ChatGPT audit on screen, identify what's wrong, assign ownership for fixing it, and decide who would own an agent if you built one. Low time investment, high alignment value.