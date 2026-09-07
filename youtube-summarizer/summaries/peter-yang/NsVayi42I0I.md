# AI Makes Cheating Easy. Here’s How It Can Make Kids Smarter Instead | Sue Khim

Video ID: `NsVayi42I0I`

## Summary
Sue Khim, co-founder and CEO of Brilliant, discusses the crisis in US education (falling test scores masked by grade inflation) and argues that AI, when used correctly, can make kids smarter rather than enabling cheating. The core argument is that AI tutors should protect students' struggle time — withholding answers *and* explanations — because productive difficulty is what actually builds learning. The conversation covers Brilliant's AI tutor Cooji, their agentic content-creation workflow, product quality philosophy, and defensibility strategy. Most relevant to edtech founders, product managers building AI-native consumer apps, parents thinking about supplemental learning, and anyone designing AI workflows.

## Key insights
- **Grade inflation masks real decline**: US test scores are down but grades are up because schools lower standards to appease parents. AP English now tests middle-school-level passages. Colleges are offering remedial algebra to STEM students.
- **AI cheating is the dominant use case today**: Most students use AI to skip learning entirely — Khim compares it to "bringing a robotic arm to the gym to lift weights for you."
- **Withholding explanations is as important as withholding answers**: Explanations feel good but let the learner off the hook. The most effective intervention is making the student discover the insight themselves. Cheating and over-explaining are "closer than you'd think" — both remove the learner from doing the work.
- **Productive struggle is the product**: Brilliant's core design goal is extending the time a student can stay with something hard. Short-term engagement metrics (completion rate, time spent) are explicitly *not* measured. The only metric that matters is performance on assessment.
- **AI is a middle-to-end solution, not end-to-end**: LLMs are uneven — excellent at implementation tasks, poor at designing pedagogical sequences. Letting an LLM own the full product means the user experience is governed by what AI is worst at. Human experts design lesson structure; AI implements it.
- **Agent UI is as important as user UI**: Brilliant built a primitives library — modular, composable UI components — each with an API the model can read and write to. This gives the LLM structured scaffolding so it doesn't hallucinate interactive content from scratch, improving latency, accuracy, and reliability.
- **Synthetic students catch errors pre-launch**: Brilliant runs ~1,000 synthetic tutoring sessions per lesson across adversarial/unhappy paths before shipping. Estimated at ~20% as useful as real data, but catches serious errors before they reach students.
- **Defensibility comes from non-RL-able data**: If a frontier lab can use reinforcement learning on your domain (e.g., coding, where correctness is automatically verifiable), they will outcompete you. Tutoring is defensible because the reward signal — a real human actually learning and retaining something — requires real student sessions at scale to measure.
- **Homework counting toward grades is the incentive problem**: Students rationally find the shortest path to a grade. In countries where grades are based only on tests, cheating on homework is pointless. The US homework-cheating problem is partly a self-inflicted incentive design failure.
- **"Pump slop" is a real product risk**: AI makes it trivially easy to generate content that looks almost right but isn't. Kids and users can tell, and it shows up in engagement drop-off. Multiple human reviewers gate every piece of content Brilliant ships.
- **Every employee now designs for agents, not just users**: Onboarding at Brilliant means shipping something user-facing on day one, which forces new hires to understand the full system. The goal is encoding institutional knowledge (pedagogy, tools, workflows) into agent-accessible interfaces so expertise is available from day one.
- **Metric to optimize: can the student do the thing — now, in a week, in a month?** Learning and retention over time is the north star, not module completion or time-on-platform.

## Use cases
- **Parents** looking to supplement classroom learning without just giving kids answers — understanding why productive struggle matters and how to structure support.
- **Edtech founders** deciding how much of their product to hand to an LLM — the framework applies directly to scoping AI's role vs. human design.
- **Product managers at AI-native companies** thinking about how to design agent interfaces alongside user interfaces, using structured primitives/APIs rather than open-ended generation.
- **Startup founders** evaluating defensibility against frontier labs — assessing whether their domain's reward signal is automatically verifiable (dangerous) or requires proprietary real-world data (defensible).
- **Curriculum or content designers** building AI-assisted workflows — understanding when to let AI implement vs. when humans must own the design.
- **School administrators or policy makers** examining grade inflation, homework grading incentives, and the structural misalignment between grades and actual learning.
- **Engineers building agentic products** — the primitives library pattern (structured components with agent-readable APIs) is directly applicable to any domain where LLM hallucination of output is a quality risk.
- **Anyone managing AI-assisted teams** — the insight that onboarding should include agent-accessible documentation of institutional knowledge applies beyond edtech.

## Patterns & frameworks

**The Robotic Arm Anti-pattern**
Using AI to skip the part where you learn is like bringing a robotic arm to the gym to lift the weights for you. The point of the gym (building strength) is defeated. Applied to product design: if your AI feature removes the user's need to think, you've optimized away the core value.

**Cheating ≈ Over-explaining (The Learner Off-the-Hook Principle)**
Both giving the answer and giving a full explanation let the learner avoid doing the cognitive work. Effective tutoring holds the learner in productive discomfort — asking Socratic questions, simplifying the problem, or letting them struggle — rather than resolving the tension for them.

**AI as Middle-to-End, Not End-to-End**
AI models are "spiky" — excellent at some subtasks, terrible at others. The pattern: identify which tasks in your product AI excels at (implementation, generation within constraints) and which it fails at (architecture, pedagogical design, engagement). Assign accordingly. The weakest AI task will define the user experience if left unchecked.

**Human Design + AI Implementation Workflow**
A master teacher/designer sketches the lesson structure, sequence, and pedagogical interventions. AI implements that design using a library of structured primitives. Separates the "what to teach and in what order" (human) from "build the interactive module" (AI), getting quality and speed simultaneously.

**Primitives Library + Agent Interface Pattern**
Build modular UI components that each expose an API a model can read and write to. The model navigates a schema rather than hallucinating free-form output. Benefits: lower latency, higher accuracy, deterministic grounding, and composability. Applicable to any domain where AI needs to produce structured, interactive output reliably.

**The Flywheel of Non-RL-able Data**
Build a product → generate proprietary data in a domain where the reward signal isn't automatically verifiable → use that data to improve the model → better model improves the product. Defensible against frontier labs because they cannot replicate the data without running the product at scale in the real world.

**The Mario Ramp (Difficulty Calibration)**
Structure difficulty so the next step always feels hard but achievable within ~10 more tries. Avoid both under-challenge (disengagement) and over-challenge (dropout). Measure only actual learning outcomes — not completion rate or time-on-platform — to avoid optimizing toward false proxies that incentivize making content too easy.