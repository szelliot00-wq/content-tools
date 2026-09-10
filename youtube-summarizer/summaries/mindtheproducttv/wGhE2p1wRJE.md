# What I learned from building, and exiting a startup — Kirsten Mann (Strategic Advisor)

Video ID: `wGhE2p1wRJE`

## Summary
Kirsten Mann, a 30-year product veteran turned founder, reflects on building and exiting Visory — an AI-powered board pack analysis tool she co-built with Toby. The conversation covers the full arc: validating demand before building, discovering the gap between stated and revealed user preferences, navigating pricing anchors, and coping with products that have long cycles to value and trust. The central argument is that in the AI era, building has become trivially cheap while distribution, commercial validation, and quality assurance remain brutally hard — and founders consistently underinvest in all three. Most relevant to product managers considering founding, early-stage founders building with AI tools, and product leaders advising startups.

## Key insights
- **Distribution is the core product problem today.** AI has collapsed the cost of building but has not reduced the cost of reaching people who trust you. Founders keep deferring distribution until after product-market fit, which is backwards — it must be treated as a parallel hypothesis from day one.
- **Being your own customer is both your best and most dangerous asset.** Kirsten's lived experience as a board director gave her deep problem intuition, but her own conviction was "the least reliable signal in the room." Real demand is someone blocked by current options, not you wanting the thing you built.
- **The Me Test has replaced the Mum Test — and it's a trap.** Many founders vibe-code a solution to their own problem over a weekend and mistake feasibility and usability-for-one as validation. That proves nothing about viability or desirability for anyone else.
- **Friction is a demand signal, not an obstacle.** Before building anything others could touch, Kirsten asked prospective users to provide two confidential board packs AND record themselves reading one aloud. The willingness to clear that high bar — not positive coffee-chat sentiment — was the real proof of demand. She set a target: if 10 people do this, build. She got 10.
- **Stated vs. revealed preference — cross-pack search case study.** The feature that drew the strongest research reaction (searching across multiple board packs by vague memory) was barely used in practice. Directors were time-poor and went straight to the "key signals" triage view instead. What people say they want in a demo and what they reach for at 10pm Sunday before a Tuesday meeting are different things.
- **Kano model delighters sell but don't retain.** Cross-pack search and the "take the perspective of different directors" persona feature both demo'd brilliantly and were mentally ticked as valuable by users — but rarely used. They functioned as risk/insurance features, not daily-driver features. The "broccoli principle": people know they should eat broccoli, but they don't.
- **Time to trust > time to value for low-frequency products.** Visory's value compounded across board cycles. Cycle 1: directors ran it alongside manual reads. Cycle 2: more confident but still comparing. Only by cycle 3 did they relax and rely on it. Kirsten had modeled 2 cycles; some users were on quarterly boards, meaning their "penny drop" moment was 9+ months away — impossible to capture in a 30-day trial.
- **The pilot pricing anchor trap.** Kirsten priced early adopters at $150/month (vs. the intended $300/board seat) to encourage adoption. When she tried to move them to $300, the 100% jump felt like a penalty even though she had pre-warned them. Lesson: pilot at full price with a proper value case, or pilot close enough to full price that the step-up isn't jarring.
- **Never run a test to confirm — run it to find a reason to stop.** Most founders (and AI agents) run validation to be proven right. Kirsten ran validation trying to find reasons to kill the idea. Sentiment ("this would be amazing") is cheap; clearing meaningful hurdles is the signal.
- **Enterprise sales creep is a strategic inflection point.** Visory started as direct B2B (director buys for themselves). It quickly flipped to enterprise sales as chairs and co-CEOs wanted bulk deals routed through IT, legal, and AI transformation leads. Kirsten had pre-decided this wasn't the company she wanted to build, so rather than raise capital to build an enterprise channel, she found an existing channel — and exited.
- **The product vs. feature question is increasingly relevant.** AI is lowering the defensibility moat on standalone products. Visory was a contained, valuable product — but it lived inside a broader ecosystem of board-related jobs (pack creation, effectiveness measurement). Founders need to honestly assess whether their product delivers standalone value or requires adjacent products to matter.
- **AI model drift is an underappreciated operational risk.** Visory used three models (two for analysis, one to adjudicate the best output). One model was silently deprecated overnight. Usage patterns shifted unexpectedly before the team caught it. Unlike app store gatekeeping, AI providers deprecate with minimal notice. Staying on top of model changes is continuous, exhausting work.
- **The relentlessness of AI-speed building has a human cost.** What would have been an 18-month build with 8 engineers took ~4 months for two people — but at a personal cost Kirsten underestimated. The "tantalizingly close" illusion (10 more minutes and it'll be done) led to sustained overwork. Toby eventually hit a wall. As AI lets small teams do more, this pressure only grows.
- **QA and eval frameworks are not optional for commercial products.** People shipping AI products to real users often skip regression testing and model eval infrastructure. It always comes back. Non-deterministic systems require treating models like employees — regular reviews and calibrations — not like deterministic software.
- **Synthetic user agents have limited validation utility.** AI agents trained on discovery interviews can be useful for early, quick usability checks. But they don't replicate the commercial pressure and behavioral reality of real users, and they can't probe the "what have you actually done about this problem?" question that separates pain from demand.

## Use cases
- **Founders building with AI tools** who need to validate commercial demand before investing deeply in the build
- **Product managers transitioning to founder/co-founder roles** who understand product craft but are new to owning distribution and pricing
- **Advisors and coaches working with early-stage founders** — particularly those coaching people who are building for themselves and mistaking it for validation
- **Teams building low-frequency, high-stakes products** (strategy tools, governance tools, compliance tools, quarterly-use products) that need to rethink trials, pricing, and time-to-value assumptions
- **Anyone setting pilot pricing** who needs to think carefully about anchoring before running early adopter programs
- **Product teams evaluating which features to cut vs. keep** — the Kano delight vs. daily-driver distinction applies broadly
- **Teams shipping AI-powered products** who need to stand up eval/regression infrastructure for non-deterministic systems
- **Anyone building in a market where the buyer is hard to reach** (executives, board members, regulated professionals) who needs to think about channel as a first-class hypothesis

## Patterns & frameworks

**Distribution as a parallel hypothesis**
Treat the distribution channel as its own testable assumption with explicit stop criteria — not something you figure out after product-market fit. Define the channel, identify how that channel mirrors customer behavior, test whether the channel is ownable. For Kirsten, board directors act on trusted recommendations, not cold outreach — so a founder with a laptop couldn't own that channel without enterprise backing or an acquisition into an existing channel.

**Friction-as-demand-signal (the "big ask" test)**
Before building, present prospective users with a genuinely difficult, high-effort request tied to the core product experience. If enough people clear the hurdle, you have evidence of real demand. Kirsten's version: ask board directors for two confidential board packs + an audio recording of themselves reviewing one — a high-stakes, time-consuming ask involving sensitive documents. "Talk over coffee is cheap. Getting clearance to hand over two board packs is expensive." Set a go/no-go number in advance (she chose 10).

**Stated vs. revealed preference**
Stated preference = what users say they want when asked in research or demos. Revealed preference = what they actually reach for under time pressure and real conditions. The gap shows up in usage data, not surveys. To narrow it in discovery: ask for three specific recent times they tried to do the thing, and what they did instead. If they built a workaround, the problem is real. If they can't name a time, it probably isn't.

**Time to trust (extension of time to value)**
For products whose value compounds over time or cycles, time to trust matters more than time to value. Trust requires comparison, and comparison requires experiencing the product across multiple cycles. For low-frequency products, this can stretch to months or years. Design your trial, pricing, and churn model around this reality — not around a 30-day SaaS activation assumption.

**Kano model applied to AI-era features (the "broccoli principle")**
Some features are delighters — they excite in demos, provide a mental "insurance" tick, and occasionally deliver real value — but are not day-to-day drivers. The broccoli principle: users know they should use it, and they're glad it exists, but they don't actually reach for it. These features can be retained for demo and positioning value but should not be confused with core retention drivers.

**Pilot pricing anchoring**
Whatever price you charge in a pilot becomes the psychological baseline. A jump from pilot price to full price feels like a penalty, even if pre-disclosed. Options: (1) pilot at full price with a strong value case, (2) pilot close enough to full price that the step-up is minor, or (3) explicitly frame a time-limited discount with a concrete expiry tied to a value milestone.

**The "run tests to fail, not to pass" mindset**
Borrowed from the scientific method: genuine validation requires designing tests whose purpose is to find a reason to stop, not to confirm your hypothesis. Applied to product: ask "what would prove this idea is wrong?" and test that. Most founders — and AI agent validation tools — are designed to confirm rather than disconfirm.

**Model-as-employee evaluation cadence**
Non-deterministic AI systems require ongoing calibration, not one-time QA. Treat AI models like employees: run regular reviews, monitor for drift, build observability into the system from the start so you can see what's happening across all model calls. Deprecation can happen overnight with minimal notice — build detection or monitoring for it if the product is commercial.