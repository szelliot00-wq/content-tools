# I Stopped Using PowerPoint After Building This Claude Code Skill (Full Tutorial + 3 Templates)

Video ID: `vbChRIIlSPE`

## Summary
The video demonstrates how to replace PowerPoint/Google Slides with an AI-powered Claude Code "skill" that generates fully animated, interactive HTML slide decks from a rough outline in minutes. The creator walks through his `/slides` skill — covering its 12 slide formats, 3 visual templates, built-in QA loop, and the skill files that power it. The core argument is that the real value isn't the slides themselves, but building reusable systems so AI does the recurring work for you. Most relevant to product managers, developers, and knowledge workers who regularly create presentations.

## Key insights
- The creator stopped making PowerPoint/Google Slides manually after building this skill — he hasn't done so in "at least a few months"
- The skill generates a complete HTML deck from a topic in minutes, vs. ~1 hour+ to make the same deck manually
- HTML slides support live interactive charts (hover to see values), smooth animations, and image embedding with AI-handled alignment — things static slide tools can't easily do
- The skill includes **12 slide format types**: two-column, stack grid (3 stats), comparison table, steps (3-step animated), roadmap (quarterly milestones), code block, quote slide, and interactive charts
- Three visual templates are included: **default (brand), dark, and light**
- The skill workflow has 6 steps: (1) read `skill.md` + `styles.md`, (2) ask clarifying questions, (3) do online research to enrich content, (4) generate the full HTML file, (5) run a visual QA agent that screenshots every slide and fixes layout bugs, (6) deliver the deck
- The **self-QA step is critical**: a separate agent renders each slide as an image, inspects for layout issues, and auto-fixes the HTML before the user even sees it
- The skill is invoked with `/slides` in Claude Code — it asks: do you have content or just a topic? how many slides? which style? who is the audience?
- The skill files are plain text (Markdown): `skill.md` (workflow instructions), `styles.md` (color/format guidelines), and a `slides` code file — "a skill is basically just a text file with instructions for the AI"
- The creator didn't write the skill text manually — he iterated with AI through trial and error, generating decks, giving feedback, and having AI improve the skill file
- Images can be included by drag-and-dropping into a folder or pasting into Claude Code
- The skill is available (behind a paid subscription) at **behindthecraft.com**, which hosts 10+ hand-curated skills
- Web search is baked into the skill so AI can research the topic and add real facts/data to supplement your outline

## Use cases
- **PMs and developers** who need to create decks frequently (strategy updates, roadmaps, sprint reviews, stakeholder presentations)
- **Technical presenters** who want to show live code blocks or interactive benchmark charts instead of static screenshots
- **Content creators and educators** building tutorial or explainer decks quickly from a document or URL
- **Anyone pitching** who wants polished animated slides without spending an hour in a slide editor
- **Teams standardizing presentations** — the templates and formats enforce visual consistency across all decks
- **Researchers or analysts** who want AI to pull in external data/facts to automatically enrich a slide outline

## Patterns & frameworks

**The Skill Pattern (Build a system, not a one-off)**
The meta-lesson of the video: instead of doing repetitive work manually, invest time once to build an AI skill (a prompt/instruction file) that automates that work forever. The upfront cost is higher than just making the slides, but every future use is near-zero effort. Applicable beyond slides — to any recurring knowledge work artifact.

**The 6-Step Slide Generation Workflow**
A repeatable pipeline baked into the skill: read templates → ask clarifying questions → research the topic online → generate HTML → self-QA with screenshot inspection → deliver. The QA loop (step 5) is the key differentiator that catches layout bugs before the human reviews.

**AI Self-QA Loop**
A best practice pattern: instruct the AI to review its own output (by rendering screenshots and inspecting them) before handing it to you. This catches a "ton of issues" automatically and reduces back-and-forth. Generalizes to any AI task where output quality can be verified programmatically.

**Iterative Skill Development**
How to build a skill: (1) ask AI for a rough first draft of the skill, (2) have it generate real outputs, (3) give feedback on failures, (4) have AI update the skill file. Repeat until quality is stable. The creator explicitly notes the current skill file reflects many rounds of trial and error — not a single perfect prompt.

**The 12 Slide Format Library**
A predefined menu of reusable slide types matched to common communication needs (comparison, steps, stats, roadmap, code, quote, chart). Forcing variety across formats prevents visually monotonous decks and gives the AI a constrained, high-quality design palette to choose from.