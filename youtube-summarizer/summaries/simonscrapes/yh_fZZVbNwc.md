# I Taught Claude Code to Build You a Personal Brand, Watch This…

Video ID: `yh_fZZVbNwc`

## Summary
The video demonstrates how to use Claude Code to build a system that makes AI-generated content sound and look like a specific person's brand, rather than generic AI output. The creator argues that the key to better AI content is not better prompts, but establishing three persistent brand context files: a voice profile, a body of work document, and a visual identity system. The framework is built once and then feeds into every future content output automatically. It is most relevant to solopreneurs, content creators, consultants, and business owners who produce regular content and want AI assistance that reflects their authentic voice and visual identity.

## Key insights
- **The core problem**: Claude doesn't know who you are by default, so AI content is competent but impersonal — it could belong to anyone. The fix is brand context files, not better prompts.
- **Three files solve this**: voice profile (`voice-profile.md`), body of work document, and a visual identity/tokens system — all stored in a `brand-context` folder Claude reads every time.
- **Voice profile extraction**: An 80/20 rule applies — 80% of brand voice comes from personality (stance, anti-corporate views, opinions, communication style), not just writing rules. The skill asks 10–15 minutes of structured questions across personality, strategic framework, and example collection.
- **Four voice extraction methods**: (1) import existing brand voices, (2) extract from pasted raw content samples, (3) build from scratch via questions, (4) scrape from LinkedIn/website URLs (requires scrapers).
- **Best voice examples come from transcribed speech**: Podcast recordings and video transcripts produce the most accurate voice profiles because they capture natural spoken patterns, filler words, and pacing.
- **AI detector validation**: A LinkedIn post generated with the personalized voice profile scored only 12.2% probability of being AI-generated, demonstrating that personalization reduces AI detection flags.
- **Voice profiles are living documents**: The creator updates theirs most frequently of all files. Voice evolves — how you wrote 3 months ago differs from today. Platform-specific sample guides (LinkedIn, School, etc.) add further nuance.
- **Body of work = foundational concepts**: 7–12 recurring themes or opinions you return to repeatedly across podcasts, posts, and conversations. Each has a single-line thesis plus three supporting opinions.
- **Body of work extraction method**: Pull past content from chats, long-form posts, video/podcast transcripts, sales/about pages → Claude identifies recurring ideas → collaborative refinement → single markdown output file.
- **Practical body of work example**: The creator's core thesis is "Claude Code is the execution layer for all knowledge work," supported by concepts like skills as individual IP units and "underneath everything it's all just files."
- **Body of work gets you 60–70% of the way there**: Combined with the voice profile, content is anchored to your point of view rather than requiring repeated re-explanation of angles to the AI.
- **Visual identity is reverse-engineered from a paid branding agency**: The creator paid an agency, then turned that process into a Claude Code skill (available as a paid extra in Aentic Academy).
- **Visual identity outputs**: Color palettes, typography with scaling rules, mock use-case dashboards, logo design, brand values, actual font files, and a `tokens.json` file Claude Code reads to lock in consistent design decisions.
- **Design tokens eliminate variability**: By injecting `tokens.json` into skills like a LinkedIn carousel creator, every visual output uses the same colors, fonts, and mastheads without manual art direction.
- **Visual references are non-negotiable**: Uploading 3–5 style references (carousel examples, brand book PDFs, website screenshots, Figma palettes) is critical — skipping this produces templates that won't match your desired aesthetic.
- **Marketing brand voice** is a free skill available via link in the video description; the **visual identity skill** is a paid extra inside the Aentic Academy community.

## Use cases
- **Solopreneurs and personal brand builders** who want consistent LinkedIn, Instagram, and short/long-form content that sounds unmistakably like them
- **Consultants and coaches** who frequently explain the same core frameworks and want AI to reflect their established intellectual positions automatically
- **Business owners** creating branded content across multiple platforms (LinkedIn carousels, Instagram reels, ad creatives, slide decks) who can't art-direct every asset manually
- **Content creators moving from generic AI output** who are frustrated that their posts sound like anyone else's
- **Podcast guests and video creators** who have transcribable material that can be mined for authentic voice patterns
- **Anyone building a brand from scratch** who doesn't yet have strong existing content but wants to establish a consistent identity from the start
- **Teams or agencies** managing brand content for clients who want a repeatable, systematized process for brand voice and visual consistency

## Patterns & frameworks

**Three-File Brand Context System**
A persistent folder (`brand-context/`) containing three markdown/JSON files that Claude reads on every session: `voice-profile.md` (how you sound), `body-of-work.md` (what you think and why), and `tokens.json` + visual assets (how you look). Built once, it passively improves every future output.

**Marketing Brand Voice Skill (slash command)**
A structured 10–15 minute interview-style skill that extracts brand voice through three sequential phases: (1) personality extraction (stance, communication style, values), (2) strategic framework (ICP, positioning, tone), and (3) example collection (paste in real content or transcripts). Outputs a voice profile markdown file and three test samples across email, LinkedIn, and landing page formats.

**Body of Work Discovery Process**
Not a formal skill but a prompted collaborative process: gather past content → Claude identifies recurring themes → refine into 7–12 foundational concepts → each concept gets a one-line thesis + three supporting opinions → output is a single markdown file. Running this against your last 30–90 days of AI conversation history is a recommended shortcut.

**Design Token Architecture**
Visual identity is captured not just as a PDF brand book but as machine-readable `tokens.json` containing color palettes, typography, and layout rules. These tokens are injected into content-generation skills (carousel creators, slide generators, thumbnail makers) to enforce visual consistency without manual intervention — analogous to a CSS design system applied to AI content generation.

**Reference-First Visual Identity Extraction**
Rather than defining a brand visually from scratch, the visual identity skill asks for 3–5 external references (admired carousels, brand PDFs, website screenshots) and extracts palette, typography, and design moves from them. This reverse-engineering approach produces more aesthetically coherent results than abstract preference questions alone.