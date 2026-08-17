# How I Run My 1.5M+ Follower Content Business With Codex | Riley Brown

Video ID: `N34zz1-RSGw`

## Summary
Riley Brown, an AI educator with 1.5M+ followers across platforms, walks through his complete content creation workflow using Codex (an AI agent platform that stores data locally) and a suite of custom skills he has built over time. The core argument is that AI tools should be used to improve content *quality*, not just output volume — batching more content leads to soulless work, while using AI for deeper research and better packaging leads to sustainable, high-quality creation. The video is most relevant to content creators, solo operators, and anyone building AI-assisted workflows who wants to see a real, working production system rather than a theoretical one.

---

## Key insights

- **Quality over quantity**: Riley explicitly rejects the "batch more content" mindset. His goal is 4 long-form + 5 short-form videos per week, but only if quality stays high. He believes "the moat is quality over a long period of time — batching will make it soulless."
- **Skills are discovered, not designed**: He never sits down to plan what skills to build. He uses AI to do something useful, and if he does it repeatedly, he tells Codex "turn this into a skill." Skills emerge organically from actual usage.
- **YouTube is the research hub**: His YouTube Researcher skill uses the Supadata API to pull full transcripts from any YouTube video in ~1 second, and can scrape an entire channel in ~30 seconds using sub-agents. This replaces yt-dlp (which downloads full video files) and is far faster.
- **Hook-first structure with a twist**: The intro/hook is scripted using AI, but the body of the video is free-flowing. He often films the hook *last*, after finishing the main video, so the intro accurately reflects what he actually covered — including tangents.
- **Hook outline as a transferable format**: He uses AI to condense high-performing YouTube videos (e.g., Alex Hormozi's) into a "hook outline" — just the intro structure and a high-level outline. He then applies that format to his own ideas, essentially borrowing proven structural templates without copying content.
- **BRENS framework for intros**: Big, Relatable, Easy, New, Safe — a checklist for what makes a strong video intro. "Safe" (reassuring viewers their time won't be wasted) is most important for videos over 30 minutes.
- **Thumbnail workflow via Paper + Codex**: He scrapes top-performing thumbnails from creators like Alex Hormozi and Dan Martell using Codex, drops them onto a Paper board (an AI-native Figma alternative), then uses Paper's built-in image generation to swap his face onto the existing thumbnail composition. He iterates with prompts like "smooth the face, add a white-orange glow outline."
- **Chaining multiple skills in one prompt**: A single Codex prompt can invoke multiple skills — e.g., the image puller skill (via SerpAPI/Google Images) combined with the Remotion best practices skill to auto-pull logos and generate a branded animation graphic in one step.
- **Remotion for intro animations**: He uses a Remotion plugin inside Codex plus a custom "Remotion best practices" skill (with his brand style embedded) to generate high-quality animated intro graphics that get exported and overlaid in video editing.
- **Excalidraw diagrams from voice**: He uses Wispr Flow (voice-to-text) to verbally dump all his ideas while walking, then runs those notes through his Excalidraw diagrams skill to generate ~80% of the diagrams he'll use in the video. He spends 20–30 minutes editing the rest.
- **Notion + in-app browser as a unified workspace**: Codex's in-browser capability lets him create and open Notion database entries (video scripts, outlines) without leaving the app. He treats Notion as a video production database — long-form and short-form tracked separately.
- **Typefully integration for Twitter**: A Typefully skill drafts tweet ideas on the fly whenever he comes across something interesting. Every Monday he reviews and fires them off — passive Twitter content accumulation.
- **Skill testing methodology**: He never reads skill files manually. He tests by outcome: run the skill, check the output, tell AI what went wrong, ask it to update the skill, clear context, test again in a new chat. Outcome-based iteration, not prompt engineering.
- **Claude vs. GPT for transcript pulling**: GPT models refuse to reproduce YouTube transcripts due to copyright concerns. Claude models do it without hesitation. For this use case he has switched to Claude.
- **Local storage as a differentiator**: Unlike ChatGPT (cloud-stored uploads), Codex stores all files locally, which matters for privacy and for giving the agent access to local files and computer control.
- **Chorus — his own product**: A multi-agent platform that lets teams use AI agents in Slack and iMessage. He is currently monetizing it primarily through consulting (implementing agents for businesses) rather than direct SaaS sales.
- **Agent teams in Slack**: He runs a personal "My Agents" Slack channel with agents like a Chief Marketing Officer (sends updates), Content Man (analyzes competitors' content and generates video ideas), and a Peter Yang bot trained on all of the host's YouTube videos.
- **Codex as single-player**: He acknowledges that Codex is a single-player experience — making these creative workflows multiplayer (team-level) is the next unsolved problem, which Anthropic and others are actively working on.
- **High-risk vs. low-risk skill governance**: For creative workflows, he lets AI "cook" with no oversight. For mission-critical tasks (payments, client deliverables, sensitive documents), he has a review process where someone else audits the skill.

---

## Use cases

- **Solo content creators** building a repeatable production system across YouTube, Instagram, TikTok, and Twitter
- **YouTubers** who want to improve their hook and intro quality using competitive analysis of top creators
- **Anyone making thumbnails** who wants to shortcut design by remixing high-performing templates rather than starting from scratch
- **Podcasters or video creators** who want to script only the intro and improvise the rest, using AI to generate the hook structure from a transcript
- **Marketers or researchers** who need to quickly scrape and analyze YouTube channels for competitive intelligence
- **Builders creating AI agents for Slack** who want a real-world example of what a personal agent team looks like
- **Consultants or agency operators** using an AI-native product (Chorus) to deliver agent implementation services to business clients
- **Content creators who struggle with Twitter consistency** — the Typefully-as-passive-queue pattern applies broadly
- **Anyone building a personal knowledge/skills system** who wants a practical framework for turning repeated actions into reusable agent skills

---

## Patterns & frameworks

**BRENS Framework (hook/intro checklist)**
Big, Relatable, Easy, New, Safe. A checklist for evaluating and constructing video intros. Each element increases viewer likelihood to keep watching. "Safe" — assuring viewers their time is well-spent — is most critical for long videos (30+ min). Apply each letter as a filter when writing or reviewing an intro.

**Hook Outline Template Method**
Find a high-performing video from another creator → use AI to condense it into a "hook outline" (just the intro structure + high-level body outline) → apply that structural template to your own content idea. Borrows proven formats without copying content. Separates packaging from ideas.

**Film the Hook Last**
Record the body of the video first (free-flowing, passion-driven), then analyze the full transcript with AI to identify key themes and tangents, then film a scripted hook/intro that accurately reflects what was actually covered. Prevents intro-body mismatch and allows the best tangents to surface naturally.

**Outcome-Based Skill Iteration Loop**
Run skill → check output → if wrong, tell AI what failed → ask AI to update the skill → clear context (new chat) → retest. Never manually edit skill files. Repeat until the skill reliably produces the correct outcome. Model-agnostic: optimize for outcomes, not prompt syntax, because model updates will change what syntax works anyway.

**Discover-Then-Codify Skill Building**
Never pre-plan which skills to build. Use AI to accomplish tasks naturally. When a useful action repeats, say "turn this into a skill." Over time, the skill library reflects actual usage patterns rather than hypothetical needs. Skills that stop being useful are abandoned.

**Thumbnail Remix Workflow**
Scrape top-performing thumbnails from target creators (via Codex + Paper) → place on a visual board → use AI image generation to swap your face/likeness onto the composition → iterate with style-reference prompting (drag reference thumbnail onto board, prompt "make it look like this"). No manual design from scratch.

**Personal Skill Stack as Competitive Moat**
Personalized skills (YouTube researcher, Excalidraw diagrams in your style, Remotion with your brand colors, thumbnail designer tuned to your face) are non-transferable and compound over time. This is framed as why AI skills are displacing generic SaaS — no off-the-shelf tool can be as tailored as a personally iterated skill.

**Multi-Agent Slack Channel (Agent Team Pattern)**
Create named agents with distinct roles (CMO, Content Analyst, etc.) in a dedicated Slack channel. Each agent has a persona and specialized knowledge. You interact with them by tagging. Agents run in the cloud independently of your local machine — solving the "computer must be on" limitation of desktop agents like Codex.