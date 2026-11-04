# This New Grok Bot Feature Just Saved Me $500 a Year (Seriously)

Video ID: `F-356TczoQU`

## Summary
This video demonstrates Grok Bot's new phone call feature, which allows the AI to autonomously call US businesses on the user's behalf. The presenter walks through a real 25-minute call where Grok Bot negotiated with a Comcast representative, reducing a monthly internet bill from $84 to $45 while also upgrading internet speed from 400 Mbps to 500 Mbps — saving roughly $468/year. The video covers setup, a detailed playback of the full call transcript, a comparison with competitor Muse, and a broader argument that AI agents handling legacy phone systems represents a significant time-saving opportunity. It is most relevant to consumers looking to reduce bills, PM/product practitioners interested in AI agent capabilities, and early adopters of AI tools.

## Key insights
- **The result**: Grok Bot negotiated the bill from $84/month down to $45/month with auto-pay (a $39/month drop) and got a speed upgrade from 400 Mbps to 500 Mbps — roughly $468/year in savings
- **Setup is simple**: Create a Grok Bot named "phone caller," provide context (address, phone number, current bill amount, competitor pricing), and Grok Bot asks clarifying questions before placing the call
- **Competitive leverage matters**: The presenter told Grok Bot that Sonic Fiber was offering 49/month in the same neighborhood — this was the core negotiation anchor that drove the discount
- **Grok Bot navigated the full IVR phone maze** (press 1, say this, enter zip code) before reaching a human, then opened immediately with the competing offer
- **The bot is an impatient negotiator**: It follows up during any pause, keeps redirecting to the core ask, and does not get distracted by small talk (when asked about the weather, it deflected with humor: "I don't have eyes on the sky, but I'm sure it's typical Bay Area gray")
- **Jiro attempted three separate upsells** (XPro Wi-Fi extender, mobile plan promotion, and a third offer) — Grok Bot declined all of them cleanly and kept redirecting to the base plan
- **Plot twist — approval required**: Comcast's system required a text/email approval link rather than verbal agreement; Grok Bot paused and checked in with the user to confirm how to handle it, showing it can escalate to humans when needed
- **Full voice recording provided**: Unlike competitor Muse, Grok Bot provides the complete voice conversation recording, not just a transcript
- **Grok Bot vs. Muse comparison**:
  - Muse introduces itself with a fake name ("I'm Haley calling on Peter's behalf"); Grok Bot says "I'm Peter's assistant"
  - Muse provides transcripts but not audio recordings; Grok Bot provides both
  - The presenter believes Grok Bot uses a more capable underlying model
- **Grok Bot built the recap app itself**: After the call, the presenter asked Grok Bot to build an app displaying the conversation highlights — it did so
- **The feature is US-only** at this time, limited to US phone numbers
- **Small team, fast shipping**: The presenter notes the feature was built by just a few engineers with PM guidance, highlighting Grok Bot's development velocity

## Use cases
- **Bill negotiation**: Internet, cable, insurance, phone plans — any subscription with a retention department
- **Canceling phone-only subscriptions**: Services that deliberately make cancellation difficult (gym memberships, streaming services, etc.)
- **Waiting on hold**: Delegate the hold time entirely to the bot while you do other work
- **Restaurant reservations**: Calling ahead for bookings at restaurants that don't use OpenTable or Resy
- **Contractor quote gathering**: Calling multiple plumbers, electricians, or landscapers for price comparisons
- **Any interaction with legacy IVR/phone-tree systems**: The bot handles "press 1, say yes, enter your zip code" flows autonomously
- **Consumers who are uncomfortable negotiating**: The bot is a persistent, unemotional negotiator that won't be swayed by rapport or upsells

## Patterns & frameworks

**Competitive anchor negotiation**
Provide the AI with a specific, credible competing offer before the call. In this case: "Sonic Fiber is offering 49/month in my neighborhood." This gives the bot a concrete number to anchor the negotiation and a credible walk-away threat, rather than just asking vaguely for a lower price.

**Context front-loading**
Before placing the call, give the bot all relevant account details (address, phone number, account number, current price, desired outcome). The more context upfront, the less back-and-forth during the live call and the fewer clarifying questions the bot needs to ask you mid-negotiation.

**Human escalation checkpoint**
Grok Bot doesn't go fully autonomous — when it hit an unexpected step (needing to approve a link via text), it paused and checked in with the user. This human-in-the-loop checkpoint is a key part of the design, ensuring the bot doesn't make binding commitments it can't complete.

**AI handling legacy systems as highest-ROI use case**
The presenter frames a mental model: AI's biggest time-saving opportunity isn't replacing modern digital workflows but handling *legacy phone-based systems* — IVR trees, hold queues, and phone-only cancellations — that have high friction but low cognitive value for humans.