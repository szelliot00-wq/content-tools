# Create Your Own Personal Claude AI System (That Makes Your Work EASY)

Video ID: `IevmGCVo9Pw`

## Summary
This video walks through building a personal "operating system" on top of Claude Code/Claude Desktop that adapts to your specific voice, brand, workflows, and clients. The core argument is that out-of-the-box Claude is a generalist, and the way to dramatically improve output quality is to inject the right context at the right time through a structured folder architecture. The presenter demonstrates building this system live, covering global instructions, memory, brand context, skills, workstations, and client management. It is most relevant to solo operators, freelancers, content creators, and small teams who use Claude regularly for writing, analysis, or visual content production.

---

## Key insights
- **The core mechanism is context injection**: Everything in the system — files, folders, skills — exists to load the right information into Claude at the right moment. Better architecture = better outputs, not smarter prompting in the moment.
- **`claude.md` is the master instruction file**: It loads into every conversation automatically and tells Claude how to behave globally — be concise, give one best recommendation, flag uncertainty, use your voice, and know which folder/client it's operating within.
- **`memory.md` acts as short-term persistent memory**: Claude is instructed (via `claude.md`) to always read this file, let it shape responses silently, and write to it whenever the user says "remember this." It tracks active projects, key contacts, and decisions, with a last-updated timestamp to keep it fresh.
- **Brand context breaks into three files**:
  - *Voice profile*: How you sound — extractable from LinkedIn posts, emails, blog posts, or newsletters.
  - *ICP & positioning*: Who you target, what you stand for, what you're against, and what differentiates you.
  - *Visual identity / design tokens*: Color palette, fonts, usage rules — can be auto-scraped from a website URL.
- **Skills are the highest-leverage concept**: Skills are process documents (markdown files) that guide Claude through a repeatable multi-step task to produce a consistent output. The presenter has pre-built skills for generating the voice profile, ICP, and design tokens. Any task done more than twice should become a skill.
- **Skills can be invoked via slash commands** (e.g., `/voice-profile`) or triggered automatically based on the task description matching the skill's description.
- **Workstations separate context by function**: Each workstation (e.g., content, finance, ops) lives in a subfolder and has its own `claude.md` and `memory.md` with rules specific to that function. Global rules from the parent `claude.md` are inherited automatically — no need to repeat them.
- **Routing map in the global `claude.md`**: A table tells Claude which workstation to load based on the task. Adding a new workstation just means asking Claude to set it up — it follows the instructions already in `claude.md` and creates all necessary files automatically.
- **Client management mirrors the workstation structure**: Each client (e.g., "Acme Corp") gets its own nested folder with its own brand context, memory, workstations, and project folders. Brand context is not inherited across folders — it must be local to wherever you're working.
- **Claude Code (code view) vs. Claude.ai Co-work (co-work view) behave differently**: Co-work cannot traverse up the folder tree to access parent-level brand context files. Code view can. This is a real limitation — the workaround in co-work is copying brand context files into each subfolder, at the cost of manual sync when files change.
- **Projects folder stores all outputs**: Each workstation has a projects subfolder where Claude saves dated output files (e.g., `post.md`). Alternatively, a single global projects folder can aggregate all outputs, but this requires the code view.
- **Dispatch enables mobile use**: The Claude mobile app can send tasks to a running desktop instance via the Dispatch feature. Limitation: it won't have automatic access to the full folder context without explicit specification.
- **Single `memory.md` has scalability limits**: As projects and clients grow, one file becomes unwieldy. The presenter acknowledges this and notes that more sophisticated memory architecture is needed for larger operations.
- **The 90% goal**: The explicit target of the system is to get Claude to a 90% complete, on-brand result without extensive back-and-forth — not perfection, but consistent, usable first drafts.
- **Starter templates and skills are provided** as downloadable zips (linked in the video description), including the base `claude.md`, `memory.md`, and three starter skills.

---

## Use cases
- **Solo content creators** who produce LinkedIn posts, carousels, newsletters, or blog content regularly and want consistent brand voice without re-prompting each time.
- **Freelancers managing multiple clients** who need isolated brand context, memory, and project folders per client without cross-contamination.
- **Small business owners** who want to separate operational domains (finance, marketing, ops) so each area has tailored rules and context.
- **Teams or individuals repurposing content** — e.g., turning video transcripts into blog posts, meeting notes into action items, or long-form writing into social posts.
- **Anyone producing visual assets** (slides, carousels, graphics) who wants Claude to apply consistent colors, fonts, and style rules automatically.
- **Knowledge workers making frequent decisions** who want Claude to remember those decisions across sessions without re-explaining context each time.
- **People frustrated with generic AI outputs** — "AI slop" — who want production-ready results that sound like them.

---

## Patterns & frameworks

**Personal Operating System (Life OS / Work OS)**
A top-level folder structure that serves as the root of the entire system. Everything else is nested inside it. The folder itself is connected to Claude as the working directory, making all files accessible as context.

**Parent Inheritance Model**
Global rules (`claude.md` at root) cascade down to all subfolders. Workstations and client folders inherit global rules but can add their own local rules. Brand context files (voice profile, ICP, design tokens) do *not* inherit — they must be present in the active working folder.

**The Three-Layer Context Stack**
1. `claude.md` — *How* Claude should behave (global instructions, tone, format, routing)
2. `memory.md` — *What* Claude should remember (decisions, projects, contacts, updated continuously)
3. Brand context folder — *Who* Claude is speaking as/for (voice, audience, visual identity)

**Skills as Process Documents**
A skill is a markdown file that defines a repeatable multi-step process for a specific output. It includes steps, rules for each step, and expected output format/location. Skills are stored globally and accessible across all workstations. They can be invoked via slash commands or triggered by task description matching.

**Workstation Pattern**
Each functional domain (content, finance, ops) gets its own subfolder containing a local `claude.md`, `memory.md`, and resources folder. This keeps context lean — finance doesn't need voice profile rules; content doesn't need accounting rules. Switching workstations means switching the active folder in Claude.

**Client Isolation Pattern**
Each client mirrors the workstation structure but also includes its own brand context (voice, ICP, visual identity). Clients are nested under a `/clients/` folder. This prevents client context from bleeding across engagements.

**Routing Map**
A table inside the global `claude.md` that maps task types to workstations. When a new workstation is created, Claude adds it to this table automatically, enabling intent-based routing without manual folder switching.

**Skill-First Scaling Principle**
The presenter's explicit recommendation: once a system is set up, the highest-leverage next step is building out skill documents for every recurring task. Skills are what move outputs from "decent generalist" to "production-ready specialist."