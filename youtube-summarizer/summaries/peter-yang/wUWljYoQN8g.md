# Full Tutorial: 3 Layer System for Context Engineering in 40 Minutes | Ravi Mehta

Video ID: `wUWljYoQN8g`

## Summary
This video features Ravi Mehta, former CPO of Tinder and current product adviser, demonstrating a structured "3-layer context engineering" system for AI prototyping. The core argument is that most people prototype poorly because they rely only on simple text prompts, when they should instead provide three distinct types of context — functional, visual, and data — to generate realistic, iterable, and high-fidelity prototypes. Ravi walks through a live demo using Reforge Build, Claude, Figma, and custom MCP servers to build a music genre exploration feature. The video is most relevant to product managers, designers, and anyone using AI prototyping or vibe coding tools who wants to move beyond basic prompting to produce prototypes good enough to put in front of real users.

---

## Key insights

- **Context engineering vs. prompt engineering:** The shift from "prompt engineering" to "context engineering" reflects a deeper change — you're not just having a conversation with an AI, you're designing all the information and tools an AI model needs to do its work effectively. The definition offered: *"Designing and building systems that provide an AI model with the right information and tools to accomplish the task."*

- **The suspension of disbelief problem:** For prototypes to generate useful user research, users must believe they're using a real product. If they don't, they shift from describing what they *are* doing to theorizing about what they *would* do — dramatically reducing the accuracy and value of the research. High fidelity is therefore not aesthetic vanity; it's a research quality requirement.

- **Layer 1 — Functional context (text/spec):** A mini-spec or functionally oriented prompt describing what the feature should do. Example: "Build a music genre detail page for down-tempo with a hero image, genre header, artist tags, and a chronological album timeline." This gets you surprisingly close to a working prototype but lacks realism.

- **Layer 2 — Visual context (wireframe):** A wireframe (built in Figma in ~20 minutes, or even a hand-drawn sketch, Balsamiq, etc.) uploaded alongside a short prompt. The AI interprets it as a blueprint, not literally, and fills in design details. This solves layout and responsiveness problems that text alone can't specify — e.g., on mobile, separating album art from descriptions to avoid crowding.

- **Layer 3 — Data context (JSON):** Structured data generated separately in Claude, including genre name, description, seminal artists, 15–20 milestone albums with release dates, 1–2 sentence descriptions, and tags. This makes the prototype feel real rather than AI-generated filler. Ravi used a custom MCP server (built in ~1 hour in Claude Code) to automatically fetch real album cover URLs from free sources (like Deezer), embedding actual artwork into the data file.

- **Using multiple tools in concert:** Rather than overloading one tool, Ravi uses Claude for data generation, Figma for wireframes, and Reforge Build for final prototyping. Each tool is given only the context it needs. This prevents "polluting" the prototyping tool with intermediary context and keeps each step clean.

- **The full-stack prompt:** Combining all three layers into one structured markdown prompt — functional requirements + attached wireframe + pasted JSON data — produces a prototype that is realistic, visually accurate, and architecturally modular. The result looked polished enough to test with real users.

- **Modular data files enable rapid personalization:** By instructing the tool to save data as a separate `data.json` file, Ravi could swap in a completely different dataset (e.g., replacing down-tempo with psychedelic rock) simply by pasting a new JSON file — no re-prompting, no redesign. This took ~15 minutes to generate a new genre dataset in Claude.

- **"AI slop" is detectable and avoidable:** Even with good UX, AI-generated placeholder images or generic content make prototypes feel inauthentic. Real album covers, accurate descriptions, and accurate artist data are what push a prototype from "feels like AI" to "feels like a real product."

- **MCP servers extend Claude's capabilities:** Ravi created a custom local MCP server in Claude Code to fetch album cover art from free APIs without requiring API keys. He also has one for location imagery (e.g., Eiffel Tower) for travel prototypes. These servers sit locally on his machine and are reused across projects.

- **The waterfall process isn't dead — it's accelerated:** What used to take 2+ weeks (spec → wireframe → build) now takes ~10 minutes. The steps are the same; the time cost has collapsed. The new model is less like an assembly line and more like a jazz band — everyone riffs off each other, roles blur, and leadership shifts dynamically.

- **PRDs still have value but don't have to come first:** PRDs answer questions that prototypes can't — what problem are we solving, what does success look like in metrics, how does this ladder to strategy. But the linear order (PRD → wireframe → prototype → build) is no longer required. Sometimes you prototype first, get customer signal, then write the PRD and link to the prototype from it.

- **The privilege of building throwaway work is now universal:** Previously, only the largest, most profitable companies could afford to build many things they'd never ship. AI prototyping democratizes this. A sign of working in a truly AI-native way: you're creating more stuff that never ships, because you're discovering the wrong answers cheaply and early.

- **Figma and visual design tools are not fading:** There are two types of thinking — textual and visual. Software is a visual experience and shouldn't be built without visual blueprints. Tools like Figma, Balsamiq, or even hand-drawn sketches remain valuable because visual prompts communicate spatial intent far more efficiently than text descriptions. Round-tripping between code and visual tools (Figma → code → Figma) is improving across Cursor, V0, and Figma itself.

---

## Use cases

- **PMs building prototypes of existing products** to test new features with real users without writing production code
- **User researchers** who need prototypes realistic enough to generate behavioral (not hypothetical) user responses
- **Designers** who want to move a wireframe quickly into an interactive prototype with real data
- **Vibe coders / non-engineers** who want more control over prototype structure and fidelity than a simple prompt provides
- **Anyone doing stakeholder demos** who needs a prototype that looks like the real product, not a generic AI mockup
- **Teams exploring solution spaces** before committing to a direction — building many throwaway prototypes cheaply to find the right answer
- **PMs working on content-heavy or data-driven features** (music, movies, travel, e-commerce) where realistic dummy data significantly affects how users engage with the prototype
- **Anyone wanting to personalize prototypes for different user segments** — swap JSON files to show a different genre, category, or persona without rebuilding the UI

---

## Patterns & frameworks

### The 3-Layer Context Engineering System
The central framework of the video. Instead of a single prompt, you provide three distinct types of context:
1. **Functional context** — A text-based mini-spec describing what the feature should do (sections, interactions, content types)
2. **Visual context** — A wireframe (Figma, Balsamiq, hand-drawn, screenshot) that shows spatial layout and design intent
3. **Data context** — A structured JSON file with real, accurate content (generated in Claude, enriched with image URLs via MCP servers)
All three are combined into a single structured markdown prompt for the prototyping tool, producing a modular, realistic, iterable prototype.

### Multi-Tool Orchestration (DIY Multi-Agent System)
Rather than asking one AI tool to do everything, Ravi uses each tool for what it does best:
- **Claude** → generate and enrich JSON data, run MCP servers for image URLs
- **Figma** → create visual wireframes/blueprints
- **Reforge Build** → take clean, prepared context and build the prototype
Each tool receives only the context it needs, keeping inputs clean and outputs high quality.

### Modular Data Architecture
Instruct the prototyping tool to save content as a separate `data.json` file rather than hardcoding it into the UI. This mirrors how real software separates front-end from data layer, makes the prototype more architecturally sound, and allows instant content swaps (e.g., different music genres, user personas, product categories) without touching the UI code.

### The Jazz Band Mental Model
Contrasted with the traditional "assembly line" (linear: spec → design → engineering → launch), the jazz band model describes how modern AI-assisted product teams work: everyone has a specialty, but roles overlap, people riff off each other's work, and leadership shifts fluidly based on what the moment needs. There is no fixed sequence — the best next step depends on what questions need answering.

### Prototype as Decision-Making Tool
A prototype's purpose is not to be pretty — it's to facilitate a specific decision. Before building, ask: *What decision does this prototype need to help make?* If the answer involves customer research, the prototype must achieve suspension of disbelief. If it's internal alignment, lower fidelity may suffice. This frames all subsequent choices about how much context engineering effort to invest.

### Sketch → Painting Analogy for Prototyping vs. Production
Prototyping is sketching; production code is oil painting. If you already know exactly what you want and are ready to deal with production complexity, skip the prototype and ship. But most of the time, artists sketch many studies before committing to a canvas. Prototyping gives you the freedom to explore unencumbered by production constraints — data structures, system architecture, existing technical debt.