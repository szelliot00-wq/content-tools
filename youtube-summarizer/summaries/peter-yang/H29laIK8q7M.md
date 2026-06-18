# How I Turned Codex Into My AI Life Coach in 13 Minutes (5-Step Tutorial)

Video ID: `H29laIK8q7M`

## Summary
The video is a step-by-step tutorial on building a personal AI advisor using Codex (or Claude Code) by organizing a small folder of structured text files. The creator argues that giving an AI model rich personal context — goals, principles, energy sources, and accumulated learnings — transforms it from a generic chatbot into a genuinely useful decision-making partner. He shares that he used this system for three months before making a major career decision (leaving his job), crediting it with insights he wouldn't have reached alone. The tutorial is most relevant to knowledge workers, content creators, solopreneurs, and anyone navigating significant life or career decisions who wants a personalized AI thinking partner.

## Key insights
- The advisor is not a single prompt but a **folder of 4 structured files**: `skill.md`, `plan.md`, `learnings.md`, and an `eval` checklist — each serving a distinct purpose.
- `skill.md` defines **behavior, not content**: it tells the AI what role to play, which files to read, how to structure advice (e.g., reflect first, separate facts from assumptions, give 2–3 concrete suggestions), and when to activate the skill (e.g., "use when user is stuck on a decision or asking for a gut check").
- `plan.md` is the **most important file** — a one-page living document covering: a single clear annual goal, 3–4 personal principles, energy sources and drains, ICP and business context, family/financial situation, and historical goal tracking.
- The creator's **annual goal example**: grow his business to a specific revenue target by end of 2026 while keeping control of his time. He optionally connected Codex to his bank via Mercury MCP to track progress toward that goal automatically.
- **Principles serve as a decision filter** — his three: "Work feels like play," "Keep the main thing the main thing" (focus on YouTube/newsletter, avoid distraction), and "Do the simple thing first" (ship early, share learnings). These help the advisor flag when he's drifting.
- **Energy mapping** is a core section: he lists 3 things that give energy (building AI products for his own problems, teaching through newsletter/YouTube, learning from other builders) and 3 that drain it (too many live meetings, admin work that doesn't compound, selling things he doesn't personally want to build).
- `learnings.md` acts as a **changelog of insights** the AI accumulates about the user across conversations. The `skill.md` instructs the AI to offer to save new learnings after every meaningful session.
- The `eval` file is a **20-point yes/no self-check checklist** the AI runs *before* giving advice. Key checks include: Did it read `plan.md` and `learnings.md` first? Did it cite actual goals and principles? Did it give 2–3 concrete, actionable next steps? Advice is only delivered once all checks pass.
- The eval mechanism forces the AI to **slow down and self-verify** rather than give generic responses — if advice is vague, the eval fails.
- **Model quality matters significantly**: the creator found Anthropic's Fable model especially effective because it combined personal context from the skill files with outside research (e.g., discovering that renewal/retention is the real bottleneck for paid newsletter growth, and that similar creators post to Substack Notes multiple times daily).
- Real-world AI advisor output example: before leaving his job, the advisor told him "your decision is psychological and about letting go of the person you spent a decade becoming" and grounded the advice in his family situation (kids aged 8 and 4) and actual goal (time with family, not income maximization).
- The creator recommends simply **copy-pasting the video transcript into Codex or Claude Code** and asking it to walk you through setup as a free alternative to his paid skill templates.

## Use cases
- **Career transition decisions**: thinking through whether to leave a job, take a new role, or bet on yourself — especially over an extended period (months, not a single session).
- **Solopreneurs and content creators** who face constant new opportunities (conferences, sponsorships, collabs) and need a system to stay focused on core priorities.
- **Newsletter and paid subscription growth**: the advisor can research comparable creators and surface non-obvious bottlenecks (e.g., retention vs. acquisition).
- **Weekly/ongoing gut checks**: asking "what should I focus on this week?" with the AI drawing on personal context rather than generic productivity advice.
- **Annual planning and goal-setting**: forcing clarity on a one-page life/business plan that can be iterated over time.
- **Anyone who makes important decisions alone**: the system is framed as always having a trusted advisor available, removing the isolation of solo decision-making.
- **Product managers and team leads** who already think in terms of principles and frameworks and want to apply that discipline to their own life and career.

## Patterns & frameworks

**The 4-File Advisor Stack**
A folder-based architecture where each file has a distinct job: `skill.md` (behavior), `plan.md` (context), `learnings.md` (memory), `eval` (quality control). The separation prevents the advice-giving logic from getting tangled with personal data, making each file easier to update independently.

**The One-Page Plan**
A single document covering goal, principles, energy map, business context, life/financial context, and historical goals. Deliberately kept to one page so the author actually reads and updates it. The constraint forces prioritization and makes it scannable by the AI without losing signal in noise.

**Principles as Decision Filters**
Borrowed from product management: define 3–4 principles upfront so the AI (and you) can evaluate new opportunities against them automatically. Functions as a standing "should I do this?" heuristic rather than re-litigating values each time.

**Energy Mapping**
Explicitly listing what gives vs. drains energy as a section in the plan. Used by the advisor to flag when proposed work conflicts with the user's actual operating conditions — not just strategic fit, but personal sustainability.

**Pre-Advice Eval Checklist**
A self-verification loop the AI runs before responding. Modeled on a QA checklist: the AI must answer yes to ~20 binary questions (grounded in context? concrete next steps? assumptions named?) before delivering advice. Prevents the AI from giving plausible-but-generic responses.

**Learnings Changelog**
A running log of insights the AI extracts from conversations, referenced at the start of each new session. Creates compounding value over time — the advisor gets more useful the longer you use it, because it accumulates a richer model of who you are and what you've learned.

**Context + Research Combination (Fable example)**
The most powerful use pattern: personal context from the skill files combined with external research on comparable people/businesses. The Fable example showed the AI finding non-obvious insights (renewal as the real bottleneck, Substack Notes underuse) that required both personal grounding and market awareness.