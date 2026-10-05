# How to Use AI to Survive (and Even Enjoy) Meetings | Sam Stephenson

Video ID: `3IF3H5dxU3U`

## Summary
This video is a product demo and conversation between Peter (the host) and Sam Stephenson, co-founder of Granola — an AI meeting tool now valued at $1.5 billion. Sam walks through how he personally uses Granola beyond basic note-taking (pre-meeting briefs, post-meeting analysis, context-aware drafting), and how Granola operates internally as an AI-native company. The core argument is that AI tools should reduce cognitive load and create calm rather than add chaos, and that shipping fast internally with quality guardrails (design systems, internal agents) is the right model for AI-native teams. Most relevant to PMs, founders, designers, and anyone building AI-native products or workflows.

---

## Key insights
- **Pre-meeting briefs are Granola's most personally valued feature for Sam** — they surface key context about a new candidate or contact in the chaotic moments between back-to-back meetings, saving him from embarrassment when underprepared.
- **"What did I miss" is the most-used recipe on Granola** — users cook it constantly, particularly when multitasking or zoning out during meetings. Granola is exploring productizing it as a hover-over tooltip on the live transcript indicator.
- **Meetings represent the richest, most up-to-date context a company has** — day-to-day meeting transcripts accumulate granular details about projects, people, and company health that high-level docs don't capture. Sam uses this to identify projects going off the rails or things not getting enough attention.
- **Post-meeting "postmatch analysis" recipes** — investors and sales teams use Granola after calls to ask: "What did I miss? What should I have asked? How could I have gone deeper?" With history of prior calls, it gives increasingly smart answers.
- **Granola is evolving from a meeting tool into a contextual company knowledge platform** — the accumulated transcript corpus enables company-wide queries (e.g., "What are customers saying?") across shared team spaces with sales calls, standups, and design critiques.
- **MCP integration is enabling power users to build personal workflows** — Sam himself uses the Granola MCP combined with other sources (Google Docs, etc.) to receive a weekly email summary. The pattern: ingest everything into one context, then query across it.
- **The core design principle is "calm"** — Granola is designed for the most chaotic moment of a knowledge worker's day (between back-to-back meetings). Every design decision is tested against: does this lower your blood pressure or raise it?
- **The transcript is intentionally hidden** — a deliberately aggressive design decision that generates complaints but keeps the user present with the other person rather than staring at a scrolling transcript. Granola is the "handwriting," not the main character.
- **Figma usage has dropped to ~20%** — the design workflow has shifted from Figma-dominant to whiteboard sketches → code prototypes, especially for interactive or data-driven features like pre-meeting briefs where real personal data matters more than polished mocks.
- **Design systems enable non-designers to ship quality UI** — Granola rebuilt on a token/component-based design system in February, making it possible for engineers and agents to produce decent-looking UI without design review for most features.
- **"Nacho" is Granola's internal AI agent** — started as a weekend project, connected to Slack, Granola, Amplitude, logs, and website analytics. It handles incident investigation, SQL queries, data pulls, and can spin up Cursor agents to write PRs. No one owns it; incentives drive everyone to improve it.
- **AI agents for meetings is the next frontier** — Sam's "ultimate feature request" is personal agents (a Peter-agent and a Sam-agent) that meet first to align, only escalating to the humans if they can't. CEOs are already asking for this as a first-line-of-defense from repetitive questions.
- **Context-switching between agent threads is a new productivity problem** — Sam notes that managing multiple concurrent coding agent threads is more cognitively exhausting than meeting context-switching, something Granola is thinking about.
- **Ship internally fast, but hold a high quality bar before broad release** — Granola had a working (ugly) brief feature in the app within 1–1.5 weeks of starting. Internal dogfooding creates pain that motivates quality. But the bar for external release is: does this person get daily value?
- **The hard problem is still knowing what to build** — AI makes building easy; the thinking, space, and judgment to know *what* to build remains irreducibly human and comes from rest and reflection, not grinding.

---

## Use cases
- **Busy knowledge workers** in back-to-back meeting schedules who need context fast and want to stay present during calls.
- **Recruiters and hiring managers** running structured interviews who want to assess candidate answers against a rubric in real time.
- **Sales teams** doing post-call analysis to improve pitch quality and learn from call history.
- **Founders and CEOs** who want a first-line agent to handle repetitive inbound questions before they escalate.
- **Product and engineering teams** building AI-native tools who need a principled approach to quality when everyone is shipping code.
- **Designers** navigating the shift away from Figma-first workflows toward code prototypes and whiteboard-to-cursor pipelines.
- **Enterprise teams** needing Granola to integrate with internal tooling (CRM, Slack, internal agents) rather than stay siloed in its own UI.
- **Solopreneurs and power users** who want to combine Granola context with other sources (Google Docs, email) via MCP for unified AI assistants.
- **Ops and data teams** who want natural-language access to company metrics, logs, and customer call insights without building dedicated dashboards.

---

## Patterns & frameworks

**The "Calm First" Design Principle**
Every feature decision is evaluated against a single emotional target: does this make the user feel calmer? The test case is the chaotic in-between moment between back-to-back meetings — stressed, late, underprepared. If a feature adds to that chaos rather than reducing it, it doesn't ship.

**The "Handwriting" Metaphor**
Granola should be like handwriting in your life — supportive, in the background, not the main character. You are the main character; Granola is a quiet tool that makes you better. Used to keep the team humble and resist feature bloat that makes the tool feel prominent.

**Pre / During / Post Meeting Workflow**
A three-phase model Sam uses consistently:
- *Pre:* Brief with relevant context on who you're meeting (pulled from emails, past notes)
- *During:* Auto-notes + "what did I miss" recipe for recovery from distraction
- *Post:* Postmatch analysis recipes ("what should I have asked?", action item extraction, drafting follow-ups)

**Corpus-as-Context Platform**
Meetings accumulate a uniquely rich, granular corpus of company knowledge. The pattern: ingest everything → share selectively into team spaces → query across the full corpus with chat or recipes. Distinct from a wiki (static, maintained) — this is live, automatic, and searchable.

**Ship Ugly Internally, High Bar Externally**
Get a shitty end-to-end working version into the app within days. Let internal users feel the pain of it being bad — that creates intrinsic motivation to fix it. But before releasing externally, hold to: does the person get daily value? Not just: did we ship?

**Design System as Agent-Compatible Infrastructure**
Rebuild UI on tokens and components not just for human engineers but for coding agents. The design system becomes the shared language that allows anyone (human or AI) to produce consistent UI without design review on every PR. Reduces design as a bottleneck without sacrificing coherence.

**Internal Agent Hub (Nacho Model)**
Build a single internal chatbot connected to as many data sources as possible (logs, analytics, Slack, CRM, docs). No dedicated owner — community incentives drive improvements. The agent handles first-pass investigation, data queries, and can spin up code agents for fixes. Low bar to add new tools; high reward for making it more useful.