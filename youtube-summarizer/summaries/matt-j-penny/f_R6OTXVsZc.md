# Best AI For Motion Graphics? Fable 5.1 vs GPT 6 Astra

Video ID: `f_R6OTXVsZc`

## Summary
This video compares two AI models — Fable 5.1 (via Claude) and GPT-6 Astra (via ChatGPT) — on their ability to create motion graphics from a raw, unedited video clip using the same prompt and workflow. The creator runs an identical test on both models, tracking cost, speed, and output quality. The core argument is that while Astra 6 may be technically more capable, Fable 5.1 delivers better value and more artistically coherent results. The video is most relevant to content creators, video editors, and AI workflow builders looking to automate video production using AI-generated motion graphics.

## Key insights
- Both models completed the task in nearly identical time: Fable 5.1 took **11 minutes 14 seconds**, Astra 6 took **11 minutes 9 seconds** — essentially a tie on speed.
- Cost differed significantly: Fable 5.1 cost **£5.90 (~$7.90 USD)**, while Astra 6 cost **$15.05** — making Astra approximately **double the price**.
- The underlying technology powering both outputs is **Remotion**, a framework that converts code into motion graphics. The AI writes the code; Remotion renders it visually.
- Fable 5.1 successfully removed silences, cut bad takes, and added motion graphics and sound effects in a single pass — a clean, coherent result for a one-shot generation.
- Astra 6 produced some technically impressive elements (e.g., a diagram showing the same prompt flowing into both models), but also made artistically illogical choices — such as a large blank space that fills in later, and graphics that wouldn't make sense to a human editor.
- The creator noted an issue mid-test where Astra 6 tried to reuse assets from the Fable 5.1 run rather than starting from scratch, requiring a correction prompt to ensure a fair comparison.
- One-shot outputs from either model are a starting point, not a final product — the creator recommends one or two additional passes for real-world use.
- The creator's custom **"full edit" skill** (a prompt/workflow built over months) drives the editing logic for both models — it encodes preferences for pacing, overlays, zooms, text, and style.
- The skill is available via the creator's **Applied AI Mastermind** community or can be built independently by defining editing preferences iteratively.
- The creator's verdict: **Fable 5.1 wins** on both value and artistic quality; Astra 6 is more expensive and makes choices a human editor would never make.

## Use cases
- **Content creators and YouTubers** who want to automate video editing and intro production using AI.
- **Solo video producers** who lack editing expertise but want polished motion graphics outputs.
- **AI workflow builders** evaluating which model to integrate into automated video pipelines.
- **Agencies or freelancers** comparing cost-effectiveness of AI tools for client video work.
- **Developers using Remotion** who want to leverage AI code generation to produce motion graphics programmatically.
- **AI tool buyers** deciding between Claude-based and ChatGPT-based solutions for creative media tasks.

## Patterns & frameworks

**The "Full Edit" Skill**
A custom, reusable prompt/workflow the creator built over months of iterative refinement. It encodes all personal editing preferences — silence removal, bad take cuts, pacing, zooms, overlays, text style — into a single instruction set. Feeding this skill plus a raw video file to an AI model produces a near-final edited video in one shot. Portable across models (used identically on both Fable and Astra here).

**Remotion-as-render-engine Pattern**
AI models generate code; Remotion compiles that code into rendered motion graphics. This separates the creative/logical layer (AI) from the rendering layer (Remotion), and leverages AI's core strength (code generation) to produce visual output. This pattern is model-agnostic and scalable.

**One-Shot Baseline → Iterative Refinement**
Both models are first run in "one-shot" mode (single prompt, no follow-up) to establish a quality baseline. The expectation is that real-world use involves 1–2 additional passes with directional feedback to reach a final, polished result. This framework separates evaluation (single shot) from production (iterative).

**Controlled A/B Model Comparison**
Same raw input, same skill/prompt, same task — only the model changes. Metrics tracked: time, cost, and subjective output quality. This is a repeatable framework for evaluating AI models on any creative or generative task where output quality is subjective but cost and speed are objective.