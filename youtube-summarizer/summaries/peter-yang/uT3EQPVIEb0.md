# Full Tutorial: Build Self-Improving Claude Skills in 20 Min (Eval + Memory)

Video ID: `uT3EQPVIEb0`

## Summary
This tutorial walks through building a self-improving "AI skill" (a folder of instructions that AI can trigger for specific tasks) from scratch using Claude Code, specifically an "edit post" skill for long-form newsletter content. The presenter outlines a 5-step framework that goes beyond basic skill creation to include automated quality loops (evals) and persistent memory so the skill improves over time without constant human intervention. It is most relevant to content creators, newsletter writers, and knowledge workers who want to encode their personal style and judgment into reusable AI workflows.

## Key insights
- **A skill is a folder, not a prompt**: Skills are structured directories with multiple files (skill.md, eval.md, memory.md, example files) that AI reads selectively based on context — not a single monolithic prompt.
- **Separate skill.md from examples**: Keep personal examples in separate files so the skill only loads relevant context per task (e.g., tutorial post examples vs. personal post examples). Benefits: faster execution, avoids overfitting, safer to share.
- **Give multiple examples, not one**: Providing only one example causes the AI to overfit to it. Use at least 2–3 distinct examples per content type.
- **The description field is a trigger gate**: AI only reads the skill name and description before deciding whether to invoke the full skill. The description must be explicit: "Use when [specific condition]." If this is vague, the skill won't trigger reliably.
- **Pass/fail evals beat scored evals**: Numeric scoring (e.g., 4/5) is unreliable because AI can't meaningfully distinguish between scores. Binary pass/fail checks on specific criteria (e.g., "no m-dashes present," "YouTube link included") are more actionable and accurate.
- **The eval loop runs autonomously**: A separate agent with a clean context window runs the evals, avoiding bias from the editing agent's prior context. If checks fail, it loops back to the editing agent for another pass — demonstrated running 5 loops in the video before all 10 evals passed.
- **Memory.md captures qualitative lessons, not quantitative ones**: Use memory for feedback that can't be reduced to pass/fail (e.g., "make the voice more authentic"). Keep entries brief — 2–3 sentences per session — to avoid confusing the model with a bloated memory file.
- **Memory and evals serve different purposes**: Evals improve output within a single session; memory improves the skill itself across sessions.
- **A "skill editor" meta-skill audits your other skills**: Running a skill-builder skill on existing skills catches AI slop (m-dashes, "this is not X, this is Y" phrasing, filler words like "leverage" and "delve"), enforces conciseness, and applies progressive disclosure formatting.
- **AI gets you 80–90% there; humans close the gap**: Even with all five best practices, the last 10–20% requires human review, taste, and judgment. The presenter's actual workflow: dictate a rough draft → AI edit pass using the skill → manual final pass before publishing.
- **Dictation tool callout**: The presenter uses Whisper Flow to dictate instructions and ideas, mentioned as part of the content creation workflow.

## Use cases
- **Newsletter writers** who publish multiple content formats (tutorials, opinion pieces, product breakdowns) and want consistent editing without manually re-explaining their voice each time.
- **Content marketers** who need to enforce brand voice guidelines and eliminate AI-generated artifacts before publishing.
- **Solo creators or indie writers** who want to scale their output without losing personal style or hiring editors.
- **Teams sharing skills** — the separation of personal examples from skill logic makes skills safe to share without exposing private content.
- **Anyone doing repetitive knowledge work** (reports, analyses, briefs) where output quality can be partially defined by pass/fail criteria.
- **AI power users** wanting to build automated quality-control loops that run without supervision.
- **Developers or PMs** building internal AI tooling who want a lightweight pattern for encoding domain knowledge into reusable agents.

## Patterns & frameworks

**The 5-Step Skill-Building Framework**
A repeatable process for building a self-improving AI skill:
1. Create the skill using personal examples and context (separate files per content type)
2. Write an explicit trigger description ("Use when…")
3. Test manually, then build an `eval.md` with up to 10 pass/fail checks
4. Build a `memory.md` to capture session-level lessons for long-term improvement
5. Apply a "skill editor" meta-skill to audit and clean up the skill itself

**The Eval Loop Pattern**
A two-agent feedback loop: Agent A edits the content → Agent B (clean context window) runs pass/fail evals → if any fail, Agent A edits again → repeat until all pass. This allows autonomous quality improvement without human presence mid-task.

**Context Separation Pattern**
Skill logic (workflow, rules, voice guidelines) lives in `skill.md`; raw examples live in separate files linked by reference. The skill loads only what's needed based on detected content type — reduces token overhead and prevents overfitting.

**Memory as Qualitative Supplement to Evals**
For feedback that resists binary encoding (e.g., tone, authenticity), use a reverse-chronological `memory.md` with concise session summaries (2–3 sentences). This gives the skill a learning trajectory without overwhelming its context.

**The 80/20 Human-in-the-Loop Model**
AI handles the first 80–90% (structure, consistency, slop removal); humans contribute the final 10–20% (judgment, taste, contextual nuance). Framed not as AI replacing the creator but as AI compressing the labor-intensive middle stage.