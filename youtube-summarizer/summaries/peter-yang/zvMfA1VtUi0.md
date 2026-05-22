# My Honest Review of Google's AI Strategy After I/O

Video ID: `zvMfA1VtUi0`

## Summary
A product manager/tech influencer shares his post-Google I/O assessment of Google's AI strategy, arguing that Google's biggest weakness is a lack of focus — launching too many fragmented AI products instead of winning the three AI races that matter most: personal agents, coding/knowledge work super apps, and multimodal AI. He acknowledges Google's genuine strengths (data, infrastructure, video models) while being critical of product sprawl, overly conservative agent permissions, and failure to consolidate tools. The video is most relevant to PMs, founders, and enterprise tech decision-makers evaluating AI platforms and competitive dynamics.

---

## Key insights
- **Product fragmentation is Google's core problem.** Google launched so many AI products at I/O (Gemini, AI Studio, Anti-Gravity, Spark, Flow, Stitch, Pomelo, etc.) that users — both consumer and enterprise — don't know which tool to use for what.
- **The AI chat era is ending; personal agents are next.** The author estimates the personal agent market at $1 trillion+. Users want AI that *does work*, not just responds in chat.
- **Google has a structural data advantage in personal agents.** Gmail, Google Calendar, Google Docs, and Drive give Google more personal context than any competitor — making the personal agent race "theirs to lose."
- **Spark is Google's personal agent answer**, framed around three pillars: *Personal* (leverages Gmail/Calendar/Drive), *Proactive* (daily brief surfacing what matters), and *Powerful* (executes tasks via Google apps and third-party APIs/MCPs, runs in the cloud on a VM so your laptop doesn't need to stay open).
- **Google is too conservative with agent permissions.** Spark currently asks for user approval on every write action. Competitors like Codex and Claude Code let users bypass permissions entirely. With 900M Gemini users, the caution is understandable, but the author argues Google should let users choose their own permission level.
- **Enterprise coding has shifted to Codex and Claude Code.** AI-native builders moved to Codex (generous rate limits, GPT-5.5) and enterprises to Claude Code (strong hype cycle + enterprise sales). Google is playing catch-up.
- **Gemini 3.5 Flash is a strong model at a competitive price.** Benchmarks show it outperforms Gemini 3.1 Pro and sometimes GPT-5.5, with pricing at $1.50 input / $9 output vs. GPT's $5/$30 and Claude Opus being the most expensive. Cost matters as enterprises hit AI budget limits.
- **Anti-Gravity, Codex, and Claude Code all look nearly identical** — left-nav thread list, agent chat, browser preview. No UI innovation for team/org-level human-agent collaboration.
- **Stitch (design) being separate from Anti-Gravity (coding) is a missed opportunity.** PMs want to plan, design, and build in one tool. Google should consolidate these into a single super app.
- **Google risks losing its Workspace moat.** By adding AI chat piecemeal to Docs, Slides, Sheets, etc., Google is playing defense. The real threat is a single super agent replacing the need to go into those apps at all — which is an existential risk to Google's product portfolio.
- **Google leads clearly in multimodal/video AI.** They're the only US lab with competitive video models, and they own YouTube. Key competitors are xAI and Chinese models (e.g., SeaDance), the latter criticized for copyright issues. Flow is highlighted as Google's best image/video generation product.
- **The Omni model** (any input → any output type, e.g., voice in → video out) is called out as a major capability announcement.
- **Flow is great but unknown.** Despite being Google's best generative media product, most users haven't heard of it because it's siloed as a separate app rather than integrated into Gemini.
- **Family photo/video editing is blocked by safety restrictions**, which the author calls his #1 personal use case — illustrating how safety policies create real consumer friction.
- **Cultural bright spot: Josh Woodward (VP, Gemini Labs/NotebookLM).** He runs on 90–120 day roadmaps only, explicitly avoids 1-year planning theater, and promotes a "build to learn" ethos. His team (including Gemini VP Chris) caps PRDs at one page and runs meetings using live AI prototypes instead of decks.

---

## Use cases
- **Product managers at AI companies** evaluating how to position tools against Google, OpenAI, and Anthropic
- **Enterprise technology leaders** deciding which AI coding or knowledge work platform to standardize on
- **Founders building personal agent products** looking to understand the competitive landscape and key differentiators (permissions model, context access, cloud execution)
- **Google PMs and strategists** looking for external signal on where their product portfolio has gaps or redundancy
- **Investors or analysts** tracking competitive dynamics across the AI platform wars
- **Individual knowledge workers or developers** deciding between Gemini/Spark, Codex, Claude Code, or Hermes for daily productivity and agent use
- **Parents or consumers** frustrated by AI content restrictions around personal/family media

---

## Patterns & frameworks

**The Three AI Races Framework**
The author organizes all of Google's AI efforts into three competitive races that determine who wins the AI platform era:
1. *Chat → Personal Agent*: Moving from reactive Q&A to proactive, task-executing agents with personal context
2. *Coding → Knowledge Work Super App*: Expanding dev-focused tools into a single app for all knowledge work (planning, design, build, write)
3. *Text → Multimodal*: Competing on images, video, voice, and cross-modal generation

**Personal Agent Spectrum (Left to Right)**
A positioning model for the agent landscape:
- *Left*: Open Claw / Hermes — messaging-native, fully customizable, pioneered the category
- *Middle*: Codex / Claude Code — backed by OpenAI/Anthropic, strong coding roots, adding agent features
- *Right*: Google / Gemini / Spark — best personal context (email, calendar, docs), weakest agent autonomy currently

**Personal → Proactive → Powerful (Spark's Product Framework)**
Google's own three-pillar framework for what a personal agent must be:
- *Personal*: Deep integration with the user's data
- *Proactive*: Surfaces insights and priorities without being asked (e.g., daily brief)
- *Powerful*: Executes real actions across apps and third-party APIs

**Velocity over Planning (Labs Culture Model)**
Josh Woodward's operating model for winning in fast-moving AI:
- 90–120 day roadmaps max, no 1-year planning
- "Build to learn" over document-and-deck cycles
- PRDs capped at one page
- Meetings run with live prototypes, not slides
- Prioritize shipping speed over organizational process