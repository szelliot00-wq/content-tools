# 10 GitHub Repos to 10x Your AI Motion Graphics

Video ID: `aD9X6Lc3dVk`

## Summary
The video demonstrates 10 GitHub repositories that, when paired with Claude (Anthropic's AI), dramatically elevate the quality of AI-generated motion graphics from generic "AI slop" to professional-grade video content. The presenter, Matt, tested roughly 87–100 different repos and distilled them into this list of 10 best-in-class tools, each solving a specific visual quality problem. The core argument is that Claude alone produces mediocre motion graphics, but feeding it specialized repos as context unlocks cinematic, stylized, physics-driven, and 3D outputs. The video targets content creators, marketers, educators, and product teams who want to produce high-quality explainer or promotional videos cheaply and quickly.

## Key insights
- **How to use any repo with Claude**: Copy the GitHub repo URL, paste it into Claude (or ChatGPT), and instruct it to "use this repo to create a video about X" — no coding required.
- **Lemo Opus** contains 66 distinct film styles (paper cut, 80s anime, ink wash, retro terminal, isometric infographic, etc.) that Claude can apply directly or choose autonomously based on context.
- **Three.js** upgrades flat 2D graphics to true 3D — including bar charts made of stacked cash, self-generated 3D models with reflections, particle effects (e.g., spiral galaxies), and camera fly-through scenes.
- **Pixel FX** provides a pixel art renderer with a built-in effects library (explosions, weather, lightning, northern lights) and supports both artistic and educational explainer styles.
- **Blender** has an MCP (Model Context Protocol) integration, letting Claude control the full Blender toolset — shaders, materials, effects, 3D scene construction, camera movement — to produce CGI-quality output. Matt one-shotted all Blender examples (population comparisons, solar panel explainer, headphone exploded view) from a single prompt.
- **Awesome Opus 5.5 Videos** and **Opus Video Prompts** are two prompt packs using HTML, WebGL, and Three.js to generate stylized scenes — mosaic effects, flat science explainers, and smooth UI-element-based motion graphics drawn from proven web design patterns.
- **Claude Animation Base** centers on a "Claubot" character with built-in emotions, animation guides, timing references, and storyboarding support — particularly suited to AI-topic explainer content similar to what appears on Instagram.
- **React Rapier** combines React and Three.js to add real physics — Jenga tower knockdowns, domino chains, and Galton board (binomial distribution) visualizations — making it ideal for science and math explainers.
- **React Postprocessing** applies post-render filter stacks for glow, depth-of-field blur, film grain, lens coloring, and glitch effects, adding a premium cinematic feel (demonstrated with a glowing electron shell animation for a sodium atom).
- **Librosa** analyzes audio to detect beats, then synchronizes all visual transitions to the music — a technique common in software product launch videos that makes output feel polished and intentional.
- **Video Shotcraft** functions as a promo video template engine with 124 pre-built recipes and formats derived from real product launch videos; Claude selects the best template automatically.
- Matt promotes an **Applied AI Mastermind** community offering access to his full skill selector tool (covering all 87+ repos), additional video production assets, and claimed $400k+ in AI tool savings.

## Use cases
- **Tech explainer videos**: Three.js 3D infographics, isometric Lemo Opus styles, or Pixel FX weather system breakdowns.
- **Documentary/historical intros**: Ink wash or paper cut Lemo Opus styles for cinematic, atmospheric openers.
- **Science and math education**: React Rapier physics simulations (Galton board, dominoes) and postprocessing glow effects for electron/atom visuals.
- **Product launch videos**: Librosa for beat-synced audio-visual transitions + Video Shotcraft's 124 promotional templates.
- **AI content and social media**: Claude Animation Base's Claubot character for Instagram-friendly, personality-driven AI explainers.
- **CGI-style brand content**: Blender MCP for high-quality 3D scenes — population comparisons, product breakdowns, mechanism explainers — previously requiring thousands of dollars and specialist labor.
- **UI/software demo videos**: Awesome Opus / Opus Video Prompts' proven UI element library for sleek, professional screen-based motion graphics.
- **Artistic title sequences**: Paper cut, pixel art, or mosaic styles for storytelling intros and narrative video openers.

## Patterns & frameworks

**The "Repo as Magic Dust" Pattern**
Treat GitHub repos as capability modules injected into a base LLM. Claude alone = mediocre output; Claude + specialized repo = professional output. The workflow is: find the right repo → paste its URL into Claude → describe your desired video → let Claude apply the repo's assets, styles, or physics engine.

**Pre-Created Assets Over Pure Generation**
A recurring theme across multiple repos (Video Shotcraft, Opus Video Prompts, Claude Animation Base): human-designed templates, UI elements, and animation assets produce higher-quality results because the creative work was done by humans and AI simply selects and assembles. This reframes AI's role as a curator/compositor rather than a pure generator.

**Style-First Workflow (Lemo Opus Framework)**
Choose your visual style before scripting content. With 66 styles available, the approach is: match the style to the emotional register of the content (ink wash for history, retro terminal for tech/sci-fi, isometric for explainers) rather than generating and then styling.

**The Skill Selector System**
Matt's proprietary meta-layer: describe your desired output to Claude, and it evaluates all 87+ repos/skills to recommend the best combination. This is a routing/orchestration pattern — a meta-prompt that maps intent to tools — sitting above the individual repo layer.

**Post-Processing as Quality Multiplier**
React Postprocessing demonstrates a compositing-layer pattern: render the base scene first, then run it through stacked filters. This separates content generation from visual polish, allowing quality upgrades without regenerating the underlying scene — a pattern borrowed from professional VFX pipelines.