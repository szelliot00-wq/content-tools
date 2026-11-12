# Fable 5.2 + Opus 5.5 Just Became a Superpower

Video ID: `fAkm3YQg73s`

## Summary
This video by a Claude Code power user (500+ hours) covers when to use Fable 5.2 vs. Opus 5.5 inside Claude Code, illustrated through five real-world use cases from their own work and personal life. The core argument is that Opus is the better daily driver for most execution tasks (email, calendar, app building), while Fable should be reserved for high-stakes strategic work, complex debugging, and deeply personal decisions. The presenter demonstrates each use case with live demos, sharing actual prompts and workflows. The video is most relevant to knowledge workers, PMs, indie hackers, and anyone building personal AI-powered workflows with Claude Code.

---

## Key insights
- **Simple rule for model selection:** Opus for daily execution tasks; Fable for hardest, most important, or most complex work. Even most Anthropic employees use Fable on medium effort, not max.
- **Cost tradeoff is real:** On the Max plan, Fable is available for up to half your weekly limit. On the API, Fable costs 2× per token vs. Opus — so using Fable for everything is wasteful.
- **Four tips for using Fable effectively (from Anthropic's Alex):**
  1. Ask Fable what's wrong with your idea *before* it builds anything.
  2. Start on medium or high effort — extra-high and max are rarely necessary.
  3. Tell Fable upfront what requires your approval vs. what it can do autonomously.
  4. Give it a whole project, not a single next step — it can reason and work for a long time.
- **Chief of staff workflow uses Opus**, not Fable, because inbox/calendar triage is straightforward execution. It runs on a scheduled task at 7am and 4pm daily.
- **Advisor workflow uses Fable** because career and life decisions are high-stakes. The key differentiator is grounding advice in a personal plan document (goals, principles, energy sources) rather than giving AI zero context.
- **Fable found 30 bugs** in a mature personal app that had already been reviewed with Opus — suggesting that upgrading to a new model and re-auditing existing codebases is a high-value habit.
- **Podcast production workflow** (using Opus) covers: interview prep, editing instructions, sizzle reels, thumbnails, show notes, newsletters, and social clips — all built as individual skills chained together.
- **Suno MCP integration** lets the presenter generate custom music for sizzle reels directly inside Claude Code without visiting suno.com — both for podcast intros and app marketing videos.
- **Claude Design (`/design` command)** is now part of Claude Code and generates a visual canvas of all app screens, enabling direct copy edits on mocks before pushing to code.
- **Personal Video Review app** was built by the presenter to solve a specific friction point: giving Claude timestamped feedback on video edits. The lesson: if Claude lacks a capability you need, build a personal app to fill that gap.
- **F-Cancer skill** creates a one-page medical brief (patient info, doctors, next steps, care log, clinical trials) for a loved one going through cancer treatment. Fable is used here because the stakes are highest. The skill is free on the presenter's GitHub.
- **Prompt audit technique** (`claude-api prompt-audit`) mines all past conversations (149 sessions in the example) to find *repetitive* feedback patterns and suggests skill improvements — avoiding the overfitting problem of improving from a single conversation. The presenter reviews exact copy edits before accepting, to prevent "AI slop."
- **Personal plan document** is the foundation of the advisor use case — it includes 3-year goals, annual goals, guiding principles, and what gives/drains energy. The presenter notes that optimizing for revenue without enjoyment is a trap they learned from experience.
- Fable's honest advisor output told the presenter: their 2026 goals are on track but 2027 subscriber growth is behind pace, paid course completion rates suggest a product-market fit problem, and their "work should feel like play" mindset has become a rationalization for lack of focus — illustrating Fable's willingness to be blunt when prompted.

---

## Use cases
- **Inbox and calendar management** — daily email triage, drafting replies for review, scheduling meetings, running twice-daily briefings via scheduled tasks
- **Career and life strategy** — getting personalized, blunt long-term advice grounded in a written personal plan
- **Content production workflows** — podcast episode production end-to-end: prep, editing, sizzle reels, show notes, newsletters, social posts
- **Personal app development** — building, iterating, and debugging mobile apps (fitness tracker example); designing UI variations via `/design`
- **App marketing** — generating sizzle reels and AI-composed music for product launches
- **Caregiving coordination** — tracking a loved one's illness, managing medical information, researching clinical trials, preparing doctor visit questions
- **Skill/workflow improvement** — auditing all past Claude conversations to surface recurring feedback and incrementally improve personal skills and prompts
- **Bug auditing** — running Fable on existing codebases to find issues Opus may have missed

---

## Patterns & frameworks

**Fable vs. Opus decision rule**
A simple two-tier model selection heuristic: use Opus as the default for execution-heavy, repetitive, or lower-stakes tasks (email, calendar, building, standard workflows); switch to Fable for strategic, complex, high-stakes, or deeply personal work. Driven primarily by cost-to-value tradeoff.

**Chief of Staff setup**
A scheduled Claude Code skill that connects to Gmail and Google Calendar, runs at fixed times (7am/4pm), returns a prioritized numbered list of urgent items, and accepts numbered replies to take action. Pairs human review with AI drafting before sending anything externally.

**Advisor + Personal Plan document**
An advisor skill powered by a canonical personal plan doc (goals, principles, energy map). Grounds AI advice in stable context rather than relying on memory or in-session context alone. The prompt explicitly requests bluntness and asks for observations the user hasn't noticed about themselves.

**Skill-per-phase workflow automation**
Breaking a complex recurring workflow (e.g., podcast production) into discrete phases, each with its own Claude Code skill. Skills can be chained and called sequentially. Enables partial automation of multi-step processes while keeping humans in the loop at review points.

**Build-your-own-tool pattern**
When Claude lacks a native interface for a specific task (e.g., timestamped video feedback), build a lightweight personal app to fill the gap. The app doesn't need to be polished — it only needs to serve you.

**New-model audit habit**
Whenever a more capable model is released, re-run audits on existing codebases, skills, and workflows. Fable's 30-bug discovery on a maintained app illustrates the value of not assuming previous passes were exhaustive.

**Prompt audit (`claude-api prompt-audit`)**
A meta-skill that analyzes all past Claude conversations touching a specific skill area, identifies *repetitive* manual feedback patterns across sessions, and proposes exact copy-level edits to skills. The presenter reviews and accepts/rejects each suggestion manually to maintain quality and avoid AI slop.

**F-Cancer caregiving brief**
A structured one-page living document (patient info, contacts, next steps, medical terms, clinical trial candidates, care log) that centralizes illness management and prepares caregivers for high-value, time-limited doctor interactions.