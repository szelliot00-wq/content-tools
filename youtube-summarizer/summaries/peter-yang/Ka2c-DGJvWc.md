# What Should Engineers Do When AI Writes All the Code | Charles Lamanna (EVP Microsoft)

Video ID: `Ka2c-DGJvWc`

## Summary
Charles Lamanna, EVP at Microsoft, discusses how agents are becoming the primary users of software and what that means for product design, enterprise tooling, and the evolving role of human engineers. He argues that the shift to AI-generated code is not a threat to engineers but the latest in a long series of abstraction-level increases — from assembly to compilers to garbage collectors to cloud — that have historically made engineers more productive and more numerous, not fewer. The conversation covers Microsoft's specific product responses in Copilot and Office, the importance of multiplayer AI experiences, and how engineering leaders should manage coordination in a world where building is cheap but alignment is not. Most relevant to: product managers, engineering leaders, and anyone thinking about enterprise AI adoption.

---

## Key insights
- **Agents are already the dominant users of some platforms.** GitHub reported a 14x increase in load in a single year — driven not by 14x more human developers, but by agents submitting pull requests on behalf of humans.
- **Agents are "harsh customers."** They prioritize performance, price, reliability, and atomic programmability over human-friendly UX. A search returning 10 links with tiny snippets is ideal for a human; an agent wants 1,000 results with large chunks.
- **We've overfit AI UX to how software engineers work.** Coding is unusually solitary (solo branch → days of work → PR → code review). Most knowledge work — sales, finance, operations — is inherently collaborative and time-sliced. Designing AI solely around the solo-coder model excludes most of the workforce.
- **Multiplayer AI is the missing layer.** Microsoft's "Workspace" in Copilot is designed so humans, Copilot, and autonomous autopilots can all collaborate toward a shared goal simultaneously, with easy switching between individual, collaborative, and communication modes.
- **The side-by-side Office + Copilot experience** (open Word/PowerPoint/Excel inside the Copilot app) is a major product bet: coarse-grained prompting for big changes, fine-grained mouse/keyboard for the last 10% of polish.
- **New data assets matter more than ever.** Meeting recordings and transcripts that no human would re-watch become highly valuable grounding data for agents. Email archives and OneDrive files that sit unused for years suddenly have utility when an AI can surface the right one.
- **AI etiquette norms are still forming.** Lamanna advocates for social norms around AI disclosure and responsible use — e.g., telling recipients "AI helped generate this, I copy-edited it" — and warns against generating more content than people can usefully read.
- **The human job shifts to higher-order thinking.** Engineers on AI-heavy teams report "I've never had to think harder." The work moves to system design, architecture, verification strategies, testing, safe rollout, and setting the right signals for the software factory.
- **Historical precedent is reassuring.** Assembly → compilers → garbage collectors → cloud: each wave eliminated a class of manual work, and engineers mourned it, then embraced it. The number of software engineers grew at every step, and they solved harder problems.
- **Building is now nearly free; coordination is the bottleneck.** The time cost of writing and shipping code has collapsed. The remaining time cost is alignment: on priorities, on whether something is worth building, and on quality bars.
- **Lamanna's three coordination principles for large engineering orgs:**
  1. Write down thinking at scale (20-page semi-annual doc with high-level direction, not feature specs).
  2. Run experiments and let data resolve debates — A/B/multiarm testing is now viable even for enterprise software.
  3. Hire great people, trust them, and empower them — talent density matters more, not less, in an AI-augmented org.
- **Multi-model auto-routing in Copilot** is a strategic priority: delivering best-quality AI at the lowest price by routing to the right model for each task.

---

## Use cases
- **Engineering leaders** figuring out how to restructure team work when AI writes most of the code — shift focus to architecture, verification, and safe rollout process design.
- **Product managers** designing APIs or platforms who need to anticipate agent-first usage patterns (performance, bulk data return, atomic programmability over pretty UX).
- **Enterprise software teams** deciding how to evolve legacy desktop apps (like Office) in a Copilot-first world without abandoning their existing user base.
- **Knowledge workers in non-coding roles** (sales, finance, operations) who feel excluded from current AI tooling because it's built around solo, async coding workflows.
- **Org leaders** struggling with coordination overhead as building speed increases — the bottleneck has shifted from execution to alignment.
- **Anyone building data infrastructure** deciding what to record and retain — transcripts, recordings, and archives that seem useless to humans today become high-value grounding data for agents tomorrow.
- **Teams setting AI usage policies** looking for a framework for disclosure norms and responsible generation of content.

---

## Patterns & frameworks

**Abstraction Level Escalation**
The recurring historical pattern where each generation of tooling (assembly → compilers → GC → cloud → AI agents) eliminates a category of manual work. Engineers grieve the lost craft briefly, then embrace the new level. Outcome: more engineers solving harder problems, not fewer engineers overall. Use this to contextualize fear about AI replacing coders.

**Software Factory Model**
Engineers who are "AI-pilled" operate software factories: they set goals, architecture, and guardrails, then let agents generate, test, and iterate code. Human work concentrates on system design, verification strategy, signal selection, and monitoring — not line-by-line authorship.

**Side-by-Side Hybrid UX**
A product pattern where a prompt/conversation interface sits alongside a full-fidelity GUI tool (e.g., Copilot app + embedded Word/PowerPoint). Coarse-grained tasks go through the prompt; fine-grained tweaks (move a text box 8px) go through the mouse. Addresses the "last 10%" problem with pure prompt-driven interfaces.

**Workspace (Multiplayer AI)**
A Copilot construct that co-locates humans, Copilot, and autonomous autopilots around a shared goal (e.g., a customer proposal or a supply chain disruption response). Automatically suggests the right people and agents to add. Enables fluid switching between individual work, collaboration, and communication — designed for non-engineering knowledge work patterns.

**Zoom Out Loop**
A mental model for the evolving human role: as AI handles more execution, humans must continuously zoom out to set goals, set ambitions, set guardrails, verify outputs, and monitor over time. The loop is: set direction → let agents execute → verify → monitor → reset direction.

**Experiment-Driven Alignment**
Instead of resolving strategic debates through top-down decisions or lengthy PRDs, run multiarm experiments and let data decide. Borrowed from search (blue-link layout A/B testing) and now applicable to enterprise software. Reduces coordination cost by replacing opinion with evidence.

**Passive Data Accumulation Strategy**
Accumulate data assets (recordings, transcripts, email archives, files) that have low immediate human utility but high future agent utility as grounding context. The value is realized when an agent needs to reconstruct a decision, find a past alternative, or surface a file from years ago — not when the asset is created.