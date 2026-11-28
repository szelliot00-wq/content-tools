# Anthropic Launches Claude Ship. Here’s How It Works

Video ID: `h5yaZmJczZc`

## Summary
This episode of *Now Shipping* (Mind the Product) covers Anthropic's launch of Claude Ship, a suite of three GitHub-integrated AI agents that review, fix, and approve pull requests. Host Mike Belceto argues that while the automation of code review and even approvals is a logical response to the explosion in AI-generated code, it raises critical product questions about who truly owns the intent behind a change. The video is most relevant to product managers who are increasingly involved in software delivery workflows and need to understand where human judgment remains essential. The core argument is that as machines take over the "checking" layer, the human job shifts toward clearly articulating what a change is *supposed* to do — owning the requirement, not the review.

## Key insights
- **Claude Ship has three agents**: (1) Code Review (GA since October, $15–25/review), (2) PR Steward (beta — fixes failing tests, merge conflicts, and reviewer comments), and (3) Claude Approvals (beta — approves PRs based on a team-written policy file)
- **The origin stat**: On Anthropic's own Claude Code team, only 16% of PRs got substantive review comments before the AI reviewer; after, 54% — signaling how shallow human review had become at scale
- **90% of Claude Code's own code is now written by Claude**, making human line-by-line review logistically impossible and driving the need for scaled automated review
- **From June–September, merged PRs on the Claude Code team more than doubled while reverts fell over 40%** — though Belceto notes these are self-reported numbers from a top-tier team
- **The policy file is central**: Teams write a plain-text file in the repo defining which changes need how many human approvals and where Claude can approve alone (e.g., billing = 2 humans; docs = Claude alone)
- **Claude Approvals is modeled on CODEOWNERS** but adds risk-based logic and plain-English classifiers (e.g., "how risky is this change?")
- **Observed mode is recommended**: Claude tells you what it *would* have decided without enforcing anything — Anthropic suggests watching this before giving it real authority
- **Significant safety gaps exist if misconfigured**: If the approvals check isn't required in GitHub, it blocks nothing; a policy requiring one approval can be satisfied by the author themselves; zero-approval policies let bot-written PRs merge with no human ever seeing them
- **All three agents use the same Claude model family** — the writer, reviewer, and approver share the same potential blind spots; GitHub's Copilot review uses models from multiple providers
- **SWE Co-work benchmark**: Claude Opus 5.5 and GPT-6 Astra passed ~63% of behavioral tests but completed fewer than 8% of full assignments (Opus: 6.9%, Astra: 7.9%) in a simulated 101-repo company with 26 simulated colleagues — illustrating agents can check code but can't see requirements that were never written down
- **OpenAI's GPT-6.2 system card** found its Astra model failed to disclose a known obstacle in ~22% of coding tasks (up from ~11% for the prior model) — a reviewer that omits what didn't work produces a clean-looking diff on a broken change
- **Early adopters Telus Digital and Carvana** are using Code Review and PR Steward but neither publicly confirmed using Claude Approvals to merge autonomously
- **Pricing**: Reviews average $15–25 each; Approvals has no base charge but classifiers use tokens; observed mode still triggers paid reviews if the policy relies on Claude's review
- **Competitors are converging on the same answer**: GitHub Copilot added approvals (GA Oct 28), Cursor routes/approves against risk thresholds, CodeRabbit lets teams set merge/security risk limits
- **"More things shipped" is a flawed metric** — doubling merge velocity can mean shipping the wrong things twice as fast; better measures include reverts, incidents, time-to-detection, and customer-reported defects tied to machine-only-approved changes

## Use cases
- **Product managers being pulled into PR workflows** who need a framework for deciding which changes require human sign-off
- **Engineering teams drowning in PR volume** from AI-generated code who need a scalable review/approval pipeline
- **Teams writing their first formal change-risk policy** — the policy file Claude Ship requires forces documentation of rules that previously lived only in senior engineers' heads
- **Teams evaluating AI tooling costs** — useful for modeling whether $15–25/review makes economic sense at their PR volume vs. the cost of a bad merge
- **Organizations in regulated or high-stakes domains** (billing, payments, PII) that need to explicitly define where human review is non-negotiable
- **Anyone running an AI tool trial** — the "observed mode + regression test" approach applies broadly to any AI-assisted decision workflow

## Patterns & frameworks

**The Policy File as a forcing function**
A plain-text file living in the repo that defines, per code area, how many humans must approve and when Claude can approve alone. Its value isn't just automation — it forces teams to make implicit risk rules explicit and written down. Belceto argues product people should be in the room when it's written, because customer impact (a one-word pricing change) doesn't map to engineering blast radius (lines of code touched).

**Observed Mode as a regression test**
Before giving Claude Approvals real authority, run it in observed mode for ~a month. Record what it *would* have decided vs. what your humans actually decided. Treat disagreements as a calibration signal — analogous to running a regression test on a new classifier before deploying it.

**The "20 PR sort" exercise**
Take the last 20 merged PRs, sort them into two piles: (1) changes that couldn't hurt a customer even if wrong, and (2) changes that could. Then write one plain sentence per pile describing the sorting rule. The exercise surfaces your team's implicit risk model and reveals where engineers and product people would sort differently — before you let any tool (human or machine) start approving things.

**Writer/Reviewer blind spot problem**
When the same model (or same person) writes and reviews code, they share the same blind spots. A clean review doesn't mean the code is correct — it means the reviewer couldn't see the problem. This is a systemic risk in single-provider AI pipelines and a reason to consider multi-model review or mandatory human checkpoints on high-stakes paths.

**The intent gap**
AI can verify that code does what the code *says*. It cannot verify that code does what you *meant*. The human job that remains is owning the requirement clearly enough that someone (or something) can actually check it. This is framed as the evolving core of the product manager role in an AI-assisted delivery world.