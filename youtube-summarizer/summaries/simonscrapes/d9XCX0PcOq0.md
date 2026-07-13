# Stop Using Fable 5 in Claude Code (It’s Holding You Back)

Video ID: `d9XCX0PcOq0`

## Summary
This video argues that Fable 5 (a top-tier Claude model) is overkill for most Claude Code tasks, especially now that it no longer ships with flat subscriptions and bills at $10/M input and $50/M output tokens. The presenter walks through three specific patterns for using Fable 5 strategically — planning, code review, and goal-oriented agentic tasks — and then covers seven concrete settings and configuration changes that reduce token overhead regardless of which model you use. It is most relevant to developers and teams actively using Claude Code with API billing, particularly those managing costs at scale.

## Key insights
- **Fable 5 is leaving Claude subscriptions on July 12, 2026** and will bill at full API rates: $10/M input, $50/M output tokens
- **A single "Hi" message costs 19,000–37,000 tokens** due to system prompts, CLAUDE.md files, memory files, MCP tool schemas, custom agents, and skills loading before you type anything — roughly $0.30–$0.40 on Fable 5 for the first message alone
- **Cost per token is misleading; cost per finished task is the real metric.** Real-world comparisons showed:
  - Simple code review (200-line PR): Fable 5 ~$0.10 (8× Sonnet's cost), but surfaces edge cases smaller models miss
  - Full Next.js pricing page: Sonnet ~$0.25 but required 2 hours of human rework; Fable 5 ~$4.18 but was ship-ready — if your time is worth $50/hr, Fable is cheaper
  - Multi-hour CRUD app build: Opus 4.8 finished at $5.40 with rough edges; Fable 5 finished at $23.70 with tests, docs, and merge-ready output
- **Sub-agents inherit the parent model by default** — if you're on Fable 5 and Claude spins up 5 parallel research agents, all 5 run on Fable 5 rates
- **MCP servers load their full tool schema at session start** regardless of whether you use them — 10,000–20,000 tokens per server, meaning 4–5 connected servers adds 50,000–70,000 tokens of overhead before any work is done
- **Switching the default model to Sonnet alone reportedly cuts bills by ~50%** for teams doing everyday tasks
- **Claude.md is the most expensive file per word** — it loads on every session start and travels with every message. A test comparing a 3,847-token CLAUDE.md vs. a 312-token trimmed version showed 92% context reduction with no quality regression, saving ~$460/month on a $500/month API bill
- **The `.claudeignore` file alone showed 85.5% context reduction** in measured results (from Fireclaw's blog) by blocking junk reads like `node_modules`, `dist`, `build`, and lock files
- **Auto-memory forks your entire context** into a background call to extract memories — you pay full input token prices for that duplicated context
- **Haiku (Hi-Q) costs ~1/5th of Sonnet** and is sufficient for sub-agents executing a pre-made plan

## Use cases
- **Developers on API billing** who previously relied on a flat subscription and need to manage costs with Fable 5
- **Teams doing code reviews** who want Fable 5's reasoning quality without paying for heavy implementation output tokens
- **Engineering leads managing shared Claude Code budgets** across a team, especially for setting spend limits and enforcing model defaults
- **Anyone building agentic workflows** where sub-agents are spun off — particularly relevant to avoid accidentally running parallel agents on expensive models
- **Projects with large CLAUDE.md files or many MCP connections** that are unknowingly inflating every single message's token count
- **Anyone doing complex, ambiguous tasks** (e.g., accounting reconciliation, multi-session builds) where Fable 5's self-checking loop and reasoning justify the cost
- **Freelancers/consultants billing by the hour** where Fable 5's ability to produce ship-ready output on the first pass is cheaper than paying for human rework time

## Patterns & frameworks

**Pattern 1 — Plan on Fable, Build on Sonnet**
Use `/model` to switch to Fable 5 for the planning phase (lower output tokens, high reasoning value). Once a complete plan is generated, write it to a `plan.md` file, switch back to Sonnet, then execute with `execute the plan.md`. Fable's intelligence shapes the architecture; Sonnet's cheaper rates handle the implementation. Planning used ~38,000 tokens in the demo vs. far more for a full build.

**Pattern 2 — Fable as a Reviewer Sub-Agent**
Create a lightweight sub-agent at `.claude/agents/code-reviewer.md` that specifies `model: fable-5`, scoped only to reviewing (not writing) code. The instruction "do not write code, just return findings" keeps output tokens low while leveraging Fable 5's ability — described as "Mythos class" — to find exploits, edge cases, and security issues.

**Pattern 3 — Goal + Success Criteria + Verification Criteria (Loop Engineering)**
For complex, ambiguous tasks, give Fable 5 a goal, explicit success criteria, and a verification step rather than prescriptive step-by-step instructions. Fable's built-in self-checking loop (plan → execute → validate → correct) handles hundreds of ambiguous judgment calls autonomously. Example: accounting reconciliation framed as a 15-line prompt with success criteria ("every bank line appears exactly once") rather than exhaustive matching rules.

**Token Reduction Checklist (7 settings)**
1. Set default model to Sonnet via `/model`
2. Set `CLAUDE_SUB_AGENT_MODEL=haiku` in `settings.json` ENV to cap sub-agent model costs
3. Trim CLAUDE.md to under 200 lines (ideally 60), removing anything Claude can infer from the codebase; use HTML comments for team notes (they don't count as tokens)
4. Add a `.claudeignore` file to block `node_modules`, `dist`, `build`, lock files, etc.
5. Add enforced `deny` permissions in `settings.json` for the same directories (`.claudeignore` is advisory; permissions are enforced)
6. Disconnect unused MCP servers (anything unused in the last two weeks); use CLI tools instead for occasional calls
7. Set `enableToolSearch: true` in `settings.json` so tool definitions load on demand instead of all at once; turn off auto-memory via `/memory` if you have a custom memory system