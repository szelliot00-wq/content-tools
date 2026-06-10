# Why Using AI to Align Executives Backfires (And What Works Instead)

Video ID: `yDeFGKaSoX8`

## Summary
This episode features Matthew Wing, VP of Product & Design at Customer.io (a $100M+ ARR company), sharing how he uses Claude as a product leader — not just an IC PM. The core argument is that AI amplifies your ability to decompose problems, but will produce shallow "slop" if you oversimplify the problem space before engaging it. The episode covers three concrete areas: building an all-hands presentation in 2 hours, running a metrics retrospective, and Wing's full weekly AI stack. It is most relevant to senior PMs, product leaders, and directors who need to produce executive-quality documents and drive alignment.

## Key insights
- **AI is a test of problem decomposition**: Claude is good at solving problems but will flatten and oversimplify if you hand it a poorly decomposed problem. The leader's job is to explode the problem into its constituent parts first, then hand those pieces to Claude.
- **Treat Claude like a talented junior employee**: It is eager to please, will race to the finish line without asking clarifying questions, and will produce output that needs substantial revision. The fix is to slow it down deliberately.
- **Inventory raw materials before generating anything**: Wing spent the first part of his 5am session cataloguing what he had — Zoom recordings, demo day transcripts, strategy docs — before touching a single slide. This "inventory first" habit is foundational.
- **The "matrix multiplication" transformation pattern**: Wing's core Claude workflow is identifying a source (e.g., an engineering demo day Zoom transcript) and a target shape (e.g., a strategy doc organized by three investment themes), then asking Claude to pivot the source into the target shape. This is the highest-leverage Claude operation for leaders.
- **Order of operations matters for talk tracks**: He built slides first (using screenshots fed back into the same Claude session), then asked Claude to write talk tracks that *don't* repeat what's on the slide — because Claude had full context from the session to draw richer narrative connections.
- **Use abstraction and analogy to prevent premature leaping**: Wing deliberately withheld the business context (Customer.io pricing philosophy) while building a lifecycle model, using an abstract biology/water cycle metaphor instead. This forced Claude to ask clarifying questions rather than jump to a pre-packaged answer. Only after the mental model was solid did he reveal what it was for.
- **Layer complexity iteratively, like explaining a board game**: Don't dump all rules and exceptions at once. Start with the crude heuristics, stabilize that foundation, then add nuance incrementally. Overloading context at once causes "mental fatigue" and produces overly complex, lost-in-the-woods output.
- **Kill the "do you want me to do X next?" behavior actively**: When Claude starts nudging you toward the next step, explicitly say "stop recommending the next step — I will tell you when." A 50–200 iteration session with a great deliverable is better than accepting the first eager draft.
- **Claude lacks social/political IQ**: It adopted Wing's internal animal-name shorthand (e.g., "unicorn," "horse") and used them in the final output, not understanding that novel jargon creates audience resistance. Leaders must actively strip internal working language before it reaches the deliverable.
- **Using AI to generate executive alignment will backfire**: Senior executives are trained to filter noise and detect slop. If you're senior, people will smile and nod but quietly push back. If you're a director-level leader, your work simply gets ignored. The symptom differs by level; the outcome is the same — no real alignment.
- **"Blue-collar knowledge work" is gone**: The work of transforming a Google Doc into slides, or pivoting content from one format to another, has been commoditized. The remaining leadership value is in (1) choosing the right source and (2) being deliberate about the target — the transformation in between is now nearly free.
- **The best persuasion requires knowing the reader's emotional state**: Knowing your audience just came out of the biggest launch in company history, or that they're exhausted before a board meeting, is something Claude cannot replicate. Leaders must bring that situational awareness to frame the story.

## Use cases
- **All-hands / company roadmap presentations**: Building a Q2 roadmap deck in ~2 hours by feeding Zoom transcripts and strategy docs into Claude and pivoting content into strategic themes.
- **Metrics retrospectives for exec peers**: Using Claude as a thinking partner to build clean mental models before drafting the actual retrospective — not jumping straight to output generation.
- **Talk track writing**: Feeding screenshots of finished slides back into the same session to generate non-redundant speaker notes informed by full session context.
- **Ad hoc data analysis at scale**: Using a Slack bot with Snowflake access (215+ back-and-forth messages) to query 2,000 customer records in natural language, with a data team standing by to verify non-deterministic outputs.
- **Cross-channel Slack monitoring**: An AI scanner watches dozens of Slack channels to surface conversations where a product person should be involved — a "sonar" rather than a surveillance tool.
- **Document consistency auditing ("Chiefy")**: Running new documents through a bot that checks them against 20–50 canonical company docs to surface discrepancies, flag stale documents, and maintain strategic coherence over time.
- **Pricing philosophy / lifecycle modeling**: Building abstract models using analogy first, stress-testing them against real business domains only after the model is validated.
- **Building executive-quality documents as a director**: The framework applies specifically to leaders who need their work to *not* get filtered out as noise by more senior executives.

## Patterns & frameworks

**Inventory Before Generating**
Before opening a blank slide or starting a Claude session, list all raw materials available (Zoom recordings, strategy docs, Slack threads, prior presentations). Only then decide which sources to use and what target shape to aim for. Skipping this step is the primary cause of slop.

**Source → Transformation → Target**
The central mental model: your value as a leader is no longer doing the transformation (Claude does that for free), but in (1) selecting and shaping the source material and (2) being deliberate about the target format and story. Leaders who only run the transformation function are replaceable.

**Analogy-First / Abstraction-First Decomposition**
When building a complex mental model (e.g., customer lifecycle), use an entirely abstract metaphor (biology, water cycle, 2x2 boxes) and refuse to introduce the actual business domain until the model is structurally sound. This forces Claude to ask clarifying questions rather than pattern-match to a pre-packaged answer, and produces a cleaner, domain-agnostic model that can then be applied and stress-tested.

**Iterative Context Loading ("Slow Crawl")**
Feed Claude context in deliberate increments rather than all at once. Start with crude heuristics, stabilize, then add nuance. This mirrors how you'd explain a board game: establish the objective and basic rules before introducing exceptions. Explicitly suppress the "do you want me to do X next?" behavior to prevent premature deliverable generation.

**Junior Employee Mental Model**
Claude is talented but junior: eager to please, won't ask enough clarifying questions, will race to the finish line, and lacks institutional and social context (e.g., which terms carry political baggage, what format the company actually uses). Manage it the way you'd manage a brilliant but inexperienced new hire — with structured guidance, explicit constraints, and iterative check-ins.

**Matrix Multiplication / Pivot**
A named Wing pattern: identify a source document with the right raw content but the wrong shape, identify a target structure (e.g., a strategy doc organized by investment themes), and ask Claude to "pivot" the source into the target. The value is in recognizing which source-target pairing unlocks the transformation — not in doing the transformation itself.

**Problem Decomposition Test**
The overarching framework: using AI well is fundamentally a test of how thoroughly you can decompose a complex problem before engaging Claude. Decompose the problem into pure observations and discrete pieces, load those into the context window, *then* assemble a solution. Flattening the problem and asking for a one-shot solution is the root cause of nearly all AI slop.