# Reverse Engineer Just Got INSANE - Grow Like Lovable

Video ID: `xTTSg5qeJ6w`

## Summary
The video introduces three open-source/AI-powered reverse engineering tools that go beyond copying a competitor's code to copying their entire growth strategy and content approach. The core argument is that the code is the least valuable thing to copy — distribution strategy and content formats are where the real competitive advantage lies. Using the fast-growing API startup Zernio ($188K MRR in under a year) as a live case study, the presenter demonstrates how these tools surface insights that would take days of manual research. The video is most relevant to indie hackers, startup founders, content creators, and growth marketers who want an evidence-based way to understand what actually drove a competitor's growth.

## Key insights
- **REA (Reverse Engineer Anything)** is an open-source GitHub repo with ~480,000 stars that lets Claude Code analyze and rebuild any app by watching its network traffic — but copying code is framed as the *least* valuable thing to copy
- The real value is in reverse engineering **distribution strategy and content formats**, not the product itself
- **REA Growth** (by Trog) runs 13 steps of automated data collection for under $1 and builds a full growth timeline for any company — covering SEO keywords, paid ads, creator partnerships, and social posts
- Zernio grew from ~4 to ~1,200 Google visits/month between Oct–Dec 2024 by targeting low-competition, high-intent keywords (300–800 searches/month), e.g. "scheduling API for Twitter"
- REA Growth found **200 Google Ads** running for Zernio despite traffic tools showing almost none — longest ad had been running 206 days (a strong signal of profitability)
- Six AI creators (largest with 170K followers) all posted about Zernio on the **same day** (Oct 5), four days before their Product Hunt relaunch, all using the angle "build an AI voice agent in 6 minutes" — no visible ad labels
- Zernio's Google traffic **crashed from ~1,700 to ~300 visits/month** in February — later attributed by the founder to removing free tools that drove traffic but hurt conversions
- The playbook output ranks **10 plays by evidence strength and stage-fit**, flags plays that look good but lack supporting data, and gives a **14-day action plan** with one metric to check per channel
- **TubeLab skills** reverse engineer YouTube channels by comparing each video to that channel's own median views (last 3 months), not to the broader niche — anything 2x+ median = winner, under 0.5x = poor performer
- The **"threat news" format** (e.g. "Google just broke this") outperformed on 3 different channels in the AI/SEO niche — a format signal worth copying
- Neil Patel and Caleb Elku shared the **same hook formula**: specific number or news fact → what it means for you → what you'll learn by the end
- The "learn 80% of X in 14 minutes" format won on Ahrefs (6–13x normal views) but didn't travel to Neil Patel or Caleb — format performance is channel-specific, not universal
- Neil Patel's "744 AI articles" post (4x normal) is tagged **needs his asset** — you can't replicate it without a comparable test dataset
- TubeLab MCP costs $29/month, but most functionality (view counts, transcripts, channel lists) can be replicated free using **Firecrawl** (~120 of 1,000 free monthly credits per run)
- Key caveat: all data is **historic** — it shows what correlated with past growth, not what will work next or for a different audience/competitive landscape

## Use cases
- **Founders** validating whether to rebuild a tool vs. buy off the shelf (rebuild only if it's core to your product and doesn't fit how you work)
- **Growth marketers** auditing a competitor's full distribution stack (SEO, paid ads, creator deals, organic social) in one automated run
- **Content creators** identifying which video formats travel across multiple channels in their niche vs. which are channel-specific flukes
- **Agencies** building evidence-based growth strategies for clients by reverse engineering category leaders
- **Indie hackers** entering a new market who want to know which channels drove growth *before* committing 3 months to the wrong strategy
- **Early-stage startups** looking for a 14-day sprint plan with a single measurable outcome per channel
- **Developers** who want to replicate specific features of an app they use but that doesn't fit their workflow or budget

## Patterns & frameworks

**REA (Reverse Engineer Anything)**
Open-source tool that connects Claude Code to an MCP server and a set of analysis tools. Claude uses the target app normally, records network traffic, and separates *seen* facts (100% confirmed by evidence) from *best guesses* (inferred from clues) before writing any code. Output is a structured plan of how the app works.

**Seen vs. Guessed split**
A core quality signal in any reverse engineering output — findings are explicitly categorized as confirmed observations or inferences. This discipline prevents building on assumptions as if they were facts.

**REA Growth (13-step growth timeline)**
Automated skill that: (1) finds the month growth stepped up and stayed up, (2) lines it up against launches/funding/ad pixel dates, (3) pulls top 1,000 SEO keywords + buyer-intent questions, (4) pulls live ads across 4 platforms (60+ days running = winner), (5) ranks own social posts top-quarter vs. bottom-half, (6) runs a +2/−2 month window around each move to see what correlated with acceleration. Output: ranked playbook of 10 plays, unsupported plays list, and a 14-day plan with one metric per channel.

**60-day ad rule**
Any ad running for 60+ days is treated as a proven winner — nobody pays for a non-converting ad that long. Used to filter signal from noise in paid ad data.

**Channel-relative performance benchmarking (TubeLab)**
Instead of comparing videos across the whole niche, each video is compared to the *channel's own* median views from its last 3 months of long-form content. Thresholds: 2x+ = winner, under 0.5x = underperformer. This removes the confounding variable of channel size.

**Format portability test**
A content format is only worth copying if it wins on **2 or more channels**. If it only outperforms on one channel, it may be explained by that channel's specific audience rather than being a universally effective format.

**Anyone can copy vs. needs their asset tagging**
Each format is labeled based on whether replication requires a unique asset (large following, proprietary data, budget). Only "anyone can copy" formats are actionable for most people.

**14-day sprint with single metric**
For each recommended play, the output specifies one number to check on day 14 — keeping execution focused and making it easy to evaluate whether the play is working before doubling down.