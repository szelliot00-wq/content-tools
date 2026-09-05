# Building a Self-Improving Loop in Claude Code (Live Walkthrough)

Video ID: `XsnSvFo4MHQ`

## Summary
Tyler Folkman, Chief AI Officer and Head of Product at Job Nimbus (which raised Utah's largest Series B at $33M), gives a live walkthrough of how he uses Claude Code with an agent orchestration tool called Herder to build self-improving AI loops for product work. The core argument is that AI "loops" — systems that fetch inputs, do work, validate via a gate, produce an artifact, and then feed learnings back to improve themselves — are fundamentally more powerful than one-off prompts or static skills. The video is most relevant to PMs, engineers, designers, and founders who want to move beyond prompt-and-response AI usage toward building autonomous, self-improving systems that scale their output.

---

## Key insights

- **Loops vs. prompts vs. skills**: A prompt is a one-off question. A skill is a reusable set of instructions that stays static. A loop is a skill that feeds its own outputs and learnings back into itself to improve over time — the self-improving flywheel is what makes it a loop.
- **Herder as an orchestration layer**: Tyler uses a terminal-based tool called Herder to manage multiple Claude Code agents simultaneously across panes, with color-coded status indicators (green = done, yellow = in progress). He prefers it over VS Code/Cursor because terminal-based agents have become powerful and community tools evolve faster than IDE extensions.
- **The anatomy of a good loop**: (1) Fetch your own inputs — don't manually gather data, let the agent do it. (2) Do work. (3) Pass a gate — validate that the work is correct; the more deterministic this gate, the better. (4) Write an artifact. (5) Feed learnings back to improve the loop. Missing step 5 means you have a skill, not a loop.
- **Human gates are the hardest bottleneck**: When the gate is a customer (not automated tests), the loop can't run at AI speed. Job Nimbus's solution is to (a) invest more in actual customer time using AI-saved capacity elsewhere, and (b) mine existing recordings/transcripts synthetically to filter bad ideas before human validation.
- **Pre-flight checks as loop hygiene**: Tyler built a demo skill that runs a pre-flight check before recording — checking for sensitive data exposure, git state, and manual checklist items. This shows AI can be a partner in enforcing conditions required for success.
- **Git for rollback, not revert**: Tyler uses Git as the version control mechanism for skills/loops. He notes he rarely reverts backward anymore — instead he "fixes forward" by tweaking the new version to recapture what was lost, since newer versions are rarely uniformly worse.
- **Synthetic customer research as a gate proxy**: Job Nimbus injects all customer call transcripts into their data warehouse, then uses AI to synthetically simulate a customer evaluating a prototype. This isn't a perfect bar but catches low-hanging failures quickly, compressing a funnel from 100 ideas → 5 → 1.
- **Prototyping at AI speed**: Their internal product skill generates three prototype variants (minimal, full-featured, creative) with basic prompts while conversations are happening. Every prototype in the demo was built live during the recording, not pre-built.
- **Skills authored by humans outperform AI-authored skills**: Tyler cites research suggesting human-written skills are better because humans can express intent more precisely. He warns of the "e-bike effect" — once you let AI write everything, it's hard to inject your own thinking because the loop moves too fast.
- **Claude hooks for determinism**: Hooks inject deterministic behavior at specific loop phases (startup, tool use, session close). Examples: blocking `rm -rf` commands, preventing credential exposure, forcing a post-session improvement review. Hooks are more reliable than prompt instructions because Claude can "forget" prompt rules but hooks always fire.
- **Quality loops matter more than velocity loops for engineering**: Shipping 2x faster at the same defect rate means customers experience 2x as many bugs. Tyler argues quality loops (standards checks, automated end-to-end testing) are the most important engineering investment with AI, not raw velocity.
- **AI-generated docs should be written for AI consumption, not humans**: Long AI-generated documents that humans must read are just shifting effort. The emerging norm at Job Nimbus: docs for AI context can be long; docs for humans should be 1–3 pages max, preferably visual and HTML-rendered. If the author used AI to write it without much thinking, it's unreasonable to expect the reader to engage deeply with it.
- **Claude's `/loop` command**: Claude Code natively supports `/loop` to run a prompt or slash command on a recurring interval — Tyler notes this is one mechanism for turning a skill into a scheduled loop, though he considers a true loop to be more than just a cron job (it must include the learning/improvement cycle).
- **Opus 5 verbosity regression**: Tyler and the host both note that Claude Opus 5 produces noticeably wordier, more AI-sounding responses than previous versions — a real regression in feel even if capability improved. He always adds "be succinct" to his skills.
- **Onboarding as a loop**: Job Nimbus built an AI-powered onboarding system that interviews new hires, generates a personalized onboarding plan, auto-schedules meetings via calendar integration, and provides a terminal-based product tutor. The goal is codifying existing process first, then identifying where AI can help.
- **Loops for PMs specifically**: Key recommended loops — (1) customer outreach loop: identify customers from Pendo/Amplitude/DB whose usage changed and auto-draft outreach; (2) project management loop: pull tickets from Linear/Jira, surface risks and stale items; (3) thinking/pushback skill: forces PMs to answer "did you talk to customers? did you check benchmarks? what's the feasibility risk?" before moving forward.
- **Two-thirds of product features deliver flat or negative value** (citing Microsoft research). This is the core justification for always running divergent prototyping and synthetic validation — it's essentially free now, so there's no excuse to skip it.
- **Vibe PMing failure mode**: The risk isn't a shipped bug (visible) — it's shipping something nobody wants, spending time on non-viable ideas, or outsourcing thinking entirely to AI and passing AI output up the chain as your own judgment. "Claude said it would take a week to build" is the cautionary example.
- **Hackathon as hiring signal**: Job Nimbus hosted what Tyler claims was Utah's largest hackathon; one winner is now an SVP; two third-place finishers were hired. The filter was: can you build a real product for their user base end-to-end in two days?

---

## Use cases

- **PMs** who want to replace manual customer outreach identification with an automated loop that surfaces the right customers to contact each week
- **PMs** who want to stop doing manual Linear/Jira ticket reviews and instead get a synthesized risk summary each morning
- **Engineers** who want to run quality loops — automated standards checks, end-to-end tests — to avoid the "2x velocity, 2x bugs" trap
- **Product teams** that want to generate 10+ prototype variants quickly and filter them synthetically before spending time with real customers
- **Leaders** who want to build self-improving onboarding systems that personalize to each new hire's role without manual effort
- **Founders/solo builders** who want to manage multiple parallel agent tasks (research, prototyping, writing) from a single terminal pane
- **Anyone building Claude Code skills** who wants to move from static skills to self-improving loops with post-session learning hooks
- **Engineering teams** that want deterministic safety guardrails (block `rm -rf`, block credential sharing) via hooks rather than prompt instructions
- **Designers** who want to accelerate prototype iteration using component libraries codified into Claude skills
- **Leaders** who want to model AI adoption visibly — the recommendation is to show, not tell, how you use AI

---

## Patterns & frameworks

**The Loop Anatomy (5-step flywheel)**
Fetch inputs autonomously → Do work → Pass a gate (validate correctness) → Write/produce an artifact → Feed learnings back to improve the loop. The "learning" step is what distinguishes a loop from a static skill. The gate step is the most critical and most valuable when made deterministic.

**Prompt → Skill → Loop progression**
A mental model for AI maturity: prompts are one-off interactions (smarter Google search). Skills are reusable instruction sets that stay static. Loops are skills that self-improve by feeding session learnings back into their own definition. Each level requires less human-in-the-loop time.

**The Gate principle**
Every loop needs a validation gate between "do work" and "write artifact." The more deterministic the gate, the more autonomous the loop can be. Code loops can use automated tests. Product loops use synthetic customer simulation or real customer feedback. Without a gate, you're just generating, not validating.

**Fix Forward (not revert back)**
Rather than rolling back to a prior version of a skill when the new one is worse, Tyler's default is to identify what was lost and add it forward to the current version. Revert is available via Git but rarely needed.

**The E-Bike Effect**
Once you let AI take over a task (writing, research, skill authoring), it becomes very hard to re-inject your own thinking because the loop moves fast and provides dopamine. The implication: write the first draft of any skill yourself before handing it to AI to improve.

**Docs for AI vs. Docs for Humans**
Two separate document philosophies: AI-facing docs can be long, dense, and comprehensive (they're context, not reading material). Human-facing docs should be 1–3 pages max, visual, HTML-rendered where possible. Sending an AI-generated 20-page doc to a human is just shifting effort without adding value.

**The Builder Gradient**
Not all product/engineering/design problems require deep specialization. There's a gradient: some problems need best-in-class specialized skill; others are just execution problems where a "full-stack builder" (PM + engineer + designer rolled into one person using AI) delivers faster with less coordination overhead. The triad (PM/design/engineering) existed partly to de-risk long build cycles — as build time collapses, so does the need for heavy up-front de-risking.

**Marty Cagan's Four Risks as a loop design lens**
Tyler explicitly frames the hardest part of product loops around the four risks: feasibility (engineers handle), usability (design handles), viability (can the business make money?), and value (will customers pay?). The last two are the hardest to automate into a gate, which is why customer access remains a critical bottleneck.

**Claude Hooks for determinism**
Hooks are shell commands that fire at specific Claude Code lifecycle events (startup, tool call, session close). They inject deterministic behavior that prompt instructions cannot guarantee. Three hook types discussed: startup hooks (check git state, branch), tool hooks (block dangerous commands), and session-close hooks (force a learning/improvement review before Claude exits).