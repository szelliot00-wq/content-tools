# I Rebuilt Hermes in Claude Code (It’s Ridiculously Good)

Video ID: `wdc1OFWDxlU`

## Summary
The creator explores Hermes (an agentic AI framework that reached 40,000 GitHub stars in 46 days) but instead of installing it, rebuilds its core features inside a custom Claude Code setup. The video's central argument is that off-the-shelf agent frameworks are faster to start but slower to scale, because you inherit their architectural assumptions and can't fix what you don't understand. The creator walks through three specific Hermes components — identity layers, memory systems, and self-learning loops — critiques each, and explains how they rebuilt improved versions. Most relevant to agency owners, consultants managing multiple clients, and developers building production agentic workflows.

## Key insights
- Hermes reached 40,000 GitHub stars in 46 days (vs. OpenClaw's 61 days), making it the fastest-adopted agentic framework on GitHub
- **Hidden cost #1 — inherited assumptions:** Hermes's self-learning loop has no external guardrails; the same model that writes a skill is also the sole judge of its correctness, creating a self-validation problem that can silently overwrite good work with worse versions and has no version control or audit log
- **Hidden cost #2 — can't fix what you don't understand:** OpenClaw (the predecessor category) has 200+ vulnerabilities filed since February, including 386 malicious packages from a single threat actor on its skills marketplace; debugging someone else's architecture is extremely difficult
- **Hidden cost #3 — doesn't scale across a business:** A non-technical CEO (Paul) spent 100+ hours and $1,000+ testing OpenClaw over 2 months, ultimately finding bugs and security gaps that disqualified it from production use; he later replicated ~30% of its features in Claude in a fraction of the time
- **Identity layer critique:** Hermes uses a `memory.md` + `user.md` file structure designed for a single person/business; running it for multiple clients requires entirely separate installations, each with its own memory, skills, and learning loop — creating a maintenance nightmare
- **Identity layer rebuild:** The creator's system injects shared brand context (voice, ICP, visual identity) per client while sharing skills/procedures across clients via a single installation and a structured folder hierarchy
- **Memory system — three levels:** Storage (saving context), injection (loading context into conversations), and long-term recall (searching for older memories)
- **Hermes memory limitation:** Caps injected memory at ~1,300 tokens (recent snapshot only); long-term recall is keyword-based, not meaning-based, making it nearly useless when you can't remember the exact words used months ago
- **Memory rebuild:** Retains Hermes's pattern of injecting a capped `memory.md` (~2,500 characters) per session, but adds semantic/meaning-based search (via a system like MemSearch) for long-term recall when local memory doesn't have the answer
- **Self-learning loop critique:** Hermes auto-generates a new skill after each task; by the 10th–20th iteration of a similar task, you end up with 15 near-duplicate skills (e.g., "LinkedIn Post V1," "LinkedIn Post V2," "LinkedIn Post for Client X") with overlapping descriptions, no clear selection logic, and no single source of truth to update when brand voice or positioning changes
- **Skill systems rebuild:** Skills are modular components, each doing one job in one place with a consistent naming format; complex outputs (e.g., a LinkedIn post) are produced by a skill *system* that chains separate skills for voice, ICP, and formatting — updating one file propagates changes everywhere
- The core trade-off stated explicitly: **Hermes is faster to start; a custom build is faster to scale**
- The creator's Agentic OS is available in their "Agentic Academy" and installs in one line

## Use cases
- **Agency owners or consultants** managing multiple clients who need separate brand contexts but shared reusable workflows
- **Developers evaluating off-the-shelf agent frameworks** (Hermes, OpenClaw, etc.) before committing to one
- **Anyone building production agentic workflows** who needs auditability, version control, and long-term maintainability
- **Non-technical founders or operators** who want AI automation but need to understand what they're deploying before committing time and money
- **Teams that have already installed Hermes or OpenClaw** and are hitting maintenance or scaling walls
- **Security-conscious builders** who need to vet the supply chain and architecture of the tools they're running

## Patterns & frameworks

**1. Three Hidden Costs Framework**
A decision-making lens for evaluating off-the-shelf agent tools: (1) inherited assumptions you didn't choose, (2) inability to debug what you don't understand, (3) poor scalability across multiple clients or brands. Used to argue for custom builds over plug-and-play installs.

**2. Identity Layer (Context Injection)**
A pattern where agent identity is established by injecting structured files (`user.md`, `memory.md`, brand context files) at the start of every conversation. The rebuild extends this by scoping brand context per client while keeping skills/procedures shared across a single installation.

**3. Three-Level Memory Architecture**
Separates memory into: (a) **storage** — saving and summarizing conversations, (b) **injection** — loading a capped recent-memory snapshot into every session, (c) **long-term recall** — searching older memories. The key upgrade is replacing keyword-based recall with semantic/meaning-based search (e.g., MemSearch, or Memory Palace for verbatim recall).

**4. Skill Systems (Modular Skill Architecture)**
Skills are atomic, single-purpose components rather than monolithic task scripts. Complex outputs are produced by a "skill system" that chains skills together in sequence, pulling from single source-of-truth files for voice, ICP, and formatting. Updating one component file propagates to every system that depends on it — solving the skill proliferation and maintenance problem created by Hermes's auto-generation loop.

**5. Build vs. Buy Trade-off Model**
Explicit framework: off-the-shelf = faster to start, slower to scale, harder to debug; custom build = slower to start, faster to scale, fully transparent and maintainable. Neither is universally correct — framed as a deliberate personal/business choice based on context.