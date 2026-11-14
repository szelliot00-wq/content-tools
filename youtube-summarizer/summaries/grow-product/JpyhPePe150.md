# Build a Claude Code Agent That Talks to Your Churned Customers

Video ID: `JpyhPePe150`

## Summary
Greg Greiner (former CPO at Bolt, Head of Product at Uber for Business, now CEO at AI company Wooven) demonstrates how PMs can use Claude Code to build an AI-powered email outreach agent that holds personalized, back-and-forth conversations with churned or lapsed customers at scale. The core argument is that AI enables a "1000x" expansion of customer research capacity — from 7–8 customer conversations per month to tens or hundreds of thousands — without requiring armies of researchers. The video covers building the agent live (in ~30 minutes), adding evaluation loops for quality control, and situating this tool within a broader AI-enabled research strategy. It is most relevant to PMs, founders, and growth-focused operators at companies with product-market fit who want to systematize discovery.

## Key insights
- **Scale leap**: A CPO at Bolt was happy talking to 7–8 customers/month; AI enables thousands to hundreds of thousands of conversations per month, generating insights at a population level rather than a sample level.
- **Email beats in-app for lapsed/churned users**: Lapsed customers aren't in your app anymore. Email reaches them where they already are daily, and research campaigns see 20–40% response rates — far higher than in-app AI chat.
- **Response speed is a conversion lever**: Wooven found that adding delays to AI replies caused reply rates to drop "precipitously." People leave their inbox quickly, so near-instant AI responses are critical for maintaining conversation momentum.
- **Plain-text, single-question emails outperform**: The best outreach emails are simple, plain-text, ask one focused question relevant to where the user is in the journey, and let the conversation branch naturally — not survey-style multi-question blasts.
- **Four lifecycle touchpoints**: (1) Sign-up abandonment (highest volume, lowest response rate), (2) mid-trial check-in, (3) trial non-converters (offer incentive here — e.g., 20% off — to boost response rate and capture fence-sitters), (4) churn/cancellation win-back.
- **Incentives are dual-purpose**: Offering a discount to churned users who share feedback both increases reply rate and converts fence-sitters who were already reconsidering — the people who respond for the incentive were already close to coming back.
- **Build evals into the loop, not just the output**: Greg live-coded an eval step in Claude Code that checks "groundedness" (whether the AI's response is backed by actual documentation) before auto-sending. If it fails, the agent regenerates with the failure as input and saves a draft for human review rather than stopping the whole process.
- **LLM-as-judge requires specificity**: Generic "did the AI do anything wrong?" evals don't work at scale. You need to trace every specific action the AI took and link it back to the explicit instruction that authorized it — especially because LLMs are biased toward pleasing users (the "free truck" anecdote about a car dealership chatbot).
- **Learn from successes, not just failures**: When the AI converts a customer in a topic where almost no one converts, analyzing *why that response worked* is as valuable as analyzing failure traces.
- **Tech stack is accessible**: The demo used Gmail MCP + a CSV of customer data + a CLAUDE.md file with company policies and programs. Can scale to Postmark, Segment, or Snowflake. Buildable by a single PM in ~30 minutes.
- **AI-native team process**: At Wooven (4 people), the team spends time in live discussions, records transcripts, and feeds those + whiteboard diagrams into an AI skill that generates PRDs, creates Linear tasks, and spins up agents — minimizing keyboard time and maximizing substantive product debate.
- **PM-to-engineer ratios are inverting**: Greg's most productive period was 1 PM to 25 engineers at Uber. AI now lets a team of 3–5 engineers produce the output of 20–25, so small pods with tight alignment beat large fragmented teams.
- **The hardest part remains unchanged**: Building quickly and with good quality is now easy with AI. Building the *right thing* is still hard — that's where human judgment and discussion time should be concentrated.
- **Internal vs. customer-facing AI quality bars are very different**: Internal tools can tolerate rough outputs because a human reviews before anything ships. Customer-facing AI requires sandbox testing, guard rails, regression testing on model upgrades, and ongoing human QA — not just deploying and hoping.
- **Conversion data layered on top of research**: The Ancestry.com example showed that combining conversation themes with post-conversation conversion rates reveals which concerns are addressable via messaging (e.g., shipping confusion) vs. which are deep product problems (e.g., subscription confusion persists even after AI addresses it).

## Use cases
- **Trial abandonment recovery**: Users who signed up and started a trial but never converted — reach out to understand blockers and potentially offer incentives.
- **Onboarding drop-off**: Users who entered an email but never completed account creation or selected a program.
- **Cart/checkout abandonment**: E-commerce use case (Ancestry.com DNA kit example) — reach out after email capture but before purchase completion.
- **Active user feature non-adoption**: User explored an upsell or new feature but didn't convert — targeted outreach while intent is fresh.
- **Lapsing users**: Users whose usage has decreased over recent weeks — reach out before they fully churn.
- **Post-cancellation win-back and research**: The highest-signal audience; they've made a decision and have clear reasons — combine incentive with open-ended research.
- **PM wanting to scale discovery without a research team**: Solo PMs or small product teams at startups with product-market fit who lack a formal UX research function.
- **B2B PMs with large B2C user bases**: Cases like Bolt where you have millions of end consumers alongside business clients — impossible to personally talk to at scale without automation.
- **Any PM who wants to build a living, tagged inbox of customer signals** to later query (e.g., "find everyone who mentioned Feature X" before a launch).

## Patterns & frameworks

**Scaled conversational research loop**
AI sends personalized outreach → customer replies → AI responds instantly with follow-up questions → insights are classified and aggregated → periodic research report delivered over Slack. The key mechanism is that email's asynchronous nature gives the AI time to run quality evals before each reply, something impossible in synchronous chat.

**Four-touchpoint lifecycle email cadence**
A repeatable map for where to insert AI research conversations: (1) top-of-funnel sign-up drop, (2) mid-trial check-in, (3) trial non-converter (with incentive), (4) post-churn. Each touchpoint has different volume, response rate, and insight density tradeoffs.

**Groundedness eval loop**
Before auto-sending any AI response: run an LLM-as-judge eval checking whether every claim in the response is grounded in documented company policies/FAQs. On failure: feed the failure reason back into a full regeneration run (not a patch), then either auto-send the new version or save as a draft. Never just stop the pipeline on failure.

**Trace-based quality analysis (successes + failures)**
Rather than only reviewing when things go wrong, treat high-performing outlier responses (unexpected conversions in typically-low-convert topics) as equally important signal. Analyze the specific action sequence that led to that outcome to encode it as a pattern.

**Discussion-to-PRD-to-agent pipeline (AI-native team process)**
Small team meets synchronously → records transcript + whiteboard diagram → feeds both into an AI skill → AI generates detailed PRD, creates Linear tasks, and kicks off relevant agents. Humans spend time on the high-judgment debate; AI handles the documentation and scaffolding.

**Sandbox regression testing before model/prompt upgrades**
For customer-facing AI: before any upgrade, run the new version on a trusted sample dataset in a non-production environment, check that guard rails pass at the same or better rate as before, do spot QA for unexpected regressions — only then deploy. The inverse of the "just ship it" approach acceptable for internal tools.