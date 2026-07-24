# obsidian second brains suck, actually...

Video ID: `NGGt0-Q8jrw`

## Summary
The video argues that Obsidian-based "second brains" are fundamentally unsuitable for business use, despite their popularity in the AI productivity space. The creator — who claims to have helped 2,800+ businesses apply AI — contends that markdown files, graph views, and backlink systems are solutions optimized for the wrong problems. He proposes Notion as a dramatically superior alternative and introduces a two-type data framework (static vs. dynamic) as the real foundation for deploying AI effectively in a business. The video is most relevant to business owners, AI consultants, and operators who are considering or already using knowledge management tools to support AI agents.

## Key insights
- **Zero businesses benefited from Obsidian second brains** out of 2,800+ in the creator's communities — he positions this as empirical, not theoretical
- **Markdown is optimized for agents, not humans** — it's plain text, efficient, and readable by AI, but lacks rich formatting, images, embedded media, and databases that humans need to actually use and update the knowledge base
- **Humans still matter** — most businesses have team members who don't use AI or aren't AI-friendly, and forcing them to interact with raw markdown files creates real friction and adoption failure
- **The graph view achieves nothing practical** — it looks visually impressive but provides no actionable value; it's described as "dangerous" because it creates an illusion of productivity
- **Backlinks (LLM wiki style) are the wrong model for business knowledge** — backlinks work well for unstructured, web-like knowledge (e.g., Wikipedia, the internet) where you don't know where information lives. Business knowledge is structured more like a book with chapters and subchapters, making hierarchical search far more efficient
- **Obsidian sync is a serious operational problem** — even paid Obsidian Sync only reliably handles two devices (desktop + phone). AI agents running on VPS instances, Claude, or other remote systems can't connect to it. The creator's workaround (GitHub + 5-minute cron sync) is brittle and time-consuming
- **Notion token efficiency myth is false** — a live test comparing a 1,000-word document in markdown vs. Notion showed Notion was actually *cheaper* by 98 characters, disproving the common claim that Notion uses 5x more tokens
- **Notion advantages over Obsidian**: rich content (images, video, HTML, GIFs), stores anything, instant seamless sync across all devices and team members, connects easily to any AI agent, and supports hierarchical search
- **Two types of business knowledge require different storage approaches**: static knowledge goes in a context/knowledge base (e.g., Notion); dynamic data connects via live integrations (MCPs, APIs, CLIs)
- **Voice-based AI interviews extract richer business context** — spending ~30 minutes letting an AI interview you about your business via voice produces far more complete and useful context than typing, because it enables follow-up questions and more natural information flow

## Use cases
- A solo founder or small team wanting to give AI agents accurate, persistent context about their business (products, pricing, customers, SOPs)
- An AI consultant setting up knowledge infrastructure for a client's business
- A business owner whose team members vary in AI literacy — needs a knowledge base humans and AI can both use without friction
- Anyone running AI agents on remote infrastructure (VPS, cloud) who needs those agents to access up-to-date business knowledge
- A business with dynamic operational data (sales pipeline, ad spend, inventory) needing live AI integration rather than static snapshots
- Someone who built an Obsidian second brain and is hitting sync, collaboration, or adoption problems
- An AI agency operator needing to onboard AI systems quickly with rich business context

## Patterns & frameworks

**Static vs. Dynamic Data Framework**
The core operational model of the video. All business knowledge splits into two types:
- *Static data*: rarely changes — SOPs, processes, brand guidelines, case studies, product info, customer profiles. Store in a knowledge base (Notion recommended) and feed as context to AI agents.
- *Dynamic data*: changes constantly — sales data, ad spend, pipeline status, inventory. Do NOT store in a knowledge base; connect directly to AI agents via MCPs, APIs, CLIs, or connectors so agents always access live data.

**Applied AI Process (4-Step)**
A framework the creator teaches in his mastermind (details not fully disclosed in this video) for taking a business from "knows about AI tools" to "has a real AI system with processes and automations." Positioned as strategy-first, not tool-first.

**AI Business Interview / Context Extraction**
A repeatable process for bootstrapping a business knowledge base: feed a structured prompt to Claude (covering identity, offerings, customers, markets, people, operations, etc.), then have it interview you about your business *via voice* for ~30 minutes. The output becomes the static context fed to all AI agents, eliminating the need to re-explain business context on every prompt.

**Structured (Tree) vs. Unstructured (Graph) Knowledge Model**
A mental model for choosing how to organize information:
- Graph/backlink model suits unstructured, web-like knowledge where location is unknown (Wikipedia, the internet)
- Tree/hierarchical model suits structured business knowledge where you know the category and can drill down (Sales > SOPs > Objection Handling)
Business knowledge maps to the tree model, making Notion's hierarchical structure more appropriate than Obsidian's backlink graph.