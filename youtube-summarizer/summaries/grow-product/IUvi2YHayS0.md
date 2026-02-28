# I learned AI designing more in this 1 hr than any course ever

Video ID: `IUvi2YHayS0`

## Summary
This video transcript details how Product Managers and designers can effectively leverage AI for product design, arguing that current approaches are often "completely wrong" by focusing solely on prompting. The core argument is that designing with AI requires understanding the entire workflow, system constraints, and user behaviors, not just generating output. It introduces a comprehensive "Design with AI" mind map covering prompting, ideation, design/prototyping, and conscious design. The video also demonstrates two specific workflows: generating AI-prototyping specs using a custom GPT and creating divergent design variations with Google Stitch before exporting to Google AI Studio for interactive prototyping. This masterclass is most relevant to Product Managers, Product Designers, and even Engineers looking to enhance their AI product development skills and gain a competitive edge.

## Key insights
- **Rethinking AI Design**: Designing with AI is not just about prompting; it's about understanding the entire workflow, system, constraints, and behaviors. Many PMs are currently designing AI products incorrectly by overlooking this holistic view.
- **The "Design with AI" Mind Map**: A comprehensive framework for AI design includes four main areas:
    1.  **Prompting with AI**: Focusing on clarifying the ask, providing necessary (not more) context, leveraging references (text, visual, code), and structuring prompts. Context engineering is crucial for amplifying prompt effectiveness, considering factors like user needs, constraints, audience, design principles, and brand guidelines.
    2.  **Ideating with AI**: Using AI for early-stage brainstorming (e.g., product ideas based on business/user goals, insights, constraints) and convergent thinking (ranking ideas, asking for examples/sources for better evaluation).
    3.  **Designing & Prototyping with AI**: Specifying instructions and context, brainstorming design variations, and tracking options. AI tools have brought convergence to these stages.
    4.  **Being Conscious with AI**: Incorporating intentionality and thoughtfulness beyond tactics. This involves awareness of risks (hallucination, biased/outdated/irrelevant/low-quality insights), and mitigation strategies like keeping humans in the loop, double-checking sources, fostering empathy, including diverse perspectives, giving users control, and auditing AI outputs for nuanced information (e.g., behavioral cues, sarcasm).
- **Workflow 1: Custom GPT for AI Prototyping PRD**:
    -   A custom GPT (or similar tool like Claude Skill/Project, Gemini Gem) can be built to generate a lightweight "PRD" (Product Requirements Document) specifically for AI prototyping.
    -   This GPT guides the user by asking critical questions: product goal, intended user (e.g., "freelancers"), platform (e.g., "responsive web"), and key user flows (deliberately excluding generic flows like login/logout to focus on core problems).
    -   The output is a structured, markdown-formatted spec focused on front-end components and interactions, designed to be fed directly into AI prototyping tools.
    -   **Tool Strategy**: Use ChatGPT (or similar) for prompt clarity and generation (to save tokens), then Claude.ai for a quick, lightweight mock-run to visually validate the prompt's intent before using more robust tools.
-   **Workflow 2: Google Stitch + Google AI Studio for Divergent Design Exploration**:
    -   **Google Stitch** is leveraged for early-stage ideation and generating diverse design ideas from existing experiences (e.g., a screenshot of a real estate detail page's "Ask Redfin" section).
    -   It allows specifying context (e.g., business goals, user goals) and requests (e.g., "evaluate, identify improvements, generate better design ideas").
    -   The "YOLO mode" and "redesign model" features in Stitch are highlighted for generating highly divergent and creative design options.
    -   Designs from Stitch can then be exported to **Google AI Studio** to create interactive prototypes, bridging ideation with interaction design.
    -   **Google AI Studio Tips**: Utilize its hidden system instruction input for specific style or context, and its "annotate app" feature for collaborative feedback (similar to Figma's iteration).
-   **AI Prototyping Tools Comparison (from Genron's perspective)**:
    -   **Larable**: High quality, well-rounded, vibrant design aesthetics, many updates, paid. Ranked highest for design quality if price isn't a factor.
    -   **Vzero**: Similar quality to Larable, allows code editing without paid plan (more accessible), personal aesthetic preference. Ranked second.
    -   **Bolt**: Good for full-stack prototypes, strong integrations, but Genron uses it less for pure UI/UX prototyping.
    -   **Google AI Studio**: Relatively new vibe coding engine, free, catching up in design quality, more accessible. Ranked third for design quality.
    -   **Subframe Magic Patterns**: Specific for product design, similar to Larable/Vzero but no backend. Free for newsletter subscribers of the host.
    -   **Cursor**: Slower learning curve, not user-friendly for non-technical users, quality varies, not browser-based, good for serious building/code.
    -   **Replit**: Great for full-stack prototypes, good backend integration, but comes at a cost for the holistic experience.
    -   **Claude.ai**: Excellent for code-related tasks and quick mock-runs to validate prompt logic, but not a dedicated high-fidelity prototyping tool.
-   **The "Alpha" of AI**: The real power of AI is not doing a worse job of what humans already do, but enabling new "superpowers" to generate 15-16 different ideas, explore divergent solutions, and accelerate workflows. Those who master these AI superpowers will replace those who use AI generically.

## Use cases
-   **Product Managers**:
    -   Quickly generating initial product ideas and clarifying product goals.
    -   Creating lightweight PRD-like specifications for rapid AI prototyping.
    -   Validating design assumptions early in the product lifecycle.
    -   Understanding and mitigating AI-specific risks (bias, hallucination) in product outputs.
    -   Accelerating product strategy and design iteration cycles.
-   **Product Designers**:
    -   Overcoming the "blank canvas" problem by generating diverse initial design ideas.
    -   Streamlining the ideation-to-prototyping workflow.
    -   Exploring many divergent design variations rapidly (e.g., using Stitch's YOLO mode).
    -   Leveraging AI to create interactive prototypes based on specific design specs.
    -   Iterating on existing UI/UX elements and identifying actionable improvements.
-   **Engineers (learning product design or building prototypes)**:
    -   Quickly spinning up front-end prototypes with minimal design experience.
    -   Understanding how design thinking integrates with AI tools.
    -   Testing and validating different UI/UX approaches before full development.
-   **Startups/Innovators**: Rapidly prototyping new product concepts for market validation or investor pitches.
-   **Anyone facing creative blocks**: Using AI as a thought partner to generate novel ideas or variations that might be hard for a human to conceive quickly.

## Patterns & frameworks
-   **Design with AI Mind Map**: A comprehensive conceptual framework categorizing AI's application in design into four key areas: Prompting, Ideation, Design & Prototyping, and Staying Conscious. It serves as a mental model for understanding the full scope of AI's impact on product design.
-   **Prompting with AI Framework (Clarify, Context, Reference)**:
    -   **Clarify the Ask**: Before interacting with AI, define precisely what you want, what to include, and what to avoid. If unclear, ask AI for help.
    -   **Context Engineering**: Provide necessary (not excessive) context related to the goal, including role, unmet user needs, constraints (time, technical), existing ideas, prioritization criteria, audience, design principles, and brand guidelines. This "amplifies the effectiveness of the prompt."
    -   **References**: Offer examples (text, output format, visual, code) to guide AI towards better design outcomes.
    -   **Additional Tips**: Structure in/structure out, simplicity, "it's okay to be imperfect," and reverse prompting.
-   **Custom GPT for AI Prototyping PRD**: A structured process using a custom GPT (or similar AI assistant) that guides the user through specific questions (product goal, user, platform, key user flows) to generate a focused, front-end-centric design specification in markdown format. This acts as a "very first prompt" to AI prototyping tools, ensuring clarity and necessary guardrails.
-   **Divergent Design Exploration (Google Stitch YOLO mode)**: A pattern where tools like Google Stitch are used to generate multiple, highly varied design options from an initial prompt or screenshot. Activating "YOLO mode" (You Only Live Once) or "redesign model" maximizes creative range and divergence, allowing designers to quickly explore a wide array of potential solutions for a specific UI section.