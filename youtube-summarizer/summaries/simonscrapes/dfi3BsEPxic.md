# Claude 5 Changed Prompting Forever, Fix Yours Now

Video ID: `dfi3BsEPxic`

## Summary
This video breaks down Anthropic's official prompting guidelines for Claude Fable 5 and Opus 5, arguing that techniques that were best practice 3–6 months ago now actively degrade output quality on these newer models. The presenter walks through seven specific rules — some about what to add (intent, definition of done) and some about what to remove (step lists, emphasis words, self-check instructions) — using a live client reporting prompt as the working example. A brief comparison with OpenAI's GPT-6 Astra guide shows the two providers largely agree on the new direction. The content is most relevant to power users of Claude Code, anyone who has built skills or system prompts before mid-2025, and product managers or agency operators using AI for client deliverables.

---

## Key insights

- **Step-by-step instructions now hurt performance.** Fable 5 and Opus 5 are trained to complete tasks end-to-end. Providing a numbered list of steps narrows the model to the human's version of the job, which is often worse than what the model would derive from a high-level goal alone.
- **Give the reason, not just the request.** Anthropic's new guides include a section titled "Give the reason not only the request." On any real task there are ~50 small decisions not specified in the prompt (e.g., is a 4% lead drop noise or bad news?); providing intent lets the model make those calls correctly.
- **Anthropic's template: "I'm working on X, for Y, so that Z — with that in mind, [task]."** This two-part structure separates context/intent from the concrete deliverable and is explicitly recommended in the Fable 5 prompting guide.
- **Define what "done" looks like explicitly.** Opus 5 expands scope by default and adds unrequested steps. For narrow tasks, you must state the exact deliverable — e.g., "a client email under 300 words, leading with total leads, including a table of the top 3 reasons for the shift."
- **For large builds, let Claude interview you.** From the Claude Code best practices guide: start with a minimal prompt, then instruct Claude to interview you using the ask-user-questions tool, covering goal, audience, definition of done, edge cases, and trade-offs. Claude then writes the brief itself.
- **Remove emphasis words (IMPORTANT, ALWAYS, NEVER, CRITICAL, YOU MUST).** These models are so responsive that such words over-trigger them. Replace "Critical: you must use this tool" with "Use this tool when." Anthropic cut over 80% of Claude Code's own system prompt using this approach.
- **Don't tell it what not to do — tell it what to do, and why.** Negative constraints (e.g., "never use bullets") are now redundant tokens that can conflict with built-in system prompt instructions on Fable 5.1, which already defaults to fewer bullets and less bold.
- **Remove "Think carefully" and "Walk me through your reasoning."** Opus 5 already thinks before answering by default. Adding a thinking prompt triggers a second reasoning pass, wasting tokens and money. On Fable 5, asking it to reproduce its reasoning can trigger a refusal — the model has a safeguard against attempts to extract and reverse-engineer its thinking.
- **Remove "Double-check every number."** Opus 5 already verifies its own work. Adding a double-check instruction buys a redundant second pass at extra cost. Same applies to "use a sub-agent to verify this."
- **State whether you want an answer or an action.** Fable 5 has a bias toward action and will draft emails, create backups, and build dashboards without being asked. Add a global instruction (in Claude.md or project settings): "When the user describes a problem, asks a question, or thinks out loud, the deliverable is your assessment — report your findings and stop." Exception: scheduled autonomous tasks should get the opposite instruction.
- **Use low/medium effort for simple tasks.** Anthropic says Fable 5.1 on low effort is still competitive with older Opus models in cost per task, so you can use a more powerful model at lower cost by dialing down effort on routine work.
- **Fix voice in one place with "Please remove all managed prose."** Rather than adding verbose style rules to every prompt, add this single line to Claude.md or project instructions. "Managed prose" is Anthropic's term for dense, long-sentence writing that makes the reader work hard so the writer can perform.
- **The presenter found 11 instances** in their own files of instructions now flagged as harmful by Anthropic (reasoning-extraction lines, double-check lines, emphasis words).
- **OpenAI's Astra 6 guide largely agrees** on removing prescriptive steps, including intent alongside the goal, and using plain paragraphs. Key difference: Astra 6 does *not* have a default bias toward action, so you must explicitly ask for it; Claude 5 over-acts by default. OpenAI also ships a blocklist of AI-sounding words (delve, leverage, etc.) inside its system prompt.
- **Anthropic's sanity check:** Can you show your prompt to a colleague with zero context? If they'd be confused, Claude will be too.

---

## Use cases

- **Agency/consultancy operators** running weekly client reports with AI — the live example is a leads/spend/cost-per-lead summary email for an SEO client
- **Claude Code power users** who have built skills, CLAUDE.md files, or system prompts before mid-2025 and need to audit and rewrite them
- **Product managers or founders** using AI to draft client-facing communications and worried about AI-sounding output
- **Anyone building Claude agents or automations** who needs to constrain autonomous action-taking behavior
- **Developers prompting AI for large feature builds** who don't yet have a clear definition of done — use the interview pattern instead of guessing
- **Teams comparing Claude vs. GPT** who need to know whether prompting strategies transfer across providers
- **Content creators or marketers** trying to eliminate managed prose / AI-sounding language from outputs without writing verbose style rules

---

## Patterns & frameworks

**1. Intent-first prompt structure ("I'm working on X, for Y, so that Z — with that in mind, [task]")**
A two-part template from Anthropic's Fable 5 guide. Part one establishes the larger project, the audience, and the output's purpose (the *why*). Part two delivers the specific, tightly-defined task. This gives the model enough context to make the ~50 small judgment calls that aren't explicitly specified.

**2. Definition of Done (DoD) constraint**
For narrow tasks, write out exactly what the finished output looks like: format, length, leading element, and any required components (e.g., a table). This counteracts Opus 5's default scope-expansion behavior.

**3. Claude-interviews-you (brief-generation pattern)**
For large or ambiguous builds, start with a minimal prompt and instruct Claude to interview you using the ask-user-questions tool, covering: goal, audience, definition of done, edge cases, and trade-offs. Claude synthesizes the answers into a full brief that then kicks off the project. Prevents the common failure mode of writing a long upfront prompt that still misses key decisions.

**4. Positive-instruction replacement**
Replace every negative or emphatic constraint ("Never use bullets," "ALWAYS check X," "Critical: you must…") with a positive behavior statement plus the reason for it ("Use plain paragraphs because the client reads this on mobile"). This is the same method Anthropic used to cut 80%+ of Claude Code's system prompt length.

**5. Global action-boundary instruction**
A reusable paragraph (recommended for Claude.md or project/desktop instructions): "When the user describes a problem, asks a question, or thinks out loud, the deliverable is your assessment — report your findings and stop. Before running a command that changes system state, check that the evidence supports that specific action." Prevents unrequested file edits, emails, backups, and dashboards.

**6. Effort-level tuning**
Use the model's effort slider (low/medium/high) rather than prompt-level thinking instructions. Low effort on Fable 5.1 is cost-competitive with older Opus models, so routine tasks should run on low; complex reasoning tasks on high. Never add "Think carefully" — it triggers a redundant second reasoning pass.

**7. "Please remove all managed prose" — single-line voice control**
Instead of multi-paragraph style rules in every prompt, place this one instruction in a global location (Claude.md, project settings). "Managed prose" is Anthropic's named concept for dense, performative writing; invoking the term gives the model a precise target to eliminate.

**8. Skill rewrite audit**
A systematic process (the presenter built a skill for it) to review all pre-Fable 5 prompts and skills: keep the goal, audience, and definition of done; strip step lists and convert them to high-level goals; replace every never/always/must with a positive instruction + reason; remove reasoning-extraction and double-check lines; show a diff before applying changes.