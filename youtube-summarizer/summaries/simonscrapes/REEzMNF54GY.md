# I taught Claude how to build my carousels and it's INSANE

Video ID: `REEzMNF54GY`

## Summary
The video demonstrates a custom Claude-based AI system for generating on-brand social media carousels at scale, arguing that the core failure of most AI-generated carousels is the absence of a proper design system rather than bad prompts. The creator walks through a multi-stage agentic workflow that handles everything from research and brand voice to visual identity and slide generation, producing platform-ready LinkedIn and Instagram carousels. It is most relevant to solo creators, content marketers, and agency operators who post carousels regularly and need brand-consistent output without spending 3–4 hours per post in Canva.

## Key insights
- **Carousels outperform other formats significantly:** A study of 1.5 million LinkedIn posts found carousels generate ~3x the reach of standard text posts, driven by dwell time (15–20 seconds vs. 8–10 seconds for single images/text).
- **Instagram gives carousels a second distribution window** that reels and single images never receive, effectively doubling exposure.
- **8–10 slides is the consistent engagement sweet spot** for carousels across platforms.
- **The real problem with AI carousels is not the copy — it's the lack of a design system.** No brand continuity, identical layouts across slides, and irrelevant AI images are the failure modes that kill engagement.
- **The fix is a "visual identity token" system:** fonts, accent colors, layout grids, and templates are stored as a single source of truth and enforced on every slide generated, but layouts are deliberately varied to maintain engagement.
- **The system handles multiple input sources:** uploaded video, topic/idea (triggers trending research), LinkedIn feed scrape, web article URL, local audio file (transcribed), PDF, or an existing post to adapt.
- **Trending research skill searches Reddit, Twitter/X, and the web** for real discussions matching a topic — so research is automated, not fabricated.
- **Brand voice is systematized:** the tool quizzes the user, grabs writing samples, analyzes tone, and produces a reusable voice profile document.
- **Visual identity setup takes 10–15 minutes the first time** but produces a reusable configuration file used on every subsequent run. It includes palette, typography, and slide templates (hero, body, CTA variants).
- **Reference image workflow:** Users paste in screenshots of posts or styles they admire; the system generates templates using the user's brand colors instead of the original creator's colors, effectively emulating a style without copying it.
- **Image generation is handled by a dedicated sub-agent** that receives a slide plan and generates images separately from the main content agent, keeping context clean.
- **Three image generation modes:** pure HTML templates (no AI image generation), AI-generated image embedded in HTML template, or real screenshots/photos automatically extracted from a source URL.
- **Human-in-the-loop checkpoint** exists before visuals are generated — the user reviews the slide plan, caption, and content angles to confirm value before committing to image generation.
- **Output includes a LinkedIn/Instagram preview mockup** where the full carousel can be browsed as if reading it live on the platform.
- **Canva Magic Layers integration** as a final manual step: AI-generated images are imported and converted into editable layers for small tweaks — moving logos, resizing text — turning a 95% draft into a finished, indistinguishable-from-human post.
- **The system is positioned as overkill for one-off carousels** (just use Canva) but highly valuable for creators posting weekly across multiple platforms.
- **Multi-brand/multi-client support** is built in via a broader "Aentic operating system" framework.
- **Current image generation uses OpenAI GPT Image 2.0**, with Gemini as an optional alternative. Social publishing uses Zernio API.

## Use cases
- **Content creators and personal brand builders** posting weekly LinkedIn or Instagram carousels who want brand consistency without manual Canva work.
- **Social media managers or marketing agencies** running content for multiple clients who need to replicate a branded design system at volume.
- **Founders or solopreneurs** who have valuable expertise but lack design skills and time to produce polished visual content.
- **Businesses repurposing existing content** — turning blog posts, videos, audio recordings, or PDFs into platform-ready carousels without starting from scratch.
- **Teams that lack a defined brand identity** and need a fast, structured way to generate brand guidelines, voice profiles, and design tokens from scratch.
- **Creators who want to test content angles at scale** — rapidly producing multiple carousel drafts and selecting the best-performing ones rather than betting 4 hours on a single post.
- **Anyone monitoring competitor or industry trends** who wants to generate timely carousel content from Reddit/Twitter discussions without manual research.

## Patterns & frameworks

**Design System Enforcement Pattern**
The core framework: store visual identity as reusable tokens (colors, fonts, grid rules, layout templates) and inject them as hard constraints into every generation call. Variation in layout is allowed and deliberate; the underlying system is non-negotiable. This separates "consistent brand" from "identical and boring."

**First-Run Onboarding → Reusable Config File**
A one-time setup (5–25 minutes) builds three assets: a brand voice profile, a visual identity config, and platform/language preferences. Every subsequent run loads the config and skips setup entirely. Reduces per-carousel overhead from hours to minutes.

**Reference Image → Template Conversion Workflow**
Users supply 3–5 screenshots of visual styles they admire (from Instagram, Figma templates, Canva, etc.). The system extracts structural layout patterns and regenerates those templates substituting the user's brand colors and fonts — style emulation without copying.

**Scenario-Branching Content Pipeline**
Input type determines the workflow path (topic → trending research; video → transcription; URL → screenshot extraction; etc.). Each scenario invokes the appropriate sub-skill while the downstream visual generation pipeline remains constant.

**Designer Sub-Agent + Image Generator Sub-Agent Split**
Content planning and visual generation are handled by separate agents with isolated context. The designer agent builds a narrative arc, stress-tests the hook, and produces a slide plan. The image agent receives only that plan and generates images. This keeps prompts focused and context windows clean.

**95% Draft + Manual Finish Layer**
Rather than attempting perfect AI output, the system explicitly targets a 95% complete carousel, then routes the user to Canva Magic Layers for the final 5% of small edits. This is a deliberate quality/effort tradeoff that avoids endless reprompting loops.

**Human-in-the-Loop Checkpoint**
A mandatory review gate before image generation where the user approves the slide plan and content angles. Ensures the carousel delivers genuine value before expensive compute resources are used and before anything is published.