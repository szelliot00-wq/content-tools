# Claude Code Has Quietly Evolved (People Haven't Noticed)

Video ID: `4iMZA1omCkM`

## Summary
This video argues that Claude Code's optimal usage patterns have shifted significantly in the past six months — not because the models changed, but because the open-source community has developed frameworks and workflows that fill three major gaps: memory, planning/reasoning, and autonomous task execution. The presenter walks through each gap, explains what Claude Code lacks out of the box, and demonstrates community-built solutions. It is most relevant to power users, product managers, content creators, and small teams who use Claude Code for ongoing, long-term projects rather than one-off tasks.

## Key insights
- **Claude Code's built-in memory is nearly useless for long-term projects.** The default CLAUDE.md file is maintained by hand, conversations are compressed mid-session, and the MEMORY.md index captures almost nothing — the presenter's own index had only 5–10 notes after months of use.
- **Memory has three distinct functions that need separate solutions:** storage (what to capture and keep), short-term injection (pulling relevant context into the active conversation), and long-term recall (finding information later by meaning, not exact keywords).
- **Open-source memory plugins close most of these gaps with minimal setup.** Tools like Memarch, Gbrain (by Gary Tan, suited for multi-user/teams), and Hermes can be installed in one or two commands (e.g., `/plugin marketplace add memarch` then `install memarch`), and they handle all three memory functions on top of Claude's existing infrastructure.
- **Semantic recall is the critical differentiator.** Good memory systems store information by meaning so you can ask "what did we decide about pricing for agency clients?" six months later in plain English and retrieve the answer — even without using the exact original keywords.
- **Claude Code's default planning mode has a context management problem.** Long single-session execution burns context quickly; the community response was to architect explicit file structures (brand voice, positioning docs, project dashboards) called "agentic operating systems" (Agentic OS).
- **Anthropic's answer to planning complexity is the `/effort` setting.** This controls how many reasoning tokens Claude allocates before acting — ranging from low to max/ultra code. Auto mode is the default and handles low-to-medium tasks well, but users should manually dial it up for complex work.
- **Ultra Code is the extreme end of the effort spectrum.** When invoked, Claude writes its own bespoke workflow, spins up a small team of agents, gives each a clean context and a single job, has agents check each other's work (adversarial review pattern), and returns a finished result — removing the need for the human to design the workflow at all.
- **Ultra Code demo: building inbox-scouting skills.** The presenter ran a single prompt asking Claude to build reusable skills that scan Gmail for AI newsletters, score stories against audience ICP, and draft LinkedIn posts and threads in the user's voice. Claude designed a two-skill architecture (tool-gmail + strategic newsletter digest), built both in parallel using separate agents, integrated them, and ran an adversarial convention review — all from one prompt.
- **The `/goal` command enables autonomous run-to-completion.** After each agent turn, a lightweight model (Haiku) checks whether the defined completion conditions have been met. If not, Claude keeps running without handing back to the user — effectively a built-in loop condition.
- **`/routines` (or `/schedule`) pairs with `/goal` for recurring autonomous workflows.** Routines schedule cloud agents on a cron cadence; `/loop` handles local machine loops under 3 days. Together with `/goal`, they let Claude run a task on a recurring schedule and only surface to the human when genuinely stuck or when human judgment is needed (e.g., reviewing a draft before publishing).
- **Full autonomy is explicitly rejected as the goal.** The presenter stresses that human-in-the-loop checkpoints still matter — Claude handles the repetitive grunt work (research, drafting, monitoring), while humans make the important decisions and provide quality control.
- **Context management remains the user's responsibility.** Brand voice, ICP (ideal customer profile), past decisions — none of this is automatically captured. The "agentic OS" context layer is what makes autonomous execution actually useful, and it still requires deliberate human curation.
- **The newsletter digest demo produced one real item scoring 16/22.5** on Claude's self-defined scoring rubric, with two additional derived angles pulled from the same email to meet the "three content ideas" completion condition. Claude also self-suggested adding identified newsletter senders to a YAML file to reduce token usage on future runs.

## Use cases
- **Content creators and marketers** who want to automate research-to-draft pipelines (e.g., daily inbox scan → content angles → LinkedIn posts/threads in brand voice)
- **Teams or agencies** managing long-running client projects where context (brand voice, decisions, positioning) needs to persist across weeks or months
- **Solo operators** who repeat the same workflows daily (inbox triage, social drafting, research summaries) and want to remove themselves from the trigger step
- **Power users building internal tooling** who want Claude to generate and maintain its own skill/tool libraries following consistent conventions
- **Product or operations leads** who need monitoring, daily summaries, or recurring reporting without manual initiation each time
- **Anyone frustrated by Claude "forgetting" past decisions** across sessions or projects — the memory framework section addresses this directly
- **Multi-user teams** where shared memory and cited recall (Gbrain) matters for consistency across team members

## Patterns & frameworks

**Three-function memory model**
Splits memory into: (1) Storage — capturing transcripts and deciding what's worth keeping; (2) Short-term injection — pulling relevant context into the active session dynamically; (3) Long-term recall — semantic search over stored information so you can find things by meaning, not keywords. Used as a diagnostic to evaluate any memory solution.

**Agentic OS (Agentic Operating System)**
A file-structure architecture the community developed to manage context: dedicated files for brand voice, positioning, customer ICP, and ongoing projects, sometimes with a dashboard layer on top. Serves as the persistent context layer that makes autonomous execution coherent and on-brand.

**Effort / `/effort` dial**
Anthropic's built-in control for reasoning token allocation, ranging from low → auto → high → max → ultra code. The rule of thumb: leave it on auto for routine tasks; manually raise it for complex planning or multi-step builds.

**Ultra Code (extreme effort mode)**
When invoked, Claude: (1) writes its own workflow plan for the task, (2) spins up a team of agents each with a focused context and single job, (3) runs agents in parallel where possible, (4) uses adversarial cross-checking between agents, and (5) returns a finished output. Removes the human from workflow design entirely on complex tasks.

**Goal + Routines pairing**
`/goal` defines measurable completion conditions; a lightweight model (Haiku) checks after each turn whether conditions are met and keeps Claude running if not. `/routines` or `/loop` provides the recurring trigger. Together they create fully autonomous, recurring workflows with human checkpoints only at decision or review moments.

**Adversarial convention review (workflow pattern)**
One of six named Ultra Code workflow patterns from Anthropic docs. After agents produce output, a separate agent (or agents) attempts to refute or find gaps in the work before returning results to the user — a built-in quality gate.

**Skill-building via meta-skill creator**
A "skill creator skill" that enforces consistent conventions across all generated skills (trigger phrases, scope, output format). New skills built via Ultra Code inherit these conventions automatically, creating a self-consistent and reusable skill library over time.