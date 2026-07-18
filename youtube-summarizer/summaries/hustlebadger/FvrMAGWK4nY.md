# How to Create a Team of Agents with Liam Darmody

Video ID: `FvrMAGWK4nY`

## Summary
Liam Darmody, a product leader based in London, presents his personal AI agent team setup built on Claude Code via his open-source tool Run Doc. Motivated by the birth of his daughter and the need to maintain work output with drastically reduced time, he built a nine-agent team to handle writing, research, admin, and content while he sleeps. The core argument is that the mental model shift from "AI as a tool" to "AI as a managed team" — with named agents, written job descriptions, and delegated responsibilities — unlocks far greater leverage than ad-hoc chat interactions. The talk is most relevant to non-technical product managers and knowledge workers who want to automate and augment their work without living in a terminal.

---

## Key insights
- **The amnesia problem**: Using AI as a chat tool means starting from zero every session — "the most capable intern on their first day, every single day." Persistent, context-aware agents fix this by remembering your work, voice, clients, and standards across sessions.
- **Management is the core skill**: Building an agent team requires the same skills as managing humans — writing job descriptions, delegating, giving feedback, reviewing output. This makes it accessible to PMs and non-technical people.
- **Automation vs. augmentation**: Automation gives time back (briefings run while you sleep); augmentation enables entirely new capabilities. Liam, a non-developer, built Run Doc itself using his Dev and Dez agents — something he couldn't have done alone. He calls this the more important and underappreciated half.
- **Taste becomes the moat**: When agents handle execution, judgment — knowing what "good" looks like — becomes the scarce, valuable skill. Taste was previously unscalable; now you write it down once and the team follows it forever.
- **Writing becomes instruction**: Specs, tickets, and docs now have a second audience: agents who execute on them literally. Agents are "the most unforgiving readers you'll ever have" — vague writing surfaces on the first run. This has made Liam a clearer writer for humans too.
- **The voice profile**: Liam has a ~2,000-word file describing how he writes, plus a banned-words list of nearly 100 terms he never uses. His content agent Pen reads this on every task and filters before he sees a draft — he calls this the single most impactful productivity investment he's made.
- **Nine-agent org chart**: Coz (chief of staff / orchestrator), Pen (content lead with her own sub-agents — analyst and researcher), Leah (calendar and meeting notes), Dev (code), Dez (design), Arlo (AI research), Solo (sales prep), plus Doc (Run Doc guide). One human: Liam.
- **Agent chaining**: Tasks flow from Coz → specialist → back to Coz (specialists can't delegate directly to each other) → next specialist. The demo showed Arlo (research) handing off to Coz who routed to Pen (content) for a multi-step content creation pipeline.
- **Asynchronous tasking via Todoist**: Liam drops tasks into a Todoist agent board from his phone. Coz picks them up, routes to the right specialist (e.g., Arlo), who completes the work and drops a response in comments — no laptop required. Results appear within ~10 minutes.
- **Run Doc vs. Claude Code**: Run Doc is a visual workspace sitting on top of Claude Code, making agent files, skill files, and session search accessible without a terminal. Its key differentiators: visual org chart, searchable conversations (universal search shipped the day before the talk), inline markdown editor with comment/suggestion review, and a UI for non-technical users. Technical users who are comfortable in the terminal don't need it.
- **Specialist vs. generalist agents**: A single generalist agent fills its context window quickly and does many things adequately but nothing exceptionally. Specialist agents hold focused context and skills, allowing each to excel in its domain — analogous to hiring a specialist vs. a generalist employee.
- **VPS for background running**: For routines to run while away from the laptop (morning briefings at 5am, Saturday AI digests, Monday analytics pull), Liam uses a Hostinger VPS with cron jobs. This also preserves his daytime Claude usage windows for real-time interactive work.
- **540+ tests in the codebase**: With Dev writing code, Liam has built a comprehensive test suite through iterative human testing across Mac and Windows, catching regressions across releases — a concrete example of augmentation producing professional-grade output.
- **Total stack cost**: Claude Pro ($20/month), Run Doc (free, open source), Obsidian (free). No code required, no infrastructure expertise needed — roughly the cost of a Netflix subscription.
- **Routines**: Coz runs a morning briefing daily at 5am; Granola end-of-day sync pulls meeting notes and tasks into Todoist; weekly Fathom Analytics digest on Mondays; weekly AI intelligence digest every Saturday morning.
- **Inline comment/review feature**: Newly shipped feature in Run Doc lets users highlight text in a file, add comments, and send them to an agent for replies or inline suggestions — mirroring Google Docs-style collaboration rather than outsourcing entire documents.

---

## Use cases
- **New parents or time-constrained professionals** who need work to continue moving without their full presence.
- **Non-technical product managers** who want Claude Code's power without living in a terminal.
- **Content creators and thought leaders** who publish regularly and want drafts in their own voice without writing from scratch every time.
- **Solo founders or indie builders** who lack design and engineering headcount and want to augment with specialist agents.
- **Anyone doing recurring research** (AI news, competitor tracking, analytics) who wants it synthesized and delivered on a schedule.
- **Meeting-heavy roles** (PMs, consultants) who want automated meeting note processing and task extraction into a task manager.
- **Knowledge workers with chaotic weeks** who need a "chief of staff" to prioritize and brief them each morning.
- **People preparing for sales or client conversations** who want a dedicated agent to prep context and talking points.
- **Teams wanting to systematize voice and standards** — the voice profile + banned words list model applies to any knowledge worker who publishes or communicates regularly.

---

## Patterns & frameworks

**Tool → Team mental model shift**
Stop treating AI as a tool you pick up and put down. Assign names, roles, and written instructions to agents. Manage them the way you'd manage people — delegate, give feedback, write corrections into their instructions. This is the foundational reframe the entire setup depends on.

**Orchestrator + Specialist hierarchy**
Start with one orchestrator agent (chief of staff) who routes work and holds top-level context. Add specialist agents beneath it over time, each with a focused skill set. Specialists cannot delegate to each other — they route back through the orchestrator. This mirrors a real org chart and keeps context windows lean.

**Automation + Augmentation duality**
Automation = work that happens without you (briefings, digests, syncs). Augmentation = new capabilities you couldn't have had alone (building an app as a non-developer). The second is the bigger long-term shift and is underappreciated in most AI productivity conversations.

**Voice Profile + Banned Words List**
A multi-thousand-word document describing how you write, paired with a list of words/phrases you never use. Assigned to your content agent on every task. One-time investment (a weekend to build v1) that permanently raises output quality more than any productivity tool.

**The "new hire" iteration loop**
Build one agent, get it genuinely useful before touching the next. Treat corrections as training: every piece of feedback gets written into the agent's instructions so it stays corrected. This mirrors onboarding a new employee — role definition → job description → training → ongoing coaching.

**Three-agent starter team**
1. Chief of Staff — knows your priorities, runs your week, acts as orchestrator.
2. Executive Assistant — calendar, meeting notes, follow-ups.
3. Content Lead — drafts in your voice once you've documented what your voice is.
Build in this order. Get each working before starting the next.

**Asynchronous task delegation via external tools (Todoist)**
Drop tasks into a shared board (Todoist) from any device. The orchestrator polls the board, routes to the right specialist, who completes the work and responds in comments. Creates a fully async, mobile-friendly delegation loop without requiring the laptop to be open.

**Skill bucketing by agent**
Rather than a flat pool of skills, assign skills to specific agents. This keeps each agent's context focused, makes iterative improvement easier (go to Pen's skills to improve content; go to Dev's skills to improve code), and prevents context window bloat from holding all skills in one agent.

**Lean Agent Team template**
A minimal, pre-built three-agent starter (Chief of Staff, EA, Content Lead) designed to get non-technical users running quickly without wading through large skill packs. Philosophy: one working agent beats nine half-working ones; start small and train up.