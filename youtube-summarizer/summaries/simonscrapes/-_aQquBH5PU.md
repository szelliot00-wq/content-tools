# Master Claude Design in One Video (Full Course)

Video ID: `-_aQquBH5PU`

## Summary
This video is a practical, live walkthrough of using Claude Design (claude.ai/design) to rebuild real business assets for the Agentic Academy, a school community focused on agentic AI workflows. The creator's core argument is that Claude Design is not a drag-and-drop tool like Figma or Canva, but rather a code-generating AI interface that requires significant upfront design system investment to avoid producing generic "AI slop" aesthetics. The video covers building a community landing page, a mobile wireframe for a kanban-style command center UI, and a dynamic slide deck, while comparing Claude Design to Claude Code with external skills. It is most relevant to non-technical founders, indie hackers, product managers, and content creators who want to produce professional-grade UI and marketing assets without a dedicated design or development team.

---

## Key insights

- **Claude Design generates code, not pixels.** Everything it produces — websites, slides, videos, animations — is HTML/CSS/JS under the hood, making it closer to Claude Code than to Figma or Canva. This fundamentally changes how you interact with it (prompting and iterating, not dragging elements).

- **The 90/10 rule is the core mental model.** Claude Design gets you to 90% quickly, but the final 10% — custom microcopy, precise icons, logos, human taste — still requires human intervention or additional tooling.

- **Every output looks the same if you skip the design system.** Reddit backlash and community complaints center on Claude Design defaulting to a "house style" (warm cream/off-white backgrounds, Inter font, colored accent bars, blinking green dots, bento grids). Anthropic's own documentation acknowledges Claude Opus 4.5 has a consistent default house style baked in.

- **The design system setup is the single most important step.** Ryan Mather from Anthropic's design team recommends spending 1–2 hours upfront building a full design system and key reference screens before creating any pages. This feels slow but pays off 10x in output quality and token efficiency.

- **Token usage is real and limited.** Claude Design has a separate usage quota from Claude Chat and Claude Code. On the Max 20x plan, the creator used ~70% of their weekly limit building a full design system, landing page, mobile wireframe, and slide deck. On a Pro plan, users reportedly exhaust their limit after just 1–2 design systems if they don't plan efficiently.

- **Do design system thinking outside Claude Design to save tokens.** The creator used ChatGPT's image model (GPT Image 2.0) to generate a one-page design system from reference screenshots before importing it into Claude Design. This avoids burning Claude Design tokens on exploratory thinking.

- **Two methods for building a design system:**
  1. **Reference screenshots method:** Collect 3–5 screenshots from websites you like, combine them in ChatGPT's image model to produce a bespoke design system one-pager and a design.md markdown doc, then import both into Claude Design.
  2. **Skill UI extraction method:** Use the open-source `skill-ui` npm package (`npm install -g skill-ui`) with Playwright/Chromium to reverse-engineer any website's full design system (colors, fonts, spacing, components, animations, screenshots) into a Claude-ready skill folder, then import the design.md and screenshots into Claude Design.

- **The Taste Skill adds the final 10% polish in Claude Code.** After exporting from Claude Design, running the `redesign` skill from the Taste Skill package (`mpx skills add taste`) audits the HTML for AI aesthetics and fixes them — e.g., changing round numbers to non-round ones (1,200 → 1,247), replacing circles with rounded squares for testimonial avatars, adding weight variety to typography, and removing zigzag layout patterns.

- **The Taste Skill also includes style variants** like `minimalist` and `brutalist`, which can completely transform the aesthetic of an exported landing page. The brutalist output — dark chromatic with accent red and code-style fonts — looked "very Agentic OS" and not AI-generated at all.

- **Inline comments are more token-efficient than full reprompts.** Clicking a specific element and commenting on it targets only that element's context rather than re-sending the entire page context. The creator noted a single element change cost ~2% of their usage limit.

- **Claude Design asks clarifying questions for open-ended briefs.** When given a less prescriptive prompt (e.g., the mobile wireframe for the command center), Claude Design enters a planning mode and asks detailed questions: wireframe style (sketchy vs. clean), which screens to include, how many variations per screen, navigation patterns, how users start new goals, device frame preference (iPhone), and whether to include annotations. This interactive planning feature is not available in Claude Code's terminal interface.

- **Tweaks panel is a standout feature.** Claude Design's "Tweaks" toggle allows switching between settings (e.g., light vs. dark theme, sketchy vs. clean stroke, notes on/off) without re-prompting, at zero token cost.

- **For dynamic slide decks, generate a video first, then convert to slides.** A tip from Peter Yang: asking Claude Design directly for slides produces static, boring output. Asking for an animated video first forces dynamic, motion-rich output, then duplicating the project and asking to convert it to a clickable slide deck preserves the energy and animations.

- **Claude Design does not support custom skills.** Unlike Claude Code, which can use community-built skills (e.g., Skill UI, Taste Skill), Claude Design only uses Anthropic's built-in front-end design skill. This is the single biggest current limitation. The workaround is importing design system files and assets manually.

- **Claude Design vs. Claude Code comparison on landing pages:** Claude Code with the Skill UI extraction produced a recognizable emulation of the StackAI website out of the box, but lacked hover effects, had inferior cards, and required significant brand contextualization. Claude Design, given the same design system, produced a more on-brand, context-aware output that incorporated actual copy, images, and brand elements — but required more token investment to iterate on individual elements.

- **The design system is reusable across all asset types.** Once built, the same design system was used for the landing page, mobile wireframe, and slide deck, ensuring visual consistency across all outputs without rebuilding from scratch each time.

---

## Use cases

- **Founders and solopreneurs** who need a branded landing page but lack a design budget or developer.
- **Community builders** (e.g., School, Circle, Kajabi) who want an external landing page that reflects their brand, not just a generic platform page.
- **Product managers and UX leads** who want to rapidly wireframe mobile or desktop app screens for stakeholder review or developer handoff without hiring a designer.
- **Content creators and educators** who want to turn existing video transcripts or LinkedIn carousels into polished, animated slide decks or carousel assets.
- **No-code builders** who want to prototype a UI before committing to a full-stack build in Webflow, Framer, or a custom codebase.
- **Marketing teams** running paid ads who need a more on-brand, conversion-optimized landing page quickly.
- **Agencies or freelancers** who want to generate a 90% design to present to clients before doing final polish in Figma or with a developer.
- **Developers** who want a visual iteration layer on top of Claude Code for front-end work, especially for making granular element-level changes without re-prompting the entire codebase.
- **Anyone dealing with design system inconsistency** across their brand assets who wants a single source of truth that can be applied across web, mobile, and slide outputs.

---

## Patterns & frameworks

### 1. The 90/10 Rule
**What it is:** AI tools like Claude Design will reliably get you to 90% of a finished design. The last 10% — brand-specific microcopy, custom icons, logos, and human aesthetic judgment — still requires human input or specialized tooling.
**How it works:** Use Claude Design aggressively for structure, layout, color, and typography. Then either hand off to Claude Code with the Taste Skill, a developer, or a designer for the final polish layer.

---

### 2. Design System First (The "Spend the First Hour" Framework)
**What it is:** Coined/emphasized by Ryan Mather from Anthropic. Before creating any page or asset, invest 1–2 hours building and approving a complete design system in Claude Design, including colors, typography, spacing, buttons, inputs, and key marketing screens.
**How it works:** Feed reference screenshots, a design.md markdown file, font files, and logo assets into the design system setup. Review each component card (colors, neutrals, typography, buttons, etc.) using the "Looks Good / Needs Work" interface. Only approve things you're genuinely happy with. Once published, every future design inherits these tokens automatically.

---

### 3. The Two-Method Design System Ingestion Pattern
**What it is:** A framework for building a non-AI-looking design system before entering Claude Design, using one of two external methods to avoid burning design tokens on exploratory thinking.
**How it works:**
- **Method 1 (ChatGPT Image Model):** Collect screenshots from 3–5 websites you admire → paste into ChatGPT with GPT Image 2.0 → prompt it to create a one-page design system (tokens, buttons, colors, typography) → refine with Taste Skill "forbidden patterns" (no Inter font, no generic gradients, etc.) → export as both an image and a design.md → import both into Claude Design.
- **Method 2 (Skill UI CLI):** Run `skill-ui --url [website] --mode ultra` in terminal → tool uses Playwright to extract full design system (colors.json, spacing.json, fonts, component screenshots, animations, scroll captures) into a structured folder with a skill.md → import the skill.md and key screenshots directly into Claude Design.

---

### 4. Asset Design vs. System Design (The AI Daily Brief Framework)
**What it is:** A mental model for categorizing design tools by their intended scope.
**How it works:**
- **Asset design** = single deliverables (one post, one flyer, one image). Canva lives here.
- **System design** = multi-screen, consistent-look outputs (websites, apps, full front-ends). Figma and Claude Design live here.
Using Claude Design for asset design is inefficient; it's purpose-built for system design outputs.

---

### 5. The Video-First Slide Deck Pattern
**What it is:** A tip from Peter Yang for creating dynamic, animation-rich slide decks using Claude Design.
**How it works:** Instead of prompting for a slide deck directly (which produces static output), first prompt Claude Design to create an animated video explaining your content. Claude generates motion, transitions, and scene structure optimized for video. Then duplicate the project and ask it to convert the video into a clickable slide deck. The result inherits the dynamic energy of the video format.

---

### 6. The Taste Skill Polish Loop
**What it is:** A post-export refinement pattern using the open-source Taste Skill package inside Claude Code to remove residual AI aesthetic patterns from Claude Design exports.
**How it works:** Export the finished design from Claude Design as a standalone HTML file → install Taste Skill (`mpx skills add taste`) → run `redesign` skill pointing at the HTML file → Claude Code audits the file, identifies AI tells (round numbers, circle avatars, zigzag layouts, uniform font weights, generic gradients), and rewrites them → optionally run `minimalist` or `brutalist` skill variants for a completely different aesthetic direction.

---

### 7. Token Conservation Protocol
**What it is:** A set of practices to avoid burning through Claude Design's limited weekly token quota prematurely.
**How it works:**
- Do all design system setup in a single focused session, not spread across multiple sessions.
- Do all exploratory design thinking (color palettes, layout inspiration, design system generation) in ChatGPT or Claude Code *before* entering Claude Design.
- Use inline element-level comments rather than full reprompts for changes (targets only the relevant element's context).
- Use "Looks Good" approvals freely (no token cost) and reserve "Needs Work" for genuine changes.
- Only use Claude Design if you're committed to building something real, not just experimenting.