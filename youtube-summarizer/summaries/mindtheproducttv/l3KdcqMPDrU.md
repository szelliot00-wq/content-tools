# AI agents have gone mainstream

Video ID: `l3KdcqMPDrU`

## Summary
This episode of "Now Shipping" features host Mike Belceto interviewing Dan Olsen (author of *The Lean Product Playbook*) about the mainstreaming of AI agents as of mid-2026. The conversation centers on the competitive landscape of agentic AI tools — Claude Co-work, Gemini Spark, OpenClaw, and Microsoft Copilot Co-work — and what the shift toward agentic workflows means for product managers. Dan argues that as building becomes faster and cheaper, the bottleneck shifts to product judgment, making strong PM skills *more* valuable, not less. The episode is most relevant to product managers, UX designers, and knowledge workers trying to stay current with AI tooling.

## Key insights
- **The agentic arms race:** OpenClaw pioneered agentic AI but required significant technical skill. Claude Co-work was Anthropic's more accessible response, iterating rapidly from December through April with frequent releases to reach feature parity. Gemini Spark is Google's equivalent entry, and Microsoft launched Copilot Co-work integrated into Microsoft 365.
- **Google IO as a turning point:** Google was widely seen as behind in AI (embarrassing Bard demos, etc.), but Gemini 2.5 Pro helped them catch up, and Google IO's breadth of announcements — Gemini Spark, Google Stitch (vibe design), Anti-Gravity IDE, relaunched Search — signaled they are now a serious competitor.
- **Gemini Spark's differentiator:** It runs on dedicated cloud virtual machines, meaning it operates 24/7 without requiring the user's laptop to be on, awake, and connected to Wi-Fi — a real limitation of Claude Co-work's desktop-bound model. Dan shared a personal story of a scheduled task failing because his hotel laptop wasn't on Wi-Fi.
- **Personal vs. work positioning:** Claude Co-work is positioned around work/enterprise use cases; Gemini Spark is pitched as a "personal AI agent." This mirrors Google's need to protect its broad B2C base against generative AI displacing Google Search.
- **MCP adoption:** MCP (Model Context Protocol) has surpassed 97 million installs. Dan notes Anthropic has simplified the language — calling them "connectors" (Gmail connector, Google Drive connector) — but warns that official connectors aren't always fully featured (e.g., the official Gmail connector couldn't create filters, forcing a pivot to the raw Gmail API).
- **The "last mile problem":** Dan references Box CEO Aaron Levie's "AI psychosis" tweet — leaders demo AI getting 80% of the way there and get excited, but the final 20% (reliability, edge cases, QA) still requires time and often some technical skill.
- **The bottleneck is shifting to PM:** Andrew Ng and others have noted that as engineering productivity rises (like a factory line becoming faster), the constraint moves upstream. The backlog was historically filled to keep engineers busy; now the question becomes "what should we build?" — a PM problem.
- **Design is getting squeezed:** Vibe design tools (Claude Design leveraging Opus 4.7's visual capabilities, Google Stitch, Canva AI) are making it easier to skip or shortcut professional UX design, which Dan views as a risk to product quality.
- **Vertical agents emerging:** Anthropic is launching pre-built vertical agents (financial analyst agent, small business accounting/invoicing agents) so users don't have to configure from scratch — a pattern likely to expand category by category.
- **AI prototyping as an unlock:** Dan frames vibe coding for PMs primarily as "AI prototyping" — going from a PRD to an interactive, iterable prototype without needing a designer or developer. Less than 5–10% of PMs in his workshops report having sufficient design resources to prototype ideas, so this is a major unblock.
- **Type 1 vs. Type 2 work:** Dan's personal framework for AI-assisted productivity — use agents to reduce Type 1 (busy/grunt work) so you can spend more time on Type 2 (thinking/strategic work).
- **Learning is now imperative, not optional:** Dan argues that continuous AI tool learning has shifted from "nice to have" to career-critical for PMs. He recommends YouTube as a fast, free way to stay current, in addition to newsletters and hands-on workshops.

## Use cases
- **PMs without design resources** who want to prototype ideas before engineering investment — vibe coding tools like Lovable (non-technical PMs) or Cursor (technical PMs) can generate testable prototypes from a PRD.
- **Knowledge workers automating repetitive tasks** — Claude Co-work scheduled tasks, inbox management scripts, research-to-spreadsheet workflows (Dan's example: auto-researching restaurants in a new city).
- **Enterprise teams on Microsoft 365** — Microsoft Copilot Co-work integrates Claude's agentic capabilities into OneDrive/365, making it accessible without leaving existing Microsoft infrastructure.
- **Product leaders evaluating AI tool strategy** — deciding which agentic platform to standardize on (Claude Co-work vs. Gemini Spark vs. Microsoft Copilot Co-work) based on deployment model (desktop vs. cloud), ecosystem fit, and use case (personal vs. work).
- **Companies rethinking their product's AI/agent compatibility** — ensuring products expose APIs or MCP-compatible connectors so they work well when agents orchestrate tasks across apps ("agent-friendly" product design, the 2026 equivalent of SEO).
- **PMs and leaders advocating for proper staffing ratios** — using the "bottleneck shift" argument to justify more PM headcount as engineering velocity increases.
- **Workshop/training organizers** — Dan's observation that carving out structured time is the main value of a workshop, because self-directed learning rarely happens given day-job pressures.

## Patterns & frameworks

**Type 1 / Type 2 Work**
Dan's two-bucket model for knowledge work: Type 1 = busy/grunt work (scheduling, formatting, inbox management, research aggregation); Type 2 = thinking work (strategy, product judgment, customer insight). The goal of AI agents is to reduce Type 1 time so more energy flows to Type 2.

**The Vibe Coding Spectrum**
Dan's categorization of AI-assisted building tools by user type and interface — non-technical PMs (Lovable), technical users (Cursor/IDEs), CLI tools, desktop apps, plugins. He notes that tool categories have converged: every major player now wants an IDE surface. Useful for recommending the right tool based on user profile rather than defaulting to one size fits all.

**Problem Space vs. Solution Space**
A classic lean product framework Dan applies to the AI era: vibe coding makes it dangerously easy to rush into solution space (building) before properly defining and validating the problem space. Faster building amplifies this risk. Strong PMs must actively resist the pull toward solution space.

**Build → Feedback → Iterate Flywheel**
The standard product loop, but Dan emphasizes it should speed up — not be skipped — in the AI era. AI accelerates the *build* phase, but the feedback and iteration steps require human judgment and cannot be speedrun. Teams that compress all three loops (not just build) will out-learn competitors.

**The Factory Line / Bottleneck Model (referencing *The Goal*)**
Borrowed from Eliyahu Goldratt's constraint theory: a production line moves at the speed of its bottleneck. Historically in software, engineering was the bottleneck (keep the backlog full). As AI makes engineering faster, the bottleneck shifts upstream to product management — what to build, for whom, and why. Implication: invest in PM capacity and quality as a strategic priority.

**AI Prototyping as Discovery**
Reframing vibe coding not as "building product" but as "prototyping for discovery" — generating a clickable, demonstrable concept from a PRD to gather user feedback before committing engineering resources. This is positioned as a complement to, not replacement for, traditional discovery methods.

**Product Sense / Product Taste**
Emerging terms (relatively new as of 2026) capturing the judgment dimension of PM work — the ability to discern what will create real customer value versus what merely seems buildable. Dan argues this becomes the primary differentiator when building anything is cheap and fast.