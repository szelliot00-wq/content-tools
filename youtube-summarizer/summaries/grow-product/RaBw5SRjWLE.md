# Stop Applying to AI PM Jobs Until You Watch This Safety & Ethics Mock

Video ID: `RaBw5SRjWLE`

## Summary
This video features a mock interview session focused on AI Product Manager (AIPM) safety and ethics interviews, hosted by Akash alongside three coaches: Ankit (AIPM at Uber/former Meta), Prasad Reddy (former CPO at Danaher), and Bart Jaworski (PM coach with 12,000+ students). The core argument is that safety and ethics competency is massively underrated by AIPM candidates, yet it is evaluated throughout the entire interview process — not just in a dedicated round. The hosts introduce the SHIR framework for safety reasoning, conduct four live mock interview rounds with real-time coaching and scoring, and close with rapid-fire tips. The video is most relevant to PMs and senior product leaders preparing for AIPM roles, especially at safety-conscious companies like Anthropic, OpenAI, or Meta.

---

## Key insights
- **Safety is evaluated throughout the entire interview, not just in a dedicated round.** At Meta, safety thinking was embedded in product sense — if you designed an AI feature without addressing harm scenarios, you failed product sense, not a separate safety checkbox.
- **Senior candidates (CPO/VP level) regularly freeze on safety questions** because they have never had to formalize their safety reasoning, even with 20+ years of experience. At the executive level, safety is table stakes.
- **The SHIR framework** is the core tool introduced: Severity, Harm Scope, Immediacy, and Reversibility. Candidates should ask for 30 seconds to run the scenario through SHIR before answering.
- **Executive-level candidates must quantify business impact alongside risk.** Bart added that the highest-scoring candidates lay out the cost of each option side by side (e.g., pulling the feature costs $50M; adding guardrails costs $200K and 2 weeks; full retraining costs $2M and 3 months).
- **Reframing risk to leadership is a critical skill.** When a VP cited earnings pressure as a reason not to act on dangerous medical AI advice, the recommended response was to reframe the question: "Can we afford the headline that we knew our AI was giving dangerous medical advice and continued to allow it?" — shifting from a $50M quarterly concern to a potential $5B brand problem.
- **The 40-minute safety rule:** In a 60-minute interview, if 40 minutes have passed and you haven't mentioned safety, find a way to bring it up. Safety should appear in nearly every interview slot across an interview day, not just one.
- **Anthropic has the hardest safety round by far**, lasting 45–60 minutes. Candidates should understand why Anthropic's founders left OpenAI, what Constitutional AI is, and be prepared for both situational and behavioral safety questions.
- **Bias in AI hiring tools is a legal liability, not just a technical problem.** A 15% lower recommendation rate for certain demographic groups triggers EEOC exposure, potential class action, and enterprise vendor deselection. Framing the fix as a competitive advantage (moral high ground, long-term retention of enterprise customers) is more effective than treating it as a slowdown.
- **For AI agents with real financial consequences**, a safety framework should include: spending caps set during onboarding, tiered confirmation flows based on transaction size, reversibility windows (e.g., 15-minute pending state before finalizing bookings), and anomaly detection for unusual behavior.
- **Liability for AI agent actions generally falls on the platform** because the platform designed the guardrails. If those guardrails fail, the company is responsible. Legal nuance varies by jurisdiction and should be confirmed with legal teams.
- **Over-polishing answers can hurt candidates.** Interviewers have explicitly asked candidates if they were reading from a script when answers sound too structured, especially with AI tools now available. Natural delivery matters.
- **The single best interview question for AIPM candidates, per Akash:** "Tell me about a time your product caused unintended harm." The answer reveals everything about a candidate's safety maturity.
- **Ankit's behavioral answer on Facebook Reels** demonstrated best-in-class STAR format: he restructured the value model from additive to multiplicative (requiring content to succeed at click, completion, and downstream engagement), resulting in a 15–20% lift in DAUs in the US/Canada and 25% gains in the hardest growth segment, with revenue stabilizing within weeks.
- **Prasad's stand-out technique** was grounding abstract safety decisions in a real past example from Danaher, where a diagnostics product was partially pulled and sent to human review loop until the underlying issue was fixed. Concrete examples at the executive level are highly valued.
- **A useful AI-assisted prep technique:** Create a Claude project with all your interview transcripts, then ask it how your answers have improved over time. You can also paste in this video's transcript and ask Claude to compare your answers to the panelists' answers.
- **Practice by recording yourself on video**, not just dictating into ChatGPT. Watching your own recording reveals delivery issues, note-reliance, and lack of eye contact that you cannot catch otherwise.

---

## Use cases
- **AIPM candidates preparing for safety/ethics interview rounds** at companies like Anthropic, OpenAI, Meta, Google, Uber, or any company with health, financial, or safety-critical AI products.
- **Senior PMs, Directors, VPs, and CPOs** who need to articulate board-level implications of AI product liability and demonstrate formal safety reasoning.
- **PMs working on consumer AI chatbots** that may generate medical, legal, or financial advice — need to know when to add guardrails vs. pull features.
- **PMs building AI-powered hiring tools** who need to address demographic bias, EEOC compliance, and how to present findings transparently to a board.
- **PMs or product leaders building AI agents** with autonomous real-world actions (booking, purchasing, emailing) who need to design spending caps, confirmation flows, and reversibility windows.
- **Candidates navigating leadership pushback on safety decisions** (e.g., VP citing earnings pressure) — need to reframe conversations from short-term revenue to long-term brand/legal risk.
- **Candidates preparing behavioral questions** about times they made the right user decision against short-term business metrics — need a clean STAR-format story with quantified results.
- **Interview coaches and PM educators** looking for a real, scored mock interview format with rubric-based evaluation to use with their own students.
- **PMs joining new teams** who discover a known, unfixed safety issue — need a clear escalation path (documentation, ethics channels, formal memos) and a framework for deciding when to escalate vs. defer.

---

## Patterns & frameworks

### 1. SHIR Framework (Severity, Harm Scope, Immediacy, Reversibility)
A four-part lens for evaluating safety risks in any AI product scenario:
- **Severity:** How bad is the worst-case outcome? (e.g., medical misinformation causing physical harm >> a slightly rude chatbot)
- **Harm Scope:** How many people are affected? (a bug hitting 10 users vs. 10 million requires completely different responses)
- **Immediacy:** Is the harm happening right now, or is it a latent/future risk?
- **Reversibility:** Can the damage be undone? (a bad recommendation is reversible; a leaked dataset is not)
*How to use it:* Ask for 30 seconds at the start of any safety question, mentally run the scenario through SHIR, then structure your answer around the most critical dimensions. In a short behavioral answer, briefly surface the two or three most relevant dimensions. In a full case interview, dedicate time to each.

### 2. SHIR + Business Impact Sizing (Executive-Level Extension)
At the VP/CPO level, SHIR alone is insufficient. High-scoring candidates pair each SHIR risk assessment with a quantified cost of each response option:
- Pull the feature entirely: $50M revenue impact
- Add a content guardrail: $200K and 2 weeks
- Full model retraining: $2M and 3 months
*How it works:* Laying costs and risks side by side makes the optimal decision obvious and demonstrates business maturity alongside safety reasoning.

### 3. Headline Risk Reframe
When leadership resists a safety action due to short-term financial pressure, reframe the conversation from revenue impact to reputational/legal headline risk:
- Instead of: "Can we afford to act before earnings?"
- Ask: "Can we afford the headline that we knew our AI was causing harm and chose not to act?"
*How it works:* This shifts the decision from a quarterly P&L discussion to a brand and legal liability discussion, which typically has much higher stakes and is harder for leadership to dismiss.

### 4. The 40-Minute Safety Rule
A proactive interview strategy: if 40 minutes of a 60-minute interview have passed without mentioning safety, actively find a way to bring it into the conversation. Safety should appear in nearly every interview slot across a full interview day loop, not just in one dedicated round.

### 5. Tiered Confirmation Framework for AI Agents
A product design pattern for autonomous AI agents taking real-world actions:
- **Scope layer:** Users set spending caps during onboarding (e.g., $500/transaction, $3,000/trip)
- **Confirmation layer (tiered by stakes):**
  - Low-stakes: no confirmation needed
  - Medium-stakes (e.g., booking under budget): push notification with 60-second undo window
  - High-stakes (near or over cap): hard confirmation required
- **Reversibility layer:** Actions go into a pending state (e.g., 15-minute hold) before finalizing; emails get a send delay
- **Anomaly detection layer:** Flag behavior that deviates significantly from a user's historical patterns
*How it works:* Reduces irreversible harm without creating friction for routine low-stakes actions, and establishes the platform's due diligence on guardrails (relevant to liability questions).

### 6. Escalation Ladder for Known Safety Issues
A structured internal escalation path when a safety issue exists but leadership is not acting:
1. Seek context — understand why the decision was made before assuming negligence
2. Formally document the concern in a written memo (not Slack) addressed to your manager, their manager, and all relevant teams, including specific risks and a recommended fix
3. Use the company's formal ethics or safety channel
4. Assess whether the organization is one you can continue to work in if users are experiencing active harm and all internal paths have failed
*How it works:* Creates a paper trail, demonstrates professionalism, and ensures the risk was surfaced transparently — protecting the PM and giving leadership the information needed to make an informed decision.

### 7. STAR Format with Linear Storytelling (Behavioral Pattern)
For behavioral questions, the highest-scoring answers follow a clean, linear narrative:
- **Situation:** Set the context (team, product, time period)
- **Task/Challenge:** Describe what made this hard (e.g., prior value model changes had been reverted due to revenue regressions)
- **Action:** Explain specific steps taken with enough technical detail to be credible
- **Result:** Quantify outcomes (e.g., 15–20% lift in DAUs, 25% gain in marginal users, revenue stabilized within weeks)
*Key nuance:* Deliver it naturally, not as a rigid recitation. The goal is for it to feel like a conversation, not a performance.