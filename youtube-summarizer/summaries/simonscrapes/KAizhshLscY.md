# How to Get So Good At Claude it Feels Like Cheating

Video ID: `KAizhshLscY`

## Summary
This video presents a five-layer framework for progressively automating knowledge work using Claude, arguing that most people learn AI features without ever genuinely delegating work to AI. The presenter's core claim is that productivity gains come not from mastering individual features but from stacking layers: prompting → projects → skills → scheduled automation → an agentic operating system. Each layer builds on the previous, and skipping the foundations (especially prompt quality) limits how far you can go. The content is most relevant to freelancers, consultants, content creators, and small business owners who want to do more work in the same number of hours.

## Key insights
- **Prescribing step-by-step instructions in prompts actually hurts output quality** — Anthropic's own guidance says models perform better when given the whole job upfront and allowed to determine their own approach.
- **A well-formed prompt has five components:** goal + task context, what "done" looks like, a self-validation check, what's out of scope, and guard rails (what it cannot touch).
- **The validation check is the most commonly omitted element** — giving Claude a way to verify its own work (e.g., "every question must link to a real, provable result") significantly improves reliability.
- **Projects solve the context re-entry problem** — instead of re-explaining your business, voice, and goals every conversation, project-level files provide persistent context across all chats in that project.
- **One project per set of context, not one per task** — the right question is "would these two jobs need the same files?" If yes, same project. If voice or client differs, separate project.
- **Connected files via MCP beat uploaded files** — an uploaded file goes stale immediately; a connected Google Doc is always live, and teams sharing that doc all get the latest version automatically.
- **Skills should only encode fixes Claude can't get right out of the box** — the workflow is: do the job once, correct it, log every correction, then filter: corrections about you/your business → project context; generic AI failure patterns (e.g., clichéd openings) → an existing ready-made skill; job-specific failures → your custom skill.
- **Never build a skill from scratch** — derive it from actual corrections made during real work, then layer in examples (e.g., two pages that already rank in AI search) so Claude can reverse-engineer why they worked.
- **Test every skill against no skill using Claude's built-in eval inside the skill creator** — an untested skill may be doing nothing at all.
- **Layer four adds autonomy via scheduled tasks** — a brief (4 lines is enough: find opportunity, draft with skill, save to folder, don't publish) plus a trigger and a destination is all that's needed.
- **Scheduled tasks can be triggered by time OR by events** — a new lead entering a CRM can fire an API call that starts the task immediately, rather than waiting for the next scheduled window.
- **Never fully automate high-risk outputs** — anything involving money, complaints, legal matters, or first-time public communications under your name should always require human review before going out.
- **Layer five (Agentic OS) is a plain-folder system that removes dependency on any single AI app** — it's a standardized markdown folder structure (you folder, brand folder, processes/skills folder, memory folder, per-client folders) that works identically in Claude Code, Codex, Cursor, or any tool.
- **Memory in an Agentic OS persists across tools and clients** — unlike Claude project memory (which is siloed to one project in one app), an OS-level memory folder is portable, readable, editable, and isolated per client.
- **Multi-client use case: one copy of each skill, separate client folders** — a correction made for one client propagates to all others because skills are shared, while client-specific voice and data stay isolated.

## Use cases
- **Content creators and SEO professionals** identifying AI search opportunities, drafting pages, and automating weekly content audits
- **Freelancers managing multiple clients** who need isolated context (voice, data, rules) per client but shared skill improvements across all of them
- **Consultants or agency owners** who want AI to do first drafts, research, and reports while they sleep, ready for review in the morning
- **Solo operators or small teams** doing repetitive knowledge work (email drafts, SEO analysis, reporting) who want to reclaim hours without hiring
- **Teams collaborating on AI workflows** where a shared Google Doc (via MCP) keeps everyone's AI context synchronized without manual updates
- **Anyone currently re-typing the same context** into every AI conversation — the project layer directly solves this
- **Power users who want model/tool portability** and don't want to be locked into the Anthropic ecosystem if a better model emerges

## Patterns & frameworks

**The Five-Layer Stack**
A progressive autonomy model: (1) Chat/Prompting → (2) Projects → (3) Skills → (4) Scheduled Automation → (5) Agentic OS. Each layer depends on the one below it; getting layer one wrong caps how effective every subsequent layer can be.

**The Five-Part Prompt Structure**
A repeatable formula for any task prompt: goal + context, definition of done, self-validation check, out-of-scope declaration, guard rails. The validation check and guard rails are the two elements most commonly omitted.

**The Skill Derivation Workflow**
Do the job → correct it → log every correction → sort corrections into three buckets (project context / existing ready-made skill / custom skill) → add examples → test with eval vs. no skill. Skills are never written from scratch; they're distilled from real corrections.

**One Project Per Set of Context (not per task)**
A decision rule for project organization: ask "would these two jobs need the same files?" Same files = same project. Different voice or client = different project.

**The Agentic OS Architecture**
A portable, plain-markdown folder system structured as: `/you` (how you work), `/brand` (voice, positioning, audience), `/processes` (one skill file per job type, each with its own brief and validation), `/memory` (persistent correction log), `/clients` (one subfolder per client with isolated context). The same folder works across any AI tool.

**Risk-Tiered Automation**
A mental model for deciding what to automate fully vs. what always needs human review: automate drafts and research freely; always require approval for anything involving money, legal exposure, complaints, or first-time public-facing output under your name.