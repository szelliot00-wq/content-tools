# Everything You Know About Skills IS OUTDATED

Video ID: `e7TY56-yIvM`

## Summary
This video covers Anthropic's updated best practices for building Claude Code "skills" (reusable instruction sets), arguing that the rules that applied when skills launched earlier this year are now outdated. The presenter walks through six new guidelines — covering file structure, instruction granularity, model-specific testing, reference file depth, self-verification loops, and dependency portability — that significantly affect how skills should be authored and maintained. The core argument is that skill quality increasingly comes from file layout and built-in checks rather than precisely worded instructions, especially as newer models need less hand-holding. It is most relevant to Claude Code power users, prompt engineers, and teams building or sharing skills for business workflows.

---

## Key insights

- **The head-100 problem**: Claude runs a `head -100` command on reference files to decide if they're worth reading. Any rules or content after line 100 may be ignored entirely, making long reference files without a contents list unreliable.
- **Contents list fix**: Any reference file over 100 lines must have an indexed contents list at the top (matching its section headings) so Claude can either read it fully or jump directly to the relevant section.
- **Degrees of freedom framework**: Skills should not all have the same level of prescriptiveness. Three levels apply — high (plain goal, ambiguous approach), medium (template with some variation), and low (exact script, no deviation). One skill can mix all three levels across different steps.
- **Low freedom = script, not more text**: For fragile or consequential operations (invoicing, database migrations, deletions), the answer is a literal script Claude runs identically every time — not more detailed instructions.
- **Model-specific testing is mandatory**: A skill's output depends on which model runs it. Skills built for older models can make newer reasoning models (e.g., Fable 5) perform *worse*. The guidance is one diagnostic question per model tier: Haiku — enough guidance? Sonnet — clear and efficient? Opus — avoid over-explaining?
- **Newer models need fewer instructions**: 6–8 months ago, numbered lists and CAPS emphasis were needed to prevent step-skipping. Now, over-prescription actively degrades output on high-end models. Remove instructions if the model does better without them.
- **Document intended model in YAML front matter**: When sharing skills, specify which model(s) they were written and tested for, directly in the skill's front matter block.
- **Keep skill.md under 500 lines**: Treat it as a table of contents that delegates to separate reference files; split content into separate files as the limit approaches.
- **One level deep only**: Reference files should be linked directly from `skill.md`. Nested chains (skill.md → advance.md → details.md) cause the deepest file to be only partially read due to the head-100 preview behavior.
- **Split reference files by domain**: For skills covering multiple areas, use separate files per domain (e.g., finance.md, sales.md) so unrelated context is never loaded unnecessarily.
- **Scripts consume no context window**: Scripts are *run*, not read into memory, so they don't cost Claude any context — an advantage over embedding long procedural instructions as plain text.
- **Checklists for ordered multi-step processes**: When step order matters, give Claude a checklist it copies into its reply and ticks off. This is not contradicted by the "give the whole goal" prompting advice — checklists apply only when sequence is meaningful.
- **Self-correction via "go back" instructions**: A step in a checklist can include a condition like "if citations are incomplete, return to step 3," preventing Claude from ticking a failed step and moving on.
- **Feedback loop pattern**: Skills should include a draft → check against guide → note failures → revise → re-check loop, repeating until output passes. This works with non-code checks (e.g., brand voice documents).
- **Living style guide**: When a draft fails for a reason not yet in the style guide, have Claude suggest a new rule at the end of the run. Approve it, add it to the doc, and subsequent runs are checked against it — the skill improves itself over time.
- **Fable 5 can update its own skills**: The model is explicitly noted as capable of updating skills based on what it learns during a task execution.
- **Portability via explicit dependency installation**: Never assume tools/libraries are installed. Every script in a skill should include an install line for its required package. If already installed, Claude skips it; if not, it installs it — making skills work on a teammate's machine on day one.
- **Free audit prompt**: The presenter offers a prompt in the video description that checks a skill against all nine rules and shows proposed changes before applying them.

---

## Use cases

- **Teams sharing skills**: Ensuring skills work on colleagues' machines without manual setup or debugging missing dependencies.
- **Business owners automating workflows**: Applying degrees of freedom to distinguish between flexible tasks (drafting LinkedIn posts, reviewing sales calls) and fragile ones (raising invoices, removing members).
- **Developers building code review or research synthesis skills**: Using checklists for ordered workflows and feedback loops to self-validate outputs.
- **Prompt engineers maintaining older skills**: Auditing existing skills built for older models and stripping over-prescriptive instructions that now hurt performance on Fable or Opus.
- **Anyone with long reference files**: Adding contents lists to any reference file over 100 lines to avoid the head-100 truncation problem.
- **Multi-model deployments**: Testing the same skill across Haiku, Sonnet, and Opus to find the right level of detail that works across all three.
- **Data or reporting workflows**: Splitting reference files by domain (finance, sales, marketing) so only relevant context loads per query.
- **Anyone building skills for resale or distribution**: Documenting intended model in front matter and including install lines to maximize portability and reduce support burden.

---

## Patterns & frameworks

**Degrees of Freedom (High / Medium / Low)**
A framework for calibrating how prescriptive a skill step should be. High freedom = plain goal, Claude figures out the approach (e.g., code review, drafting a post). Medium freedom = a template with configurable settings (e.g., weekly report with format options). Low freedom = an exact, unchanging script with no parameters (e.g., database migration, invoice creation). The key diagnostic question for any step: *what happens if Claude does it differently?* If the answer is "not much," loosen it; if it's consequential, lock it down with a script.

**The Head-100 Rule**
Claude previews reference files with `head -100` before deciding whether to read them fully. Any content past line 100 in a file without a contents list risks being ignored. The fix is an index at the top of any file over 100 lines, matching its section headings, so Claude can navigate directly to what it needs.

**One-Level-Deep Reference Structure**
All reference files must be linked directly from `skill.md`, never through intermediate files. Chained nesting (A → B → C) degrades read reliability at each level due to the head-100 preview behavior. Flattening all links to one level ensures consistent access.

**Draft → Check → Revise Loop (Self-Validation)**
A repeatable pattern for output quality: Claude drafts output, checks it against a defined guide (style guide, brand voice doc, schema), notes each failure with the section it violates, revises, and re-checks. It only finalizes when everything passes. The guide itself grows over time as new failure modes are added at the end of each run.

**Checklist-Driven Ordered Workflows**
For multi-step processes where sequence matters, Claude is given a checklist it copies into its reply and ticks off step by step. Steps can include conditional rollback instructions (e.g., "if X fails, return to step N") to prevent false progress. Not used when order is irrelevant — only when it genuinely matters.

**Model-Tier Calibration**
A testing protocol where the same skill is run on Haiku, Sonnet, and Opus against the same task. Haiku missing steps signals the need for more explicit guidance or a low-freedom script. Opus performing worse *with* the skill than without it signals over-prescription — instructions should be removed until performance improves. The target is a skill that works adequately across all tiers, or a skill explicitly documented for a specific model.