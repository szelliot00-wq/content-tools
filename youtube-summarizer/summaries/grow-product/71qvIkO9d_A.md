# The PRD is dead. The Best PMs Are Replacing It With This

Video ID: `71qvIkO9d_A`

## Summary
The video, featuring Anker Goyle, CEO of Brain Trust, argues that the traditional Product Requirements Document (PRD) is "dead" in the age of AI, replaced by "evals" (evaluation systems). It emphasizes that the success of AI products is directly tied to the quality and continuous improvement of these evals, which act as quantifiable specifications for engineering teams. The discussion covers the critical role of evals in managing LLM unpredictability, enabling rapid experimentation, and building durable product differentiation, making them an indispensable skill for modern product managers and AI builders.

## Key insights
- **Evals are crucial for AI product success**: The success or failure of AI products is driven by the quality of evals, their effective use, and continuous improvement. Leading AI companies like Replit, Vercel, and Airtable utilize platforms like Brain Trust for this purpose.
- **Vibe checks are a form of eval**: Initial, informal "vibe checks" – where a user intuitively scores an AI product's output and iterates – are a valid starting point, described as the "do things that don't scale" approach for evaluations.
- **Scalability requires formal evals**: As an AI product grows and more people contribute, vibe checks become insufficient. Formal evals, supported by software, process, and tooling, are necessary to achieve predictable performance at scale.
- **Evals provide durability in AI development**: While LLMs, agent frameworks, and models constantly evolve (e.g., "all of that might change in a couple weeks or months"), investing in well-defined evals (encoding user needs as data and scorers) creates a durable asset. This enables continuous iteration and builds true product differentiation, unlike relying on current agent wiring.
- **The Product Manager's (PM) evolving role**: The modern PRD is an eval. PMs now provide quantifiable specs that engineering teams can use to measure software performance, gaining leverage by being responsible for improving the evals when the product falls short.
- **Addressing the "Claude Code controversy"**: The claim that coding tools like Claude Code don't use evals is countered by asserting that engineers using and providing feedback on the tool are, in effect, performing a type of eval. Structured evals become increasingly important as the "distance" between product builders (engineers) and end-users (e.g., doctors for a healthcare AI) grows, requiring PMs to bridge that intuition gap.
- **Brain Trust's rapid growth**: The company is approximately 100 people, serves "many hundreds of customers and many tens of thousands of organizations," and has seen "multiple orders of magnitude" consumption growth. Users now run 10 times more evals and log twice as much data daily compared to a year prior. They target companies with existing product-market fit that are earnestly adopting AI and uphold high quality standards (e.g., Zapier, RAMP).
- **AI enables rapid offline experimentation**: Unlike traditional software development where A/B testing is expensive and often done in production, AI allows for rapid "offline" experimentation (e.g., 12.8 experiments per day) directly on a developer's laptop using evals.
- **Components of an Eval**: An eval comprises three essential elements:
    1.  **Data**: A set of inputs (e.g., questions for a bot), potentially with ground truth answers.
    2.  **Task**: The AI system (e.g., an LLM call, an agent with tools) that processes the input and generates an output.
    3.  **Scores**: A function that evaluates the task output against the data, producing a normalized numerical score (0-1) to ensure comparability across different tests.
-   **Scoring function design**: While not every score needs to be binary, it's crucial to have clear, categorical criteria rather than asking an LLM to generate an arbitrary number. Overcomplicating scores should be avoided, but they can be iterated on to better reflect "vibe checks."
-   **Offline vs. Online Evals**:
    *   **Offline evals**: Testing in a simulated environment using a curated dataset to quickly iterate on prompts, models, and agents.
    *   **Online evals**: Deploying scoring functions on real-time production logs to assess how offline performance translates to actual user experience and identify problematic examples for inclusion in the offline dataset.
-   **Maintaining trust in evals**: The best teams view evals not as a gate, but as a core part of their iterative product improvement loop. A recommended ritual involves daily review of production examples to find novel patterns, adding them to the eval dataset, and then working to improve eval performance on those specific areas.
-   **The importance of failing evals**: It's crucial to have evals that *fail*. This indicates problems users are encountering or current limitations of the AI, providing clear targets for improvement and validating progress when new models or techniques emerge.
-   **Iterate quickly, don't perfect initially**: Instead of spending months creating a "perfect golden data set," it's more effective to "just jump in" with simple questions, run tests, confront outputs with intuition, and iterate quickly.
-   **Democratizing access**: Brain Trust removed user-based pricing to encourage wider adoption, allowing PMs, engineers, and domain experts to use the tool without cost barriers, recognizing that eval contribution shouldn't be limited to AI engineers.
-   **Loop Agent**: Brain Trust's internal AI agent (akin to Claude Code) assists in the eval process by interacting with data, prompts, and running evals, even suggesting prompt improvements and score adjustments. This showcases how models can "look at their own work and improve."

## Use cases
-   Product managers defining quantifiable success criteria and performance metrics for new AI features.
-   AI engineers testing and optimizing LLM prompts, model choices, and agent architectures.
-   Teams developing AI solutions for specialized industries (e.g., healthcare) where domain expertise is critical but engineers lack it, requiring PMs to bridge the knowledge gap.
-   Companies needing to rapidly experiment and iterate on AI product improvements in an offline environment before deployment.
-   Debugging and understanding why an AI application is not meeting user expectations or failing in specific scenarios.
-   Prioritizing product roadmap items based on insights from online eval performance and identifying areas where the AI needs significant improvement.
-   Gathering structured feedback to communicate specific use case requirements and performance issues to external LLM providers.
-   Any team building internal or external AI-powered tools that need consistent, measurable quality.

## Patterns & frameworks
-   **Evals as the Modern PRD**: A concept where traditional, qualitative Product Requirements Documents are replaced by quantifiable evaluation systems. These evals serve as living, measurable specifications that define how well an AI product should perform, enabling engineering teams to build towards objective criteria and empowering PMs to directly improve product quality.
-   **Vibe Checks as "Do Things That Don't Scale" Analog**: Vibe checks are presented as a fundamental, intuitive form of evaluation, especially in early-stage AI product development. This aligns with Paul Graham's principle of "do things that don't scale," suggesting that manual, qualitative assessment by product builders is valuable before formal systems are required for scale.
-   **Three Components of an Eval (Data, Task, Scores)**: A framework for structuring any AI evaluation:
    1.  **Data**: The set of inputs (e.g., user queries, scenarios) that the AI system will process, optionally including ground truth or expected outputs.
    2.  **Task**: The AI system itself (e.g., an LLM, an agent, a prompt pipeline) that takes the input data and generates an output.
    3.  **Scores**: A function or set of criteria that assesses the output of the task against the input data (and optional ground truth), producing a normalized numerical value (0-1) to measure performance and allow for comparison.
-   **Offline vs. Online Evals Flywheel**: An iterative process for continuous AI product improvement:
    *   **Offline Evals**: Conducted in a controlled environment (e.g., a development playground) using a curated dataset to rapidly test and iterate on AI model, prompt, and agent changes.
    *   **Online Evals**: Deployment of the same scoring functions to run on real-time user logs in production. This provides insight into real-world performance discrepancies and feeds poorly performing examples back into the offline dataset, creating a continuous feedback loop.
-   **"Evals That Fail" Principle**: A mental model emphasizing the importance of having evaluation scenarios where the AI product performs poorly. These failing evals are crucial indicators of existing user problems, current model limitations, and serve as targets for improvement, signaling when new models or architectural changes could unlock significant gains.
-   **Model Context Protocol (MCP)**: A standard or API that enables LLMs to interact with external tools and data sources (e.g., a Linear task management server), allowing AI agents to perform complex actions, research, and retrieve specific information beyond their base knowledge.
-   **Brain Trust's "Loop" Agent**: An example of an advanced AI agent (similar to self-improving code assistants) integrated into the eval platform. It can automate parts of the eval workflow, such as generating test data, suggesting prompt modifications, or refining scoring functions based on observed performance, demonstrating the potential for AI to aid in its own evaluation and improvement.