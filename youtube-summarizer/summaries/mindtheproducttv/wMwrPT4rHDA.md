# The document that can replace PRDs — Rags Vadali

Video ID: `wMwrPT4rHDA`

## Summary
This video features Rags Vadali, a veteran product manager (formerly Google, Meta, and six startups) turned founder of Floto, a feedback agent startup. He discusses how AI-driven development has forced him to completely invert the traditional PM workflow — starting with engineering prototypes rather than PRDs — and introduces the Product Experience Document (PXD), a new artifact designed to replace PRDs when building agentic products. The conversation covers discovery practices, synthetic personas, conversation design for agents, hiring philosophies, and scaling challenges. It is most relevant to PMs, founders, and product teams building AI-native or agentic products, particularly in small, fast-moving organizations.

---

## Key insights

- **The traditional PM workflow has been inverted at Floto.** Instead of PM → Designer → Engineer, they now start with Engineering → PM → Designer. Engineers build the first prototype directly on the codebase, then Rags plays with it to understand what is possible before shaping the experience layer.

- **The PM became the bottleneck under the old model.** Running weekly sprints with AI-assisted engineers meant Rags and his designer couldn't produce enough specs to keep pace. Inverting the process removed this bottleneck.

- **"I don't know what I don't know" as a PM.** Foundation model capabilities change so fast that pre-speccing a user experience is often already disconnected from what is actually buildable. Starting from what engineers can demonstrate solves this gap.

- **The product for an agentic tool is the experience layer, not the UI.** Rags argues that when building agents, the real product definition work is designing the experience on top of the agent — guard rails, instructions, conversation arcs — not screens and interactions.

- **The PXD (Product Experience Document) is not a PRD.** It is not designed to align stakeholders in a room. It is a handoff document to engineers and, crucially, to coding agents (like Claude Code) that use it to generate prompts and tune behavior. It bridges product intent and AI model behavior.

- **The PXD has these core sections:**
  - **Why** — the reason for building this
  - **Success Criteria** — a mix of quantitative (e.g., 80% of users achieving X) and qualitative bars (e.g., "same insight quality as a 15-minute real user interview")
  - **Experience Principles** — how the agent should feel to interact with; e.g., ask only one question at a time, add break points for serious moments, go deeper emotionally on key issues
  - **Example Interactions (Good / Bad / Ugly)** — real pulled examples from prototype testing, used to teach the model acceptable and unacceptable ranges of behavior
  - **Critical Moments** — specific conversational triggers where the agent must break its normal flow and go deep (mirroring the "tell me more" instinct of a skilled human interviewer)
  - **Conversation Closing** — intentional design of how the conversation ends to habituate users to return; abrupt closings harm future engagement
  - **Success Metrics** — standard product metrics applied at the end

- **Engineers at Floto no longer write code themselves.** The entire engineering team uses Claude Code (Anthropic's agentic coding tool), with parallel agents writing the code. A single engineer can own and build entire product areas independently.

- **Floto runs 2–3 products in parallel with a team of 3 engineers.** They throw away 50–60% of what they build because Rags acts as the quality/problem-fit gate: if it doesn't solve a user problem, they kill it with low ego.

- **Discovery principles have not changed, but AI accelerates parts of it.** Talking to real users remains the gold standard. However, AI tools like Perplexity can now surface cited evidence of user pain from Reddit, G2, and comment threads at scale, replacing manual forum trolling.

- **Synthetic personas are useful but limited.** They reflect average model training data and fail at edge cases. The key insight: **ask negative questions, not positive ones.** E.g., instead of "Why would you click Buy?", ask "What would make you pause before clicking Buy?" — this surfaces real friction even from AI personas that are trained to be agreeable.

- **Conversation design is now a core PM skill for agentic products.** Floto builds agents that ask questions and never give answers — the reverse of how most people use LLMs. This requires deliberate design of conversation arc, personality, pacing, and emotional depth, informed by Rags's osmosis of content design principles over his career.

- **The PXD also functions as an eval document.** Because agents are non-deterministic, specifying a single "correct" behavior is insufficient. The good/bad/ugly interaction examples define a range of acceptable and unacceptable outputs, functioning similarly to LLM evals.

- **This approach is best suited for agentic products, not UI-heavy ones.** For interface-heavy products, Rags still recommends close designer-engineer collaboration, potentially starting with a Figma reference. The full inversion works when the product is primarily conversational or agentic.

- **Product sense is now a universal hiring requirement at Floto, regardless of role.** Every hire — engineer, growth, intern — goes through a product sense interview (modeled on Google/Meta loops), including questions like "Tell me about a product you love and why." This is because everyone is now in the direct path of user experience decisions.

- **Hiring skews toward AI-native early-career talent.** The founding duo brings experience and editing judgment; all other hires are recent graduates or interns who are natively curious about AI possibilities. Product sense + AI nativity is considered the ideal combination and can slot into multiple roles.

- **The biggest risk of the current moment is feature bloat at scale.** Rags warns that as everyone can ship, large teams will produce feature explosions with degraded end-user experience. The correction will come when the market rewards quality and relevance over velocity, and teams that maintained a user-focused compass will win.

- **The one thing that hasn't changed: talk to users and build what they want.** This is Rags's closing first principle — the compass that product people should not abandon regardless of how fast tooling evolves.

---

## Use cases

- **Founding PMs or solo PMs at AI startups** who are struggling to keep pace with fast-moving engineering teams and need a lighter, more flexible spec format.
- **Product teams building conversational agents or AI interviewers** who need to define agent behavior, conversation arcs, and guard rails in a structured way.
- **Engineers or technical founders without a dedicated PM** who need a document format that bridges product intent and AI model prompting/tuning.
- **PMs transitioning from traditional enterprise product roles** (PRD-heavy, Figma-first) who want a practical framework for working in AI-native environments.
- **Product teams using agentic coding tools (Claude Code, Cursor, etc.)** who want to understand how to feed product intent into coding agents effectively.
- **Startups using AI for user research** who want to know where synthetic personas and AI-assisted discovery are reliable versus where they fall short.
- **Hiring managers at AI-native startups** rethinking role definitions and interview processes as the line between engineering, design, and product blurs.
- **Conversation designers or UX writers** moving into product roles at AI companies where conversational experience design is a core product output.
- **Product leaders at large organizations (Google, Meta scale)** trying to understand how small-team AI-native practices might inform cultural or process changes at scale.

---

## Patterns & frameworks

### 1. The Inverted Product Workflow
**What it is:** A reversal of the traditional PM → Designer → Engineer sequence.
**How it works:** Engineers receive a problem statement (not a spec) and build a working prototype directly on the production codebase. The PM then plays with the prototype to understand the boundaries of what is possible, shapes the experience, and loops back with lightweight direction. Design polishes last. This removes the PM as an upstream bottleneck and grounds experience decisions in real capability.

---

### 2. The Product Experience Document (PXD)
**What it is:** A living artifact that replaces the PRD for agentic products.
**How it works:** Structured in six sections — Why, Success Criteria, Experience Principles, Example Interactions (good/bad/ugly), Critical Moments, Conversation Closing, and Success Metrics. It is written to be handed directly to engineers AND fed into coding agents as prompt input. Its language draws from eval design: defining ranges of acceptable behavior rather than single correct outputs.

---

### 3. Good / Bad / Ugly Interaction Examples (Range-Based Specification)
**What it is:** A section of the PXD that defines acceptable and unacceptable agent behavior through real pulled conversation examples.
**How it works:** Because agents are non-deterministic, you cannot specify a single correct output. Instead, you anchor behavior by showing the model (and engineers) what good looks like, what bad looks like, and what to avoid entirely. Directly analogous to LLM evals.

---

### 4. Critical Moments (Conversational Break Points)
**What it is:** A predefined set of triggers within a conversation where the agent must abandon its scripted flow and go deep.
**How it works:** Modeled on skilled human interviewer instincts ("tell me more"), these are flagged signals — a user expressing strong frustration, an unexpected problem statement — where the agent is instructed to stop its goal-oriented path and probe emotionally and contextually. Prevents monotonic, goal-tunnel-visioned agent behavior.

---

### 5. Negative Question Framing for Synthetic Personas
**What it is:** A technique for getting useful signal from AI-simulated users despite their tendency toward positive/agreeable responses.
**How it works:** Instead of asking "Why would you do X?" (which yields rationalized positive answers), ask "What would stop you from doing X?" or "What would make you pause?" The model's agreeable bias still operates, but the inverted frame surfaces friction and hesitation that is actually insightful.

---

### 6. Product Sense as a Universal Interview Bar
**What it is:** A hiring philosophy that applies traditional product sense screening to every role on a product team.
**How it works:** Regardless of whether you are hiring an engineer, growth person, or intern, include a product sense question (e.g., "Tell me about a product you love and why"). The rationale: since everyone now ships directly into the user experience path, everyone needs baseline judgment about what good product feels like. Combined with AI nativity, this creates a generalist profile that can flex across roles.

---

### 7. The "Focus on the User" First Principle as a Constant
**What it is:** A meta-framework or orienting compass for navigating rapid change.
**How it works:** Rags argues that amid all the process, tooling, and team structure changes, the one invariant is: continuously understand what the user wants and build only that. Teams that maintain this discipline through the current velocity explosion will be the ones whose shipped features actually drive growth and retention. Described as the antidote to feature bloat.