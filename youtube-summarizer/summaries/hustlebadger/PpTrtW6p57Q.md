# Build Your Personal Operating System in Claude Code with Dave Wascha

Video ID: `PpTrtW6p57Q`

## Summary
Dave Wascha, a veteran CPTO and startup advisor, presents his personal productivity system built entirely in Claude Code without writing a single line of code himself. His core argument is that knowledge workers should stop doing formulaic, repeatable work and instead invest time in designing systems and defining criteria so AI agents can do that work automatically. He walks through a layered framework of tools, skills, roles, tasks, and routines that automates roughly 80–85% of his administrative and consulting workload. The talk is most relevant to product managers, executives, consultants, and independent operators who manage high volumes of communications, client work, and routine deliverables across multiple channels.

## Key insights
- **The core mantra is "don't do work"** — specifically, don't do toil that doesn't require your unique brain, judgment, taste, or experience. The goal is to automate 100% of that work and focus only on what requires you specifically.
- **The nature of knowledge work is shifting** — workers will stop doing work, judging work, analyzing data, and answering questions. Instead, they will define *how* work gets done, define *criteria* by which work is judged, decide *what* gets analyzed, and craft *what questions* get asked of systems.
- **The problem that triggered the system**: Dave was managing ~6 early-stage startups and 6–12 executives simultaneously across half a dozen Slack instances, multiple email accounts, WhatsApp, Notion, Confluence, and more. He was dropping obligations, missing questions, and double-booking meetings. Admin overhead had become his business bottleneck.
- **After implementation**: All communication channels are triaged daily, all commitments extracted from meeting transcripts and added to Todoist automatically, meeting scheduling happens hands-free, and coaching proposals are generated automatically — all without Dave initiating anything manually.
- **No code was written by Dave** — he has viewed approximately 2% of the code running his entire system. Everything was built by describing what he wanted to Claude. The ghost-writing tool, for example, took 15 minutes to build, with 14 of those minutes spent writing the spec.
- **The framework stack (bottom to top)**: Tools & Skills → Roles → Tasks → Routines. Tools are MCP server connectors to external services (Gmail, Trello, file system, etc.). Skills are agent capabilities. Roles are personas that execute specific tasks with specific tool access. Tasks are individual steps. Routines are sequences of tasks.
- **The Ghostwriter role** is a single reusable role called across 10–15 routines that takes any text input and rewrites it in Dave's voice, using 15 years of his actual emails, proposals, and documents as training examples. It accepts a tone/register selector (formal, client-friendly, casual).
- **RLHF self-improvement loop**: The ghostwriter tool shows its proposed response on the left; Dave writes his preferred version on the right; when he hits send, the system compares the two and automatically updates the role's prompt to close the gap. Over time it became so accurate Dave rarely needs to correct it.
- **Anonymizer/De-anonymizer pattern**: Before any content is sent to an LLM, deterministic (non-LLM) code strips out real names of people and companies and replaces them with placeholders (e.g., "Person 1," "Company 1"). After processing, another deterministic script replaces placeholders with real names in the final output. This protects client confidentiality without compromising output quality.
- **The Conductor role** is the master orchestrator — a role that reads routine files, grants tool permissions to sub-roles, executes tasks in sequence or in parallel, manages dependencies, and spawns sub-agents when tasks can run concurrently. It is analogous to the "Mayor" in Steve Yegge's Gasstown framework.
- **Programmatic invocation without API costs**: Dave discovered (via Steve Yegge's Gasstown framework) that Claude Max subscription accounts can be called programmatically without API keys, meaning all automated routines run against a flat ~£200/month subscription rather than per-token API fees. He shared this with a podcaster who had spent £1,500 in tokens on a single newsletter.
- **Three invocation methods**: (1) Interactively during a Claude session, (2) on a timer via system schedulers (Cron on Linux, LaunchD on Mac), and (3) programmatically from scripts or other routines. Example: a routine runs every 5 minutes checking for scheduling emails and books meetings fully autonomously.
- **Coaching proposal routine is fully automated**: A watcher detects a new meeting transcript, classifies it as a prospecting call, spawns parallel agents (Analyst extracts themes from the transcript; Researcher gathers company/sector info), passes results to a Proposal Writer, then to the Ghostwriter, then to a Reviewer that checks all claims trace back to the transcript. The final proposal lands in Dave's inbox ready to forward — with no action required from Dave after the initial call.
- **The Reviewer role** was originally built to catch hallucinations — it verifies every claim in a document can be traced to a source in the transcript. Dave notes this is now rarely triggered, as hallucinations have become far less common with current models.
- **Everything is stored as Markdown text files** — routines, roles, tasks, skills — all interpreted by Claude at runtime. Markdown is preferred over PDF/Word because it uses fewer tokens and LLMs interact with it more efficiently. Obsidian is used as the knowledge base.
- **CRM built entirely in Obsidian by Claude**: Full contact history, meeting transcripts, and timelines stored locally. A "Head Hunter" role can scan the CRM against a job description and return ranked candidates with LinkedIn links automatically.
- **Inter-agent communication tip**: Rather than passing full context windows between agents (which wastes tokens), agents should write outputs to shared text files and have other agents read from those files. This is more reliable and efficient than direct inter-agent communication.
- **Token optimization strategies**: Keep context windows short and clear them regularly; avoid leaving irrelevant information in the context window; use lightweight fast models (Haiku/Flash) for simple tasks and reserve reasoning models for complex tasks; be especially careful with browser/Playwright plugins that generate hundreds of screenshots per session.
- **Shelf life of custom-built solutions is shrinking rapidly**: Dave built a mobile-to-terminal-session tool; it was superseded by the community's "Happy" framework within 2 weeks, then by Anthropic's native "Remote" feature shortly after. The lesson: build to solve today's problem, but expect features to be absorbed by platforms quickly.
- **Presentations built in HTML**: Dave uses a Slide Outline role (outputs YAML) fed into a Slide Building role that produces HTML presentations with animations. He demoed a fully animated step-by-step diagram of his coaching proposal routine built in a single 90-second prompt with no refinement.
- **Claude.md for coding standards**: Dave instructed Claude to research global software engineering best practices and write its own coding standards into a `claude.md` file — so all code generated adheres to professional architecture and security practices without Dave specifying them each time.
- **Privacy note**: Despite having an Anthropic enterprise agreement with a no-training clause, Dave still uses the anonymizer for client data integrity reasons. He acknowledges this may be overkill but it's already built and causes no friction.

## Use cases
- **Independent consultants or advisors** managing multiple clients simultaneously who need to avoid dropping obligations and commitments
- **Executives with high communication volume** across Slack, WhatsApp, email, and other channels who need triage and drafting assistance
- **Product managers** automating formulaic deliverables: PRDs, competitive analyses, proposals, meeting summaries, and stakeholder updates
- **Coaches and mentors** who need session prep, context recall across multiple clients, and automated note-taking with commitment tracking
- **Due diligence professionals** (VC, M&A) who conduct structured assessments repeatedly and need a repeatable, automated workflow from scheduling through final report
- **Anyone scheduling meetings** across multiple time zones or with many clients — the scheduling routine runs every 5 minutes, handles negotiation, and books without human involvement
- **People managing a personal CRM** who want automated relationship tracking, meeting history, and candidate matching against job descriptions
- **Business development** — automating personalized outreach at scale ("mail merge on steroids")
- **Content creators or newsletter writers** who want to reduce token API costs by using subscription accounts programmatically
- **Anyone building personal software** to fit their exact workflow without paying for or compromising on off-the-shelf SaaS tools

## Patterns & frameworks

**Tools → Skills → Roles → Tasks → Routines (The Automation Stack)**
A layered mental model for designing automated workflows. Tools are connectors to external services (MCP servers). Skills are discrete agent capabilities. Roles are personas with defined tool access and a specific purpose. Tasks are individual steps executed by a role. Routines are ordered sequences of tasks, run automatically or on demand. This mirrors patterns in OpenClaw, Agent Flywheel, and other agentic frameworks.

**The Conductor Pattern**
A master orchestrator role that sits above all other roles. It reads routine definition files, assigns tool permissions to sub-roles, manages sequencing and parallelism, and spawns sub-agents. Analogous to the "Mayor" in Steve Yegge's Gasstown framework. The key insight is that all other automation flows through this single entry point.

**RLHF Self-Improvement Loop (Reinforcement Learning with Human Feedback)**
Applied to the Ghostwriter role: the system proposes a response; the user writes their preferred version; the system diffs the two and automatically updates its own prompt. Over many iterations the model's output converges to the user's actual voice with no manual prompt engineering. Applicable to any role where subjective quality improves with repeated human correction.

**Anonymizer / De-Anonymizer Pattern**
A privacy-preserving pipeline pattern: deterministic code strips identifying information before LLM processing (replacing names with placeholders stored in a dictionary), LLM performs all analysis on anonymized content, then deterministic code re-inserts real names in the final output. Protects client confidentiality without degrading output quality or requiring a local LLM.

**The "Don't Do Work" Principle**
A meta-framework for deciding what to automate: if a task does not require *your* specific judgment, taste, or experience, it should be automated. Corollary: you should also not build the automation yourself — Claude should build it. The human's role shifts to writing specs, defining criteria, and designing systems.

**Parallel Agent Spawning for Independent Sub-Tasks**
When a routine contains tasks that don't depend on each other (e.g., Analyst extracting themes and Researcher gathering company data), spawn them as parallel sub-agents with their own context windows to reduce total processing time. Each returns only its result (not its full context window) to the conductor, ideally by writing to a shared text file.

**Shared Text File Inter-Agent Communication**
Rather than passing context windows between agents directly (expensive and fragile), agents write their outputs to shared text files. Other agents read from those files. This is more token-efficient, more reliable, and easier to debug than direct inter-agent messaging.

**Model Tiering for Cost/Quality Optimization**
Match model capability to task complexity: use lightweight fast models (Haiku, Flash) for simple, high-frequency tasks (triage, scheduling checks, classification); reserve reasoning-heavy models (Opus 4.7) for tasks requiring complex judgment (theme extraction, proposal drafting, architecture review). This keeps subscription-based usage within limits while maintaining quality where it matters.

**Gasstown (White Collar Edition)**
Dave's adaptation of Steve Yegge's Gasstown framework — originally designed for massively parallel multi-agent software development — applied to personal productivity and knowledge work automation. The core transfer: use programmatic subscription-based Claude invocation (no API keys) to run multiple automated routines in parallel against a flat monthly fee.