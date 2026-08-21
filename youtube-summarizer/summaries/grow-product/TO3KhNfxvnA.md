# She Gets 5 Job Offers a Week on LinkedIn with Claude Code

Video ID: `TO3KhNfxvnA`

## Summary
Basha Kubitzka, a PM-turned-content-creator who grew from zero to 70K LinkedIn followers in six months, walks through her complete Claude Code-powered system for generating inbound job offers on LinkedIn. The core argument is that LinkedIn should be treated as a product — with a profile as a landing page, content as passive networking, and active outreach via comments and DMs — and that Claude Code skills and a persistent story bank dramatically accelerate every step. The episode is most relevant to PMs actively job searching, PMs wanting to build a personal brand, and anyone trying to get recruiters and hiring managers to come to them rather than the reverse.

## Key insights
- Basha receives an average of 5 real inbound job offers per week, including roles created specifically for her and positions not publicly listed — a direct result of her LinkedIn system, not just follower count.
- She taught a cohort of students the same system; by week 5, many were getting similar inbound results, confirming it is replicable.
- The LinkedIn profile should be treated as a **landing page, not a resume** — every element (banner, tagline, about, experience, skills) must sell the candidate to a specific type of hiring manager.
- There are three distinct ICP (Ideal Customer Profile) journeys for anyone landing on your profile: passive discovery via content, active search by a recruiter using boolean keyword search, and a hiring manager who saw you comment on their content. The common conversion bottleneck in all three is the **profile picture + tagline** pairing.
- Taglines must be targeted to a specific role category, not generic. Claude outputs three headline options; the recommended one for Basha was: *"Product Manager, API & Developer Platforms | Agentic AI, MCP | I help teams turn AI models into products developers build on | Founder, AI startup, $0→$7M, TechStars."*
- She uses a Claude Code skill called **JD Keyword Miner** that takes up to five job description URLs, extracts keywords by category, ranks them by coverage frequency, diagnoses whether the roles are focused enough (requires ≥75% overlap), and outputs a keyword brief. If overlap is too low, it stops and tells you to rethink your target roles.
- A second skill, **LinkedIn Profile Writer**, takes the keyword brief + current profile text and rewrites every section: headline (3 options), banner statement, about section (3 versions: skimmable/timeline/simple), featured section suggestions, and experience bullets quantified around outcomes rather than ownership.
- The about section's **first three lines are critical** — they are all that shows before "See more." They must hook the reader. The rest should be easy to skim with arrows, line breaks, or emojis rather than dense paragraphs.
- Experience bullets should lead with **numbers and outcomes** ("I shipped X → result Y"), never just responsibilities or things owned. Claude inserts brackets like `[X]` where real numbers are missing, prompting the user to fill them in.
- Skills sections should be treated differently by location: in-line skills under each job should be selective (40 skills under one role "looks terrible"); the standalone Skills endorsement section can be loaded with every relevant keyword since recruiters use it for boolean filtering and no one scrolls it critically.
- LinkedIn Premium is recommended during active job search for Open Profile (others can reach you without paying), InMail credits, and top-applicant visibility. Estimated ~$100/month for the Career tier.
- Content follows a **ToFu/MoFu/BoFu funnel**: Top-of-funnel (reach/viral posts, generic "how to X") grow new audiences; Mid-funnel (authority posts, personal "how I did X") build credibility; Bottom-of-funnel (lead gen) is for founders/sales. Job seekers should prioritize authority posts (2×/week) with one reach post, posting at least 3× per week.
- The structural formula for a high-performing post: **Hook → Bridge (story/struggle) → Meat (educational value/fix) → Mic Drop (2–4 line summary) → Engagement question or CTA.**
- Basha built a **LinkedIn post scraper using Apify** (third-party API marketplace) as a proxy to get around LinkedIn's scraping restrictions — the actor uses a proxy server so it is not tied to her LinkedIn account. She filters scraped posts by an **X Factor score** (how many times a post outperformed the creator's 30-day moving average), which surfaces genuinely high-quality posts regardless of follower size.
- She adds **Voyage AI embeddings** to scraped posts and images to compute similarity scores, allowing her to cluster visually and textually similar viral posts and identify repeatable formats.
- Content ideation starts with ICP definition: she describes her ideal follower/hiring manager in granular detail — their fears, dreams, vocabulary, season of life — and stores this in Claude Code's CLAUDE.md so every session inherits it.
- She defines **3–5 brand pillars** (e.g., AI agents, vibe coding, AI product management, personal stories) to keep content cohesive without being one-dimensional. For a job seeker, pillars should map directly to target role domains (e.g., API pricing, customer discovery, developer tools).
- Her **story bank** is a large markdown file inside Claude Code containing detailed personal stories, accomplishments, and context. Claude pulls from it when writing authority posts so the same stories don't have to be re-explained each session. Stories are added organically: after a session where she tells Claude a new story, she asks it to append the story to the bank.
- Claude Code is preferred over Claude.ai chat specifically because persistent skills (`.md` files), the story bank, and the CLAUDE.md context file make the system stateful across sessions — something not possible in a stateless chat interface.
- For **active outreach to hiring managers**: search the company's LinkedIn People page filtered by location + "Product Management" to narrow candidates; look for the team name in the job description; find peers (who report to the hiring manager) and engage their content first; time comments to be among the first on newly published posts; always apply through official channels first before reaching out directly.
- Connection request messaging tactics: reference the applied role, ask for a 15-minute brain-pick; appeal to their accomplishments; or use a playful hook ("Given you already eat three meals a day, why not spend one with me? I'll buy.").
- On content originality: templates (structure/format) are fair game without attribution; graphics inspired by others warrant a tag or permission request; word-for-word swaps are only done under pre-agreed "content swaps" between creator friends who cross-tag for mutual benefit.
- Claude's first draft is never final — the human's primary value-add is refining the **hook** and ensuring voice authenticity. Claude does the scaffolding; the human does the polish.

## Use cases
- **PMs actively job searching** who want inbound offers instead of spray-and-pray applications.
- **PMs with non-linear career paths** (founders, researchers, COOs pivoting to CPO) who need to reframe experience to eliminate red flags and turn career gaps into differentiation.
- **PMs targeting a specific domain** (API platforms, fintech, developer tools) who need keyword-optimized profiles aligned to 3–5 similar job descriptions.
- **Early-stage content creators on LinkedIn** who are stuck in the "spammy" or low-engagement phase and need a structured system.
- **PM founders or operators** who want to build authority in a niche without hiring a social media team.
- **Anyone using Claude Code** who wants to see a real, production-grade personal-brand harness built with skills, reference files, and a story bank.
- **Job seekers who want to bypass ATS black holes** by building relationships with hiring managers and peers before or during the application process.
- **Recruiters or hiring managers** who want to understand how sophisticated candidates are now gaming LinkedIn search.

## Patterns & frameworks

**Three-Component LinkedIn System**
Profile (landing page) → Content (passive networking) → Active Outreach (comments + DMs). Each component feeds the others: content drives profile visits; profile converts visits into DMs; DMs convert to interviews.

**Three ICP Journey Model**
Maps three distinct paths a hiring manager or recruiter takes to your profile — passive content discovery, active recruiter keyword search, and hiring manager who saw you comment. All three converge at the same bottleneck: profile photo + tagline. Optimizing that pair is the highest-leverage action.

**JD Keyword Miner Skill (Claude Code)**
Input: up to 5 job description URLs. Process: extract terms by category, normalize, rank by cross-JD coverage, diagnose focus (flags if <75% overlap). Output: keyword brief with top skills, suggested phrases, role intent signals, and gaps. Used as input to the profile rewrite skill.

**LinkedIn Profile Writer Skill (Claude Code)**
Input: keyword brief + raw current profile + context questions. Process: maps keywords to truthful experience, identifies gaps (asks clarifying questions), optionally runs an "edge pass" to flip red flags into strengths. Output: rewritten tagline (3 options), banner statement, about section (3 formats), featured section ideas, experience bullets with outcome quantification, and recommended LinkedIn skills.

**ToFu/MoFu/BoFu Content Funnel**
- **ToFu (Reach):** "How to X" — shareable, non-personal, grows new audiences.
- **MoFu (Authority):** "How I did X" — personal story + expertise, builds credibility with hiring managers.
- **BoFu (Lead gen):** For founders/sales; irrelevant for most job seekers.
Job seekers: 2 authority posts + 1 reach post per week minimum.

**Viral Post Structure Formula**
Hook (first 2–3 lines visible in feed) → Bridge (story/struggle narrative) → Meat (educational value, the "fix") → Mic Drop (2–4 line summary landing the key truth) → Engagement question or CTA. The image and hook must work together to stop the scroll before anything else matters.

**X Factor Scoring for Content Research**
For any scraped creator post: X Factor = post performance ÷ creator's 30-day moving average performance. A score of 24× means the post outperformed the creator's typical output by 24×, signaling intrinsic content quality independent of audience size. Used to identify formats worth adapting.

**Story Bank (Claude Code Persistent Context)**
A large markdown file of personal stories, accomplishments, and contextual details stored in the Claude Code project. Claude draws from it automatically when writing authority posts. Grows organically: after each session involving a new story, user asks Claude to append it. Eliminates the need to re-explain context in every session.

**Apify-as-LinkedIn-MCP Proxy**
Since LinkedIn has no official MCP, Basha uses Apify's third-party actors (built by external developers using proxy servers) to scrape LinkedIn posts without being tied to her account. Augmented with Voyage AI embeddings for image and text similarity clustering — enabling visual/thematic grouping of viral post formats.

**Active Outreach Funnel (Hiring Manager Targeting)**
1. Find team name in job description → search company LinkedIn People page by location + "Product Management" → filter to ~10–30 people. 2. Identify peers (who likely report to the hiring manager). 3. Engage their recent content with value-adding comments + open-ended question. 4. They see your tagline in the notification. 5. Send connection request referencing the applied role. 6. Request a short call to "pick their brain." Always apply through official channels first.