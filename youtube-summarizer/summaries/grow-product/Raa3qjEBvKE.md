# The Most Important New Skill for Product Managers in 2026: AI Evals Masterclass

Video ID: `Raa3qjEBvKE`

## Summary
This video masterclass by Ana Chukla, an expert in AI evaluations (evals), argues that AI features frequently fail not due to the underlying models but due to a lack of proper evaluation. It emphasizes that Product Managers (PMs) must master AI evals as a critical new skill, especially by 2026, to ensure AI products are reliable, scalable, and meet user needs. The core of the masterclass is a detailed framework for creating effective evaluations, moving beyond introductory concepts to provide a practical, end-to-end flow for building and maintaining AI products. This content is highly relevant for aspiring AI PMs, existing PMs integrating AI, and anyone involved in scaling AI prototypes into production.

## Key insights
-   **Problem Statement**: AI features often fail because they are shipped without proper evaluations, leading to products that "lie" about their performance and impact. The non-deterministic nature of large language models (LLMs) means outputs vary, even for similar inputs, necessitating robust evaluation.
-   **The New Skill**: The most important new skill for PMs in the AI era is the ability to write effective evaluations, which serve as the "PRD for AI engineers," defining success criteria and expected behavior.
-   **Components of a GenAI Product**: A GenAI product comprises a language model (LLM or SLM), context engineering (RAG, prompts), tools, orchestrations (how components connect), and user experience (human-in-the-loop, latency).
-   **Example Use Case (AI Job Website)**: An AI-first job site could enhance job descriptions with summaries (<300 words), interview questions, required skills, learning guides, and quizzes. Evals would check factual accuracy, relevance, and adherence to constraints (e.g., summary length) using LLM judges or code.
-   **Why Prototypes Fail to Scale (5 Reasons)**:
    1.  **Data Drift**: Models trained on old data become irrelevant as user expectations or context evolve. Evals continuously monitor and detect this.
    2.  **Cost Considerations**: Prototypes often use the best (most expensive) models (e.g., GPT 5.1 at $10/million tokens). Evals help identify if cheaper models (e.g., GPT Nano at $0.40/million tokens – a 25x difference) can achieve similar quality, optimizing costs.
    3.  **Engineering Limitations**: Untested scalability, asynchronous behavior, etc. While not fully solved by evals, some aspects can be addressed.
    4.  **Guardrails**: Lack of defined feedback loops, fallback logic, and legal/ethical boundaries in prototypes. Evals define what the model should/shouldn't do, when to quit, or ask for help.
    5.  **Collaboration Failure**: Not directly eval-related, but good evals involve subject matter experts, fostering empathy and collaboration.
-   **MIT Study on AI Failure Rates**: A study by the Nanda committee at MIT suggests 95% of AI initiatives fail due to a "learning gap," meaning they either don't solve the right problems or fail to evolve with user feedback.
-   **Analogy of Tea**: Just as different people prefer different tastes of tea, LLMs, while factually correct, may not produce the *desired* or *consistent* user experience. Evals ensure the product meets customer preferences.
-   **Offline vs. Online Evals**:
    -   **Offline Evals**: Critical pre-deployment tests run before major releases, akin to alpha/beta testing. They ensure changes are correct and define the "PRD" for AI engineers.
    -   **Online Evals**: Continuous monitoring in production, observing product performance against evolving user expectations and data drift. They might be sampled (e.g., 1 in 100 queries) due to cost.
-   **Types of Evaluation Methods**:
    1.  **Code-based**: For definitive, objective metrics (e.g., text length, presence of keywords). Cheapest and most efficient.
    2.  **LLM as a Judge**: An LLM (often more intelligent than the product's base LLM) evaluates subjective aspects like relevance, tone, helpfulness, and adherence to guardrails.
    3.  **Human Evaluation**: Costly and time-consuming, used for new features, critical issues, or when LLM/code evals flag problems. Can be pass/fail or 1-5 ratings with remarks for deeper insights.
    4.  **Hybrid**: A combination where LLMs flag issues, and humans make final calls.
-   **Traditional ML Metrics (BLEU & ROUGE)**: These compare word overlap between generated and "golden" (reference) texts. They can be misleading for GenAI as they might show high scores even when semantic meaning is incorrect (e.g., "cat on the bed" vs. "cat on the mat").
-   **Evaluation is not QA**: PMs use evals to *transform* the product (improve prompts, models, orchestration), whereas QA roles primarily *inform* developers about issues.
-   **Real-Life Examples of Evals Impact**:
    -   **Grammarly**: Evals ensure tone accuracy, preventing significant meaning changes across many scenarios.
    -   **GitHub Copilot**: Lack of evals for minor ML file errors led to widespread production issues upon launch.
    -   **Clara**: Evals evolved to focus on business metrics (e.g., increasing checkout conversion rates via AI suggestions), not just user helpfulness.
    -   **Chatbots**: Continuous online evals prevent chatbots from giving outdated or irrelevant information due to data drift.
-   **Stakeholder Management Hack**: For critical documents (like eval plans), allocate 15-20 minutes at the start of a meeting for everyone to read it, ensuring engagement and alignment.
-   **Evals are an Ongoing Journey**: They are not optional guardrails but a continuous, evolving process that adapts as the product and user expectations change.

## Use cases
-   Developing AI-powered features for any product (e.g., chatbots, content generation, recommendation systems).
-   Product Managers taking on AI product roles or integrating AI into existing products.
-   Companies struggling to scale AI prototypes to production due to cost, quality, or consistency issues.
-   Ensuring legal, ethical, and safety compliance in AI outputs (guardrails).
-   Optimizing the cost of AI models by identifying opportunities to use cheaper alternatives.
-   Improving user experience and reliability of AI features by catching hallucinations or irrelevant outputs.
-   Establishing clear success criteria and performance metrics for AI engineers.
-   Managing data drift in AI systems by continuously monitoring performance in production.

## Patterns & frameworks
-   **Masterclass on Creating Effective Evaluations**: A comprehensive approach to understanding, building, and maintaining AI evaluations.
-   **Three-Part Evals Agenda**: A structured learning path for evals, covering AI product nuances, basic eval concepts, and a deep dive into LLM nature, metrics, and an end-to-end flow.
-   **5 Critical Components of GenAI Product**: A mental model for breaking down an AI product into its core elements: Language Model, Context Engineering, Tools, Orchestrations, and User Experience. Understanding these helps identify evaluation points.
-   **5 Reasons Prototypes Fail to Scale**: A diagnostic framework for identifying common pitfalls when moving AI prototypes to production: Data Drift, Cost Considerations, Engineering Limitations, Guardrails, and Collaboration Failure.
-   **End-to-End Evaluation Flow**: An 8-step process for developing and implementing evaluations:
    1.  **Define Success Criteria & Expected Behavior**: What should the product achieve and how should it behave?
    2.  **Transform to Metrics**: Convert criteria into measurable metrics (e.g., quality, UX, safety, performance).
    3.  **Create Base Product**: Develop an initial version with system prompts, models, tools, context, and orchestration.
    4.  **Create Data Set**: Gather diverse input data from past logs, research, synthetic generation (LLMs), and domain experts.
    5.  **Run & Analyze**: Test the data set against the base product and analyze outputs with expert remarks to identify errors and areas for improvement.
    6.  **Decide Evaluation Methods**: Choose appropriate methods (code, human, LLM, hybrid) for each metric.
    7.  **Write Evaluations**: Develop specific evaluation scripts or LLM prompts for each metric.
    8.  **Run Offline & Online Evals**: Conduct pre-release "offline" tests and continuous "online" monitoring in production, refining the product in a continuous loop.
-   **Latency Metrics (P50, P95, P99)**: A standard pattern for measuring system latency, focusing on percentiles (e.g., 99% of users experience latency below X ms) rather than simple averages to capture edge cases.
-   **Continuous Evaluation Improvement Loop**: A feedback mechanism where online and offline evaluation results continuously inform and improve the product's prompts, models, and overall design.
-   **Amazon Stakeholder Management Hack**: A meeting strategy to ensure critical documents are read: dedicate the first 15-20 minutes of a meeting for silent reading of the document.