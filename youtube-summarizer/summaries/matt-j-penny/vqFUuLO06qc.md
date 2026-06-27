# How To Automate 90% of Your Marketing With Hermes Agent

Video ID: `vqFUuLO06qc`

## Summary
The creator (Matt) demonstrates how he uses Hermes, an autonomous AI agent framework, to automate the majority of his marketing operations across YouTube, email newsletters, social media, and analytics tracking. The core argument is that Hermes outperforms tools like Claude Desktop because it runs autonomously on a VPS (no computer required), is model-agnostic, and keeps all data in-house to enable a compounding marketing flywheel. The video is a practical walkthrough of a real system, not a theoretical exercise, and is most relevant to solo creators, small business owners, and marketers who produce consistent content and want to scale output without sacrificing quality.

## Key insights
- **Why Hermes over Claude**: Hermes runs autonomously on a VPS (no need for a local machine to be on), supports multiple AI models simultaneously (e.g., Claude for writing, GPT for slides), is shareable across team members, and keeps all data owner-controlled.
- **Human-in-the-loop is intentional**: Matt explicitly avoids full automation on steps like script review, thumbnail selection, and newsletter approval — because AI-only output produces worse results in those steps. He frames this as a deliberate choice, not a limitation.
- **YouTube ideation uses vidIQ MCP**: Hermes connects to the vidIQ database to scan YouTube for videos that outperformed their channel's average in the last 1–2 weeks (recency-filtered to stay relevant, especially in fast-moving AI content).
- **Research pipeline uses Open Notebook (open-source NotebookLM)**: Hermes scrapes YouTube videos, X posts, blog posts, and other sources, loads them into Open Notebook, then uses RAG to draft scripts in Matt's voice — pulling from his past content, opinions, and case studies.
- **Slides are built with a custom front-end skill**: A purpose-built Hermes skill reads the script and generates slides matching Matt's brand (purple color scheme, logo, fonts), which he then reviews and adjusts manually.
- **Video editing is semi-automated via a "pre-editor"**: Before sending footage to HyperFrames, Matt uses a custom pre-editor to cut filler words and bad takes, apply motion graphics/b-roll templates, and set editing style — dramatically speeding up the HyperFrames output.
- **Publish prep skill automates YouTube metadata**: Strips audio from the final video, transcribes it, checks for bad cuts, writes the video description, generates chapter timestamps, and sets up custom link tracking.
- **Two types of email newsletters**: (1) Daily AI news — Hermes surfaces stories, Matt ranks them by business relevance, Hermes drafts and sends to MailerLite automatically, then asks Matt for approval. (2) New mastermind content — Hermes monitors a database for new additions, drafts an email in Matt's voice explaining the content and its business application.
- **"The Syndicator" tool**: A custom Hermes tool that takes a long-form YouTube video or livestream and repurposes it into LinkedIn posts, carousel slides, X posts, X clips, X articles, YouTube Shorts, and Instagram content — all automatically.
- **Original social posts use a "last 30 days" skill**: Hermes identifies trending AI topics from the past 30 days, combines them with Matt's voice and existing content (via Open Notebook), drafts posts, and Matt approves before posting.
- **Tracking is the underrated pillar**: Matt's most-viewed video (400k+ views) generated only ~$700, while a 32k-view video drove thousands in revenue. Without custom link tracking on every click, he would have misallocated content effort based on vanity metrics.
- **The marketing flywheel**: Because all data lives on the VPS, Hermes can analyze what converts, feed that back into ideation, and continuously improve content quality and targeting over time.
- **Thumbnails are not Hermes-native**: Matt maintains an inspiration library of proven thumbnails and uses ChatGPT's image model (via the website, not Hermes) to adapt them to his style — the final pick is manual.

## Use cases
- **Solo content creators** who publish regularly and want to 10x output without hiring a team.
- **Small business owners** who run their own marketing and need an autonomous system that works while they sleep.
- **Marketing agency owners** managing multiple clients who need model-agnostic, data-controlled automation per client.
- **Newsletter operators** who curate news or content updates and want to automate drafting while maintaining editorial control.
- **Anyone repurposing long-form content** into short-form social formats across multiple platforms simultaneously.
- **Marketers who want attribution clarity** — anyone currently optimizing for views/engagement without knowing which content actually drives revenue.
- **Teams** where multiple people need access to the same AI marketing system (Hermes is shareable; Claude Desktop is not).

## Patterns & frameworks

**The Marketing Flywheel**
All data lives on the owner's VPS. The more content Hermes creates, the more performance data accumulates. That data feeds back into ideation (what to create next), improving targeting and conversion rates over time. The system compounds rather than plateaus.

**Human-in-the-loop by design**
Matt uses a deliberate rule: automate steps where AI output equals or exceeds human output; keep humans in the loop where AI output is worse. Applied practically — AI handles research, drafting, metadata, and distribution; humans handle judgment calls (script accuracy, newsletter tone, thumbnail selection, final approvals).

**The Four-Pillar Marketing Stack**
1. YouTube (top of funnel — ideation → research → script → slides → record → edit → publish prep)
2. Email newsletter (mid-funnel conversion — news digest + mastermind content updates)
3. Social media (syndication of long-form + original trend-based posts)
4. Tracking (revenue attribution loop that feeds back into content strategy)

**Recency-filtered ideation**
When scanning for YouTube video ideas, Hermes filters to the last 1–2 weeks only — avoiding stale topics that no longer reflect audience interest, especially critical in fast-moving niches like AI.

**The Syndicator Pattern**
One long-form asset → many short-form outputs. A single video becomes LinkedIn posts, carousels, X clips, Shorts, and articles automatically. Maximizes the return on the highest-effort content unit (the long-form video).

**Revenue-per-view attribution (not views as a proxy)**
Rather than treating view count as a success metric, Matt tracks custom links on every piece of content to measure actual revenue generated. This reframes content strategy around conversion efficiency, not reach.