# Creating Your Own Agentic OS is Easy (Insanely Powerful)

Video ID: `w0S-khYCaB4`

## Summary
This video presents a step-by-step guide to building an "Agentic OS" — a structured file and context management system that sits underneath AI tools like Claude Code to dramatically improve output quality and consistency. The core argument is that the difference between users who get great results and those who don't isn't prompting skill, but whether they've built a supporting system that tells the AI who you are, what you've done, and how to work. The framework addresses nine specific limitations of out-of-the-box LLMs, covering identity, memory, skills, workflows, planning, multi-client management, output organization, and remote access. It is most relevant to freelancers, agency owners, product managers, and knowledge workers who use AI tools daily and want repeatable, high-quality outputs at scale.

---

## Key Insights

- **The core problem is context management, not prompting.** Out-of-the-box LLMs start every session from zero. Users who get better results have built a file/folder structure that injects the right context at the right time — not better prompts.

- **An Agentic OS is just clever folder and file organization.** No coding required. If you can organize a Notion workspace, you can build this. It is entirely based on markdown files and folder structures.

- **Static context has two layers:**
  - **User identity file** (user.md / soul.md / claude.md depending on the tool) — defines who you are, how you work, and how the AI should respond. Best created by letting AI interview you with ~15 questions rather than writing from scratch.
  - **Brand context folder** — contains brand voice, ICP (ideal customer profile), positioning, and messaging examples. Claimed to 3x–10x output quality for knowledge work. Stored in a shared location so all skills pull from one source.

- **Different tools use different names for the same identity file:** Claude Code uses `claude.md`, Codex/others use `agents.md`, OpenClaw uses `soul.md` — but the function is identical (injected into the system prompt at session start).

- **Context rot is a real and critical problem.** The more context pushed into a conversation window, the worse recall becomes. This makes it effectively impossible to run ongoing projects without a dedicated memory system.

- **Memory systems have six levels** (from a separate video the presenter made):
  - Level 1: Native `claude.md` / static rules (built-in but Claude doesn't have to follow)
  - Level 2: Session start hook — deterministically forces project context to load every session
  - Level 3: Semantic search (e.g., mem search, claude.mem) — searches by meaning across stored notes, pulls relevant memory into context
  - Level 4: Verbatim/word-for-word recall (e.g., Mem Palace) — useful for client work where exact phrasing matters
  - Level 5: Knowledge bases
  - Level 6: Cross-tool shared memory (across devices and different LLMs)
  - **The 80/20 recommendation is layers 1+2+3 combined**, which is sufficient for most users.

- **Skills should be short, modular, and under 200 lines.** Claude reliably recalls up to ~200 lines of instruction. Skills use "progressive disclosure" — load name/description first, then full file only when needed, then additional examples only when required in a specific step. This prevents bloating the context window.

- **Skills should always reference shared brand context.** A copywriting skill shouldn't guess your brand voice — it should pull directly from the shared brand context folder. Same for research skills pulling from ICP/positioning files.

- **Self-learning skills** can be built by including a step that reads a `learnings.md` feedback file before executing, and asks for feedback after each run. This creates a continuous improvement loop.

- **Skills should be chained into "skill systems" (pipelines), not used in isolation.** Example: a scheduled task runs topic research → script writing → content creation → human review loop → posting. This is where real time savings come from, not single skill use.

- **A transcription skill is a good example of modularity** — it can be reused inside short-form video creation, newsletter generation, blog article generation, and more, without rebuilding it each time.

- **Four levels of planning are recommended:**
  - Level 1: Built-in shift+tab planning mode in Claude Code (simple tasks only; breaks down for complex, multi-hour projects)
  - Level 2: PRD-style project planning (half-day to multi-day scope, files with checkboxes)
  - Level 3: GSD (Get Stuff Done) framework — lightweight metaprompting that breaks complex tasks into Plan → Execute → Verify phases to combat context rot
  - Level 4: (Implied) custom frameworks for highly complex builds like full SaaS applications

- **Multi-client architecture uses context inheritance from parent folders in Claude Code:**
  - Root folder has a master `claude.md` with shared methodology and skills
  - Individual client subfolders each have their own `claude.md` that overrides/conflicts with parent instructions where needed
  - Each client folder has its own brand context, agent context, memory, and learnings — fully isolated
  - Skills are kept at root level with a working copy synced to client folders for customization

- **Outputs should be stored in one predictable folder structure** organized by project → skill → type. Without this, Claude Code and similar tools scatter outputs across the terminal window and random subdirectories. The suggested structure: `projects/[client]/[skill or brief]/[output files]`.

- **Remote access has two components:**
  1. Host the system on a VPS or cloud server (not your laptop) so scheduled tasks run 24/7 without your machine being on
  2. Use Anthropic's built-in channels feature to message the system via Telegram or Discord from your phone, with full access to the underlying file structure

- **The architecture is tool-agnostic and portable.** The underlying folder/file structure remains valid even as specific AI tools evolve. OpenClaw, Codex, and Hermes are all moving toward similar native features.

---

## Use Cases

- **Freelancers and agency owners** managing multiple clients who need clean separation of context, brand voice, and outputs per client
- **Content creators** who want automated pipelines for topic research → scripting → repurposing → posting without manual intervention between steps
- **Product managers and builders** working on complex SaaS projects who need structured planning that doesn't degrade over multi-hour or multi-day sessions
- **Knowledge workers** producing recurring deliverables (reports, proposals, briefs) who want consistent, brand-aligned outputs without re-explaining context every session
- **Solo operators** who want AI to run scheduled autonomous tasks (SEO, social content, ad monitoring) while they are away from their laptop
- **Teams or individuals using Claude Code daily** who are frustrated by generic outputs, forgotten context, or outputs saved in random locations
- **Consultants doing client work** where exact phrasing and recalled decisions matter across weeks or months of engagement
- **Anyone evaluating off-the-shelf Agentic OS products** (like Agentic Academy) who wants to understand what's inside them before buying or building

---

## Patterns & Frameworks

**1. Agentic OS (the overarching framework)**
A folder/file system layered beneath any AI tool that manages context — who you are, what you've done, how you work, and how to execute — across nine dimensions: identity, brand context, memory, skills, skill systems/chaining, planning levels, multi-client architecture, predictable outputs, and remote access.

**2. Static Context (two-layer identity system)**
- *User.md* — captures the human user's working style, preferences, and non-negotiables
- *Soul.md / Personality.md* — defines the agent's responding persona
- *Brand context folder* — shared, centrally updated repository of brand voice, ICP, and positioning; pulled by any skill that needs it
- Stays constant; updated rarely

**3. Six-Level Memory Framework**
A tiered model for memory management from static rules (Level 1) to cross-tool shared memory (Level 6). The 80/20 implementation is Levels 1+2+3: static files + session start hooks + semantic search (e.g., claude.mem / mem search).

**4. Session Start Hook (Level 2 memory)**
A deterministic trigger that forces specific context (e.g., business context, brand voice) into the conversation window at the start of every session, regardless of whether the LLM would otherwise choose to read it. Solves the unreliability of relying on `claude.md` instructions alone.

**5. Progressive Disclosure (skill design pattern)**
Skills are structured in layers: name + description load first (so Claude knows when to use them), then the full instruction file, then supplementary examples only when needed at specific steps. Keeps context window lean while maintaining full capability.

**6. Skill Systems / Skill Chaining**
Individual modular skills (each under 200 lines, single-purpose) are chained together into end-to-end automated pipelines called skill systems. An orchestrator meta-skill sequences skill A → skill B → skill C, with optional human-in-the-loop review steps between them. Example pipeline: topic research → script writing → content creation → review → publish.

**7. Self-Learning Skill Loop**
Each skill includes a step to read a `learnings.md` feedback file before executing, and a step to request user feedback after completing. Feedback is written back to the file. On next run, the skill starts with that accumulated knowledge, creating a continuous improvement loop.

**8. GSD (Get Stuff Done) Framework**
A lightweight context-engineering / metaprompting approach for complex tasks. Operates in three phases: **Plan** (break project into phases) → **Execute** (run each phase) → **Verify** (validate completion). Designed specifically to combat context rot on long-running projects by injecting only the relevant phase context at the right time.

**9. Context Inheritance (multi-client architecture)**
Uses Claude Code's native parent-folder context inheritance. A root `claude.md` holds shared methodology. Client-level `claude.md` files override or extend the parent. Brand context, memory, and learnings are isolated per client. Skills live at root and sync working copies to client folders. Enables unlimited clients without cross-contamination of context.

**10. Predictable Output Folder Structure**
A defined folder hierarchy: `projects/[client or project name]/[skill name or brief]/[output file]`. Enforces consistent output location regardless of which skill or skill system runs, making all AI-generated artifacts immediately findable and organized.