# Every Level of Claude Code Skills in 27 mins

Video ID: `-u_igSQHAIo`

## Summary
This video details a seven-level framework for building increasingly sophisticated Claude Code skills, moving beyond basic instructions to creating self-improving, context-aware, and integrated AI workforces. It starts by defining what a skill truly is—a folder of structured knowledge—and progresses through best practices for efficient skill design, leveraging existing marketplace skills, infusing business context, and implementing robust evaluation and self-learning mechanisms. The framework is designed for anyone building Claude skills, especially business owners aiming to automate their operations and marketing with AI specialists that sound like their brand.

## Key insights
-   **Level 1: Understanding Skill Structure:** A skill is fundamentally a folder of knowledge, comprising a mandatory `skill.md` (the "brain" or SOP) and optional `scripts`, `references`, and `assets` folders. Claude utilizes "progressive disclosure" with three tiers of information loading: YAML front matter (always loaded, max 15,000 characters), `skill.md` body (loaded upon activation), and other files (pulled only when specifically referenced and needed).
-   **Level 2: Building Lean, Effective Skills:** The "golden rule" is to keep `skill.md` under 200 lines, serving as a table of contents that points to detailed information within `references` folders to avoid context window bloat and improve performance. Skill descriptions in the YAML front matter should follow a three-step framework: define triggers, define anti-triggers, and state the outcome, as marketplace skills often have low (around 20%) activation rates due to vague descriptions.
-   **Level 3: Refactoring Existing Skills:** Many marketplace skills are poorly structured (e.g., 1,000-line `skill.md` files). Users can "grab, install, and make their own" by refactoring them using Claude's `skill creator skill` to apply Level 2 principles, abstracting information into `references` folders and improving descriptions. An example cited is refactoring an AI SEO skill from 400 lines to 148 lines.
-   **Level 4: Infusing Business Context:** To move beyond generic outputs, skills need specific business context (brand guidelines, audience personas, tone of voice, competitors). This context should be stored in `references` folders (either skill-specific or shared) and referenced within `skill.md` through a "context needs chart" to ensure Claude understands the brand's unique attributes and desired outcomes.
-   **Level 5: Evaluation and Benchmarking:** Anthropic's `skill creator skill` includes evaluation and benchmarking features. Users can test skills against specific criteria (e.g., three to five criteria at a time for thorough review) and perform A/B tests (e.g., with and without a specific reference file) to measure output quality, identify improvements, and optimize token usage. Results are hosted locally, providing a structured report.
-   **Level 6: Self-Improving Skills:** Implement a feedback loop where skills learn from every interaction. Observations or rules (e.g., "articles that open with a direct answer rank faster") are captured in a `learnings.md` or `rules` section within `skill.md`, often updated by a "wrap-up skill" at the end of a session. This file should be regularly pruned to prevent new context bloat.
-   **Level 7: Integrated AI Workforce:** The ultimate level involves skills working together in comprehensive workflows, rather than isolated tasks. An example provided is a copywriting skill pulling in brand context, then passing output through a "humanizer" skill, or a content repurposing skill leveraging a YouTube transcript tool. This creates a coordinated system that benefits from shared foundational skills (voice profile, positioning, ICP).

## Use cases
-   **Automating Marketing Strategy & Operations:** For business owners seeking to automate parts of their marketing (e.g., trending research, SEO optimization, content creation, copywriting).
-   **Content Creation & Optimization:** Developing skills that generate high-quality, on-brand content, and then evaluate or self-improve its effectiveness for AI search rankings.
-   **Market Research:** Building skills to gather and analyze trending topics from platforms like Reddit and X.
-   **Agent Building for LLMs:** Developers or advanced users creating complex, multi-functional agents with Claude, ensuring they are lean, efficient, and contextually relevant.
-   **Refactoring and Improving Existing Tools:** Taking pre-built or marketplace skills and optimizing their structure and performance according to best practices.
-   **Personalizing AI Outputs:** Ensuring AI-generated content or responses align with a specific brand's voice, audience, and strategic positioning.
-   **Performance Measurement:** Systematically evaluating the quality and effectiveness of AI skill outputs through benchmarking and A/B testing.

## Patterns & frameworks
-   **Progressive Disclosure:** A tiered information loading system for Claude skills.
    1.  **Tier 1 (YAML Front Matter):** Name, description, triggers, always loaded into context (limit ~15,000 characters).
    2.  **Tier 2 (Skill.md Body):** Process steps, loaded only when the skill is activated.
    3.  **Tier 3 (References, Scripts, Assets):** Deep knowledge, code, templates, pulled only when specifically needed by instructions in `skill.md`.
-   **Golden Rule of Skill Building:** Keep your `skill.md` under 200 lines maximum. This makes `skill.md` function as a concise "table of contents" for Claude, guiding it to relevant, detailed information in `references` folders only when necessary.
-   **Skill Description Framework:** A three-step method for writing effective YAML descriptions to improve skill activation:
    1.  **Trigger:** Define the event or keywords that should activate the skill.
    2.  **Anti-Trigger:** Specify situations or keywords that should *not* activate the skill.
    3.  **Outcome:** Clearly state what the skill does and the output it produces.
-   **Context Needs Chart:** A method within `skill.md` to explicitly reference specific contextual information (e.g., brand positioning, ICP summary) from shared or skill-specific `references` folders, ensuring relevant brand context is loaded only when needed for a particular step or task.
-   **Feedback Loop / Learning Loop:** A mechanism for skills to self-improve by capturing observations and successful patterns. This involves a `learnings.md` or `rules` file within the skill's context, which is updated (often by a "wrap-up skill" at the end of a session) and referenced by `skill.md` in subsequent runs. The learnings file should be regularly pruned to maintain efficiency.
-   **Agentic OS (Presenter's System):** A named example of an integrated "AI workforce" built using these principles, comprising 20+ production skills across marketing, strategy, operations, and visuals, all sharing a central brand context folder for consistent, personalized outputs.