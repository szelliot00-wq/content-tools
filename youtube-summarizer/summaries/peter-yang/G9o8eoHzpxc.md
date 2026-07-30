# Full Tutorial: From Idea to App with Claude Design and Claude Code in 25 Minutes

Video ID: `G9o8eoHzpxc`

## Summary
This tutorial walks through a 6-step AI-native design process for building a web app called "Tastemaker" — a personal taste profile page for movies, TV shows, and games. The presenter, a product manager, argues that successful AI-assisted development requires front-loading 50% of effort into planning and design before writing any code. The process deliberately uses multiple AI tools in sequence (Claude Code, Claude Design) alongside structured artifacts like `design.md` and `spec.html` to constrain and guide AI output. It's most relevant to product managers, indie hackers, and non-engineers who want to ship polished apps with AI without a traditional design-to-dev handoff.

## Key insights
- **Planning first is non-negotiable.** The presenter explicitly states you should spend at least 50% of your time planning before building. Jumping straight to code without specs and designs leads to an AI that doesn't produce what you want — and database-level decisions become expensive to change once made.
- **Generic AI design output ("purple slop") requires active direction.** By default, AI produces generic-looking UIs. The fix is finding a real app you like (in this case, Monogram), screenshotting it, and using those images to generate a `design.md` that captures a specific visual direction.
- **`design.md` is a lightweight visual system brief.** It's a markdown file containing design principles, color palette, typography, and spacing guidelines. It acts as a persistent reference that keeps AI output visually consistent across all screens.
- **Claude Design's clarifying questions are a feature, not friction.** Unlike other AI design tools, Claude Design asks targeted questions before generating mockups (e.g., "whose profile should the example show?", "row-heavy vs. grid editorial?"). The presenter treats answering these as a valuable design-thinking exercise.
- **Generate key screens before writing the spec.** This inverts the traditional PM workflow (spec → Figma → build). Seeing visuals first makes it far easier to catch missing states, unclear flows, and wrong assumptions before committing them to a written document.
- **A component library inside the spec prevents visual chaos.** Without pre-defining a component library, AI will invent inconsistent components as it builds. The spec's design tab includes a component library that must be kept updated as new screens are added.
- **The spec bundles PRD, design system, and tech requirements in one HTML file.** Three tabs: (1) user problem, goals, and requirements; (2) design principles, style guide, and component library; (3) tech stack and data schema. One file = one source of truth.
- **Data schema must be locked early.** The presenter calls out that "databases are very difficult to change once in production" — this is why schema design belongs in the spec phase, not during build.
- **AI consistently underestimates build time.** The spec AI generated estimated 3 weeks to build the app. Actual time was roughly 30 minutes to a few hours — but only because thorough upfront planning compressed the build phase dramatically.
- **Building still requires heavy iteration.** Even with a spec and full design mockups, the build phase involved many rounds of feedback: pasting screenshots of what's wrong, listing specific issues (e.g., "hover states missing on cards," "review section not matching design"), and repeatedly asking Claude to follow the plan.
- **Keep the plan and design files updated as code changes.** When Claude makes product-level decisions in code, instruct it to sync those changes back to the spec and design files so everything stays in alignment.
- **AI design tools that the presenter evaluated:** Claude Design (chosen), Paper (Figma-like with AI features), pen.dev (multi-agent design), and Figma (now has AI features). Claude Design was chosen for subscription convenience and its clarifying-question workflow.
- **Resource called out for design.md templates:** `z.sh` — contains pre-built design.md files for brands like Nike, SpaceX, Apple, Vercel, and Notion, including their actual color and typography systems.
- **Inspiration vs. copying distinction:** Borrowing visual direction from an app in a completely different product category (Monogram → Tastemaker) is framed as acceptable inspiration; copying a direct competitor would not be.
- **Ask AI to always review and ask questions before building.** The recommended build prompt is: "Review the spec and design and let me know if you have any questions or ambiguities before you start building." This surfaces gaps before code is written.
- **Monetization is harder now.** The presenter notes it's increasingly difficult to build a software business because AI enables everyone to build their own version of anything — something worth validating before investing in a product.

## Use cases
- A product manager who wants to ship a personal app without hiring engineers or designers
- A solo founder building an MVP who wants to avoid costly late-stage design pivots
- A non-designer who needs a repeatable process to get AI to produce visually consistent, non-generic UIs
- Anyone using Claude Code or similar AI coding assistants who finds that AI goes off-rails without enough upfront structure
- A developer who wants to understand how to layer a design system into an AI-assisted build workflow
- Someone building a content/media curation app (the Tastemaker example is directly reusable)
- A team replacing a traditional Figma → spec → dev handoff with a compressed AI-native equivalent
- Anyone evaluating AI design tools (Paper, pen.dev, Figma AI, Claude Design) and wanting a practitioner's comparison

## Patterns & frameworks

**The 6-Step AI-Native Design Process**
The core repeatable framework of the video. Steps run sequentially and each output feeds the next:
1. **Define the user problem** — clarify who it's for, what's broken, and (if commercial) whether there's a revenue opportunity
2. **Get inspired + create `design.md`** — find a real app with a visual style you want, screenshot it, and prompt AI to extract a design brief
3. **Prototype key screens in Claude Design** — generate 2 variations per screen, answer clarifying questions, iterate with direct edits and chat feedback
4. **Create a spec.html** — combine the problem statement, design system, component library, tech stack, and data schema into one interactive HTML file with three tabs (PRD / Design / Tech)
5. **Design all core screens** — upload the spec back into Claude Design to generate every screen including empty states, edge cases, and onboarding flows
6. **Build the app** — attach spec + design HTML to Claude Code, ask for questions before coding starts, then iterate heavily through feedback loops

**The "Diverge then Converge" Design Pattern**
Asking AI to produce multiple variations (e.g., "row-heavy vs. grid editorial," "light vs. dark") before selecting and refining one direction. Mirrors how experienced designers explore a solution space before committing.

**"Visuals Before Spec" Inversion**
Deliberately reverses the traditional PM workflow. Key screens are designed first so the written spec can describe something concrete rather than abstract — making requirements easier to write, review, and validate.

**The One-File Spec (PRD + Design + Tech)**
A single `spec.html` with three tabs that acts as the sole source of truth for the entire build. Eliminates context-switching between separate documents and makes AI easier to ground in consistent requirements.

**The Component Library as a Guardrail**
Pre-defining UI components inside the spec's design tab prevents AI from inventing inconsistent components during the build phase. Must be kept updated as new screens are added.

**"50% Planning" Rule**
A heuristic the presenter treats as a hard constraint: at least half of total project time should be spent on definition, design, and spec work before any code is written. The build phase is fast only because the planning phase was thorough.