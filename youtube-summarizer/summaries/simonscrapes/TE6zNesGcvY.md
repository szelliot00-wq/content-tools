# How to Build an Agentic OS Your Whole Team Can Actually Use

Video ID: `TE6zNesGcvY`

## Summary
This video presents a blueprint for building a team-wide "agentic operating system" (OS) inside Claude Code — a structured set of files and folders that manage AI context for multiple users simultaneously. The core argument is that while solo agentic OSes are straightforward, team versions require solving three hard problems: shared-but-controlled memory, non-technical team member accessibility, and vendor portability. The presenter synthesizes ideas from Gary Tan's GBrain concept with software architecture principles to propose a three-tier storage system (shared drive → Claude Code → GitHub) layered with a four-system access control model. Most relevant to product/ops teams, agency leads, and technical leads managing AI workflows across multiple clients or departments.

## Key insights
- **LLMs have two core limitations** the OS addresses: context rot (degraded performance with too much info at once) and no long-term recall of business context, clients, voice, or decisions — so every conversation starts from zero without an OS.
- **The three-tier storage model** separates files by who maintains them: humans edit in Notion/Google Drive (markdown files), agents edit inside Claude Code (scripts, memory, skills), and GitHub backs up everything for version control.
- **Notion/Google Drive as source of truth** for human-editable files (claude.md global rules, brand context, shared knowledge) because it's where non-technical team members already work and has a clean markdown editing experience.
- **Skills/process documents** live inside Claude Code rather than Notion due to formatting issues with YAML front matter that can cause errors when passing between systems.
- **Private user overrides** are handled via `claude.local.md` files stored only on the individual's machine and git-ignored, allowing personal rule overlays without exposing them to the team.
- **Four-system access control** must be configured separately and kept in sync: (1) Notion/Google Drive per-doc permissions, (2) local machine token-scoped pulls, (3) GitHub repo membership mirroring Notion access, and (4) memory database row-level security.
- **GitHub requires manual permission mirroring** — Notion permissions do not propagate to GitHub automatically. The rule is one repo per client, scoped to exactly the same people who have Notion access to that client.
- **Two memory database architectures** are presented: (a) local per-user vector stores — easy isolation but no shared memory; (b) shared Postgres on Supabase with row-level security filtering queries by user identity — harder to set up but scales across the whole team and enables genuine shared memory.
- **The whole OS is just markdown files and folders**, making it fully portable — no vendor lock-in. The system can be moved from Claude Code to any other AI interface.
- **Project outputs** can be pushed back into Notion for non-technical team members to view (read-only), while remaining managed and version-controlled inside GitHub.
- **Inherited permissions cascade**: Notion is the single source of truth for access, and GitHub membership and memory database permissions must mirror it — controlled by the team owner.

## Use cases
- **Agency or consultancy teams** managing context for multiple clients who need strict data separation (e.g., one client's data must never be accessible to another client's team members).
- **Non-technical team members** (writers, strategists, account managers) who need to contribute to and edit AI context without touching code or GitHub.
- **Team leads or AI infrastructure owners** wanting to give teammates personalized rule overrides while maintaining global shared standards.
- **Ops/product teams** scaling AI-assisted workflows across departments where different teams need different context but share some company-wide knowledge.
- **Teams already using Notion or Google Drive** who want to layer an agentic OS on top of their existing toolstack without migration overhead.
- **Organizations with compliance or confidentiality concerns** around AI memory — the row-level security Postgres model provides an auditable, controlled shared brain.
- **Technical leads** evaluating AI tooling who want to avoid vendor lock-in and build portable infrastructure that survives model/tool transitions.

## Patterns & frameworks

**Three-Tier Storage Model**
Separates file storage by maintenance responsibility: Tier 1 = shared drive (Notion/Google Drive) for human-editable markdown; Tier 2 = Claude Code environment for agent-maintained files (memory, scripts, skills); Tier 3 = GitHub for version control and backup of everything. The rule: edit in the tier appropriate to who owns that file.

**GBrain-Inspired Shared Company Brain**
Borrowed from Gary Tan (Y Combinator), this is the concept of a centrally maintained knowledge base scoped per client/team that any authorized user can query. The adaptation here is implementing it via tiered file permissions rather than a monolithic database.

**Separation of Stable vs. Frequently Changing Content**
A software architecture principle applied to file structure: files that change often (memory, outputs) are kept separate from stable files (brand rules, global claude.md), so updates don't destabilize the whole system.

**Four-System Access Control Stack**
A repeatable pattern for enforcing permissions across: (1) Notion/Google Drive doc-level rights, (2) machine-local token scoping, (3) GitHub repo membership, (4) memory DB row-level security. The key rule: each system's permissions must manually mirror the Notion source of truth — they do not sync automatically.

**Global → Local Override Inheritance**
Global shared rules flow down from Notion into every user's environment. Individual users can layer personal overrides via `claude.local.md` files on their own machine, which are git-ignored and private. This mirrors CSS cascade logic applied to AI context management.

**Dual Memory Architecture Decision**
A named trade-off pattern: choose between (a) isolated local vector stores (simple, no sharing) or (b) shared Postgres with row-level security (complex, scalable). The presenter recommends (b) for teams that need genuine shared memory across clients and teammates.