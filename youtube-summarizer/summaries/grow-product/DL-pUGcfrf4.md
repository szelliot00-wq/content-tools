# The AI PM Skill That Gets You Instant Job Offers | Aparna, Arize AI

Video ID: `DL-pUGcfrf4`

## Summary
This episode features Aparna Dhinakaran, CPO and co-founder of Arize AI ($131M raised), walking through the full end-to-end loop of building an AI product taste agent using Claude Code, instrumenting it with observability (tracing), and running evals to iteratively improve it. The core argument is that in the age of AI, **product taste** — not coding ability — is the primary differentiator for PMs, and that observability + evals are the foundational layer for building self-improving agents. The video is most relevant to product managers, AI PMs, and technical product leaders at companies of any size who want to understand how to work with AI agents professionally and competitively.

---

## Key insights

- **Product taste is the new alpha.** Since code is now cheap to produce, the scarce resource is judgment — knowing *what* to build. PMs who develop strong product taste will have outsized leverage.
- **The AI-native PM is nearly indistinguishable from an engineer.** At AI-native companies, PMs are building agents themselves in Claude Code, going from pain point to shipped feature in a single day — something that used to take weeks or months.
- **Start by building, not by planning.** Most teams make the mistake of over-thinking when to add evals. The right sequence is: build something real first, trace everything, then layer in evals once you have data.
- **Tracing is the prerequisite to evals.** You cannot write good evals without first having trace data (the step-by-step playback of what your agent did). Evals that aren't grounded in real trace data have a very low signal-to-noise ratio.
- **Top 1% PM signal:** Any PM who is actively using observability, looking at traces, and running evals on their agents is already in the top 1% of PMs globally right now.
- **"Vibe evals" are a valid starting point but have a short shelf life.** Having Claude auto-generate a first-pass eval from your traces is fine, but it will fall short quickly without human curation and ruthless criticism to align it to real product priorities.
- **The self-improving agent loop is the end goal.** The full loop is: collect traces → run evals → identify failures → fix agent or fix eval → re-deploy → repeat. This loop can itself be automated inside Claude Code using loop/cron skills.
- **Human-in-the-loop checkpoints matter.** Even in highly automated pipelines, humans must review: (1) eval changes, (2) agent changes, and (3) the design of the improvement skill itself. The "radius" of autonomous change starts small (prompt tweaks) and grows over time.
- **Context graphs are the next big unlock, especially for enterprises.** Enterprises have siloed data (Gong calls, Slack, product analytics, GitHub, etc.). Giving agents access to a unified context graph — rather than isolated data silos — is one of the biggest challenges and opportunities of 2024-2025.
- **Enterprise vs. AI-native gap is real but closeable.** Enterprises are still unlocking coding agents for individual workflows. The recommended starting point is building a simple internal agent — not a customer-facing product — to experience the unlock personally.
- **Arize Phoenix (open source) vs. Arize AI (paid).** Phoenix is ideal for teams that can't send data to an external platform (PII concerns, self-hosting). The paid platform makes sense when data volume scales to terabytes. Arize's key differentiators: framework-agnostic, open data formats (no vendor lock-in), inventors of OpenInference instrumentation, first to ship LLM-as-a-judge.
- **The PM agent demo specifics:** The agent pulled 40 GitHub discussions, 60 issues, and 8 releases from Arize Phoenix's repo, scored each item by priority (bugs vs. features, recency, reactions, comments), and produced a ranked PM report (P0–P3) with top pain points, feature requests, and themes — all built in ~1 hour via Claude Code with no IDE.
- **The "study your plays" analogy.** Elite athletes (Nadal, Federer, Djokovic) review their own game footage to improve. Self-improving agents do the same — they study their own traces and eval failures to get 1% better each iteration.
- **Biggest PM eval mistake:** Starting evals from gut instinct rather than actual trace data. Evals must emerge from observed agent behavior, not assumptions about what might go wrong.

---

## Use cases

- **PMs at AI-native startups** who want to build internal tooling (product taste agents, roadmap prioritization agents) without waiting for engineering bandwidth.
- **PMs at digital-first or enterprise companies** who want a concrete first step toward AI-native practices — building a simple internal agent to automate a recurring weekly workflow.
- **AI product teams** shipping agents to customers who need to instrument observability, set up evals, and build an improvement loop without deep ML engineering knowledge.
- **Anyone managing a GitHub-heavy open source or developer product** who wants to automate synthesis of issues, discussions, and releases into a prioritized PM report.
- **Product leaders designing self-improving agent architectures** who need a framework for where to place humans in the review loop (eval changes, agent changes, improvement skill design).
- **Job seekers targeting AI PM roles** who want to understand what skills (Claude Code fluency, observability literacy, eval design) are actually valued by AI-native hiring managers.
- **Engineers or PMs exploring the Arize ecosystem** trying to decide between Phoenix (open source, self-hosted) and Arize AI (paid, scaled).

---

## Patterns & frameworks

**1. The AI Product Development Loop (core framework)**
Build agent → Trace everything (observability) → Run evals → Identify failures (agent or eval?) → Fix → Re-deploy → Repeat. Aparna treats this as the canonical loop for AI product development, analogous to a traditional product sprint cycle but operating at much higher velocity.

**2. Trace → Eval → Improve (TEI Loop)**
A subset of the above. The specific sequence for quality improvement: get trace data first, derive evals from that data, use evals to surface failures, then fix either the agent or the eval depending on which is wrong. Never start evals without traces.

**3. "Vibe eval" → Aligned eval progression**
Start with Claude auto-generating a first-pass eval from traces (vibe eval). Then apply ruthless human criticism — identify where you disagree with the scoring and why. Iterate until the eval reflects genuine human taste. This is presented as a faster on-ramp than starting from scratch with manual annotation.

**4. The "Radius of Change" model for autonomous improvement**
The degree of autonomous self-improvement an agent is trusted with starts small (prompt-level tweaks) and expands over time as evals become more reliable. The radius grows from prompt changes → tool changes → workflow additions. Human review gates each expansion of radius.

**5. The Context Graph**
A unified layer that aggregates feedback from all relevant sources — GitHub issues/discussions, Gong call transcripts, Slack/Discord, product analytics (PostHog, Amplitude, Pendo, FullStory), Twitter, release notes — and makes it accessible to an agent as context. The richer the context graph, the better the agent's output quality and improvement capacity.

**6. The Triple-Threat PM**
A mental model for the ideal AI-native PM: someone who (1) deeply understands user pain points and can articulate them, (2) has strong product taste about what the right experience looks like, and (3) can actually build a working prototype or agent themselves using Claude Code. All three together create disproportionate leverage.

**7. "Study Your Plays" (sports analogy for self-improvement)**
Borrowed from elite athletics: just as Nadal or Djokovic study their own match footage to improve, agents (and PMs) should study their own trace data and eval failures to identify patterns for improvement. The data layer (observability) is the prerequisite — no footage, no improvement.

**8. Skill-based instrumentation pattern**
Rather than manually writing observability code, Arize provides pre-built "skills" (plain-English instruction sets for Claude Code) that auto-detect the agent's language, LLM provider, and call structure, then instrument it automatically. This pattern — encoding best practices as skills for coding agents — is presented as a general approach for reducing the human lift required to adopt new tooling.