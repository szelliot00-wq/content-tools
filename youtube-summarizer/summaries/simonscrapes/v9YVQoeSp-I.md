# 5 Claude Myths Even “Pros” Fall For

Video ID: `v9YVQoeSp-I`

## Summary
This video debunks five widely-shared Claude Code tips that are either outdated or only partially correct, arguing that model improvements (especially Opus 5.5) have made many workarounds unnecessary. The host walks through plan mode, CLAUDE.md management, agent team design, model cost optimization, and third-party plugins — showing how advice that was valid for older models can now hurt performance or waste tokens. It is most relevant to power users and teams actively using Claude Code for real workflows who want to stay current as the models evolve.

## Key insights
- **Plan mode is no longer for the agent — it's for the user.** Older models needed the "don't code yet" prompt reminder; Opus 5.5 plans internally before acting and doesn't need the constraint. The real value of plan mode was surfacing Claude's assumptions for human review, not holding the model back.
- **The replacement for plan mode is a four-part brief:** (1) what "done" looks like, (2) how it will be validated, (3) what is out of scope, and (4) guardrails / what Claude cannot touch. These give Claude the information it used to guess at.
- **CLAUDE.md files have a quality problem, not a quantity problem.** When Claude 5 models launched, Anthropic cut 80%+ of their own system prompt with no measurable loss on coding tests. Docs now recommend keeping CLAUDE.md under 200 lines; longer files cause Claude to ignore rules.
- **Deleting CLAUDE.md wholesale is also wrong.** Some rules cover decisions Claude can't infer from files — team decisions, client preferences, specific prohibitions. The right test per line: "Would removing this cause Claude to make a mistake?"
- **`agents.txt` now covers both Claude Code and Codex.** If there is no `CLAUDE.md`, Claude Code reads `agents.txt`, so one file can serve both tools.
- **Fixed agent teams are out; orchestrator-led teams are in.** Eric Provencher (Codex) found that running more than two agents at once almost always burns tokens with no quality gain due to a "coordination tax" — agents double-checking each other. Anthropic counters with orchestrator-led parallelism: one lead agent spawns sub-agents only when needed.
- **Anthropic's large multi-agent run found 66 of 70 hidden bugs** vs. 14–27 for a single agent — but they still recommend starting small because token costs scale fast.
- **Haiku 5.5 is 40x cheaper per token than Opus 5.5, but often more expensive per job.** On Terminal Bench, Haiku 5.5 scores 39% vs. Sonnet 5.5 at 71%. Wrong answers go back to the main model for correction, often producing 2–3 fix rounds that cost more overall. The right metric is total usage per outcome, not price per token.
- **Most popular skill-pack plugins (including Superpowers) no longer beat a placebo file** when tested on Opus 5.5. In a 450-run test of 9 plugins, only 2 outperformed a dummy file of equal length. These tools were built for models that skipped steps; top-tier models increasingly handle those steps natively.
- **Plugins likely accelerated model improvements** by surfacing gaps to Anthropic and OpenAI, which then got built into the models directly.
- **If you want Claude's assumptions without plan mode**, just ask for a one-line plan before it starts work, rather than entering full plan mode.

## Use cases
- **Solo developers** running Claude Code daily who want to reduce token spend without degrading output quality.
- **Teams with large CLAUDE.md files** that have accumulated rules over many months and want to audit what's still load-bearing.
- **Anyone using fixed agent team setups** (researcher + writer + reviewer) who wants to know whether to simplify to a single orchestrator.
- **Teams weighing cheaper sub-agent models** for file exploration or research tasks and trying to decide whether the savings are real.
- **Users running third-party Claude plugins** (Superpowers, skill packs) who want to know whether they're still earning their token cost on modern models.
- **Product managers and operators** handing off recurring processes to Claude who need a structured briefing method.
- **Anyone still using plan mode by habit** who wants to understand what it was solving and how to replicate the benefit without it.

## Patterns & frameworks

**The Four-Part Brief**
A structured first message that replaces plan mode. Consists of: (1) definition of done, (2) how the output will be validated, (3) explicit out-of-scope items, (4) guardrails / what Claude cannot touch. Forces the human to surface assumptions upfront rather than discovering them mid-execution.

**"Ask Claude to interview you first"**
If you can't answer the four brief questions yourself, prompt Claude to ask you the four questions before starting work. Generates the brief collaboratively rather than requiring it upfront.

**CLAUDE.md Line-by-Line Audit**
Run `/doctor prompt audit` to flag instructions written for older models and broken file references, then assess each remaining line against: *"Would removing this cause Claude to make a mistake?"* Delete anything Claude already does by default; keep only what it cannot infer from your files.

**Orchestrator-Led Agent Model**
Instead of pre-defining a fixed team of role-agents, give the full job to one orchestrator agent and let it decide when to spin up sub-agents. Mirrors how Claude Code's new Projects feature works internally.

**Total-Usage Comparison (not price-per-token)**
When evaluating model choices for sub-agents, run the same task both ways and compare total token usage, fix rounds, and human review time — not the sticker price per token. Cheaper models that produce more errors can cost more overall.

**Coordination Tax (Eric Provencher)**
The overhead cost of multi-agent systems where agents distrust each other's outputs and spend cycles verifying each other's work. Used to argue that >2 concurrent agents rarely pays off in quality per token spent.

**"Conflating planning with a plan" (Ammar Nadeem)**
The distinction between the *act of planning* (which remains essential and Opus 5.5 does internally) and a *visible plan artifact* (which plan mode produced for human review). The planning still matters; the artifact is now optional.