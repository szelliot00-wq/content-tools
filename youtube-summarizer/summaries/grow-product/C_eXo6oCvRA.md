# Designing With AI With Designers of Figma & Codex

Video ID: `C_eXo6oCvRA`

## Summary
This video features Ed Baze (Head of Design for Codeex at OpenAI) and Gee Seiya (Head of Design for AI at Figma) discussing the evolving landscape of product design in the age of AI. They address the "design in code versus design in canvas" debate, asserting it's a false dichotomy and that modern designers must seamlessly navigate both. The core argument is that AI tools are blurring traditional roles, accelerating workflows, and empowering individuals to move fluidly between conceptual exploration in Figma and functional implementation in code (like Codeex), ultimately making design a potential bottleneck if not adapted. This conversation is highly relevant for designers, product managers, and engineers seeking to understand and adopt cutting-edge AI-driven product development workflows.

## Key insights
-   **False Dichotomy:** The debate between designing in code versus designing in a canvas (like Figma) is a false dichotomy. The future of design involves seamlessly navigating between both, leveraging the strengths of each for different stages of the process.
-   **AI Accelerates Workflows:** AI has drastically accelerated developers (estimated 10x), while designers have seen an acceleration of approximately 1.5x to 2x. This makes design a potential bottleneck if designers don't adapt to new AI-powered tools and workflows.
-   **Evolving Workflow:** The traditional "low-fidelity to high-fidelity" design process is changing. A "low-fidelity" start can now be a functional wireframe generated directly in Codeex, providing more dimensionality from the outset.
-   **Seamless Handoff Example (Codeex to Figma and back):**
    -   Designers can prototype interactions in Codeex (e.g., a dynamic composer system for an OpenAI product).
    -   To refine pixel-perfect details, specific components or entire screens can be imported from Codeex into Figma with a single command (`@Figma import my homepage...`).
    -   Figma provides a snapshot where elements are responsive and accurately reflect code's padding, border radius, etc., making design changes straightforward.
    -   After making design adjustments in Figma (e.g., changing colors, labels), a link to the modified component can be copied back into Codeex with a command like "update my code with the change I made here," updating the codebase.
    -   This process significantly reduces "lossiness" and manual translation between design and development.
-   **Integration of Design Systems:** Newer Figma tools allow for the import of design tokens and local styles from the actual design system into the Figma file, ensuring designers work with an accurate representation, not just a facsimile. This enables aligned sources of truth across storybook, GitHub, and Figma.
-   **Blurring Roles & Empowered Teams:**
    -   At OpenAI's Codex, designers often code, with Ed Baze spending 70-80% of his time coding, reflecting the developer-forward nature of their product.
    -   At Figma, teams previously "AI curious" are now "banging down the door" to use AI. Designers are working directly in staging environments, building technically accomplished prototypes, and even shipping polish to production (submitting PRs).
    -   This empowerment allows projects to start at various stages and enables teams to work on previously low-priority (P2) projects, accelerating shipping velocity.
-   **Importance of AI Model & Hygiene:** OpenAI's Model 54 significantly improves reliability and interoperability with Figma MCP. Good "design hygiene" (e.g., naming components well, aligning design systems with CSS tokens) is crucial for effective collaboration with AI agents.
-   **Accessibility & Learning:** Anyone, regardless of technical background (GTM, finance, comms), can start using AI tools like Codeex or ChatGPT to build things (e.g., an iOS app, event seating plan, honeymoon planning app) by simply asking questions. AI acts as an "incredibly patient tutor" that never clocks out.
-   **Curiosity as a Defining Skill:** In this rapidly changing AI era, curiosity is paramount. The ability to ask "What does that mean for what I'm doing?" and "How can I find out a little bit more?" fosters adaptability and success.

## Use cases
-   **Designers:**
    -   Rapidly exploring layout ideas and overall user flows in a canvas (Figma).
    -   Diving deep into interaction design, testing responsiveness across breakpoints, and finessing component states in code (Codeex).
    -   Achieving pixel-perfect designs, managing design systems, and ensuring brand consistency in Figma.
    -   Contributing directly to codebase (shipping PRs) for small styling tweaks or string changes.
    -   Recreating inherited design files and understanding undocumented design decisions from existing codebases.
-   **Product Managers:**
    -   Quickly building and stress-testing working prototypes ("prototypes, not PRDs") for new features.
    -   Exploring product decisions and shaping strategy roadmaps with AI assistance.
    -   Writing more coherent executive briefings by leveraging AI to understand complex data or frameworks.
-   **Engineers:**
    -   Collaborating more seamlessly with designers, receiving design updates directly in code.
    -   Leveraging AI to debug, understand data architecture, or identify redundant systems in a codebase.
-   **Teams (Design, PM, Engineering):**
    -   Streamlining the handoff process between design and development by using integrated tools.
    -   Maintaining aligned sources of truth across design files, codebases, and design systems.
    -   Accelerating the development and shipping of 0-to-1 products and even revisiting previously deprioritized projects.
    -   Onboarding new team members by using AI to explain complex systems or codebases.
-   **Individuals (Technical & Non-technical):**
    -   Learning to code or understand complex technical concepts by asking AI questions.
    -   Building personal projects (e.g., iOS apps, interactive web tools, travel planners) without extensive prior technical expertise.
    -   Interrogating systems and finding opportunities for contribution or thinking differently in various industries, including regulated ones like healthcare or financial services, even if company tools are limited.

## Patterns & frameworks
-   **Design in Code vs. Design in Canvas (False Dichotomy):** The initial problem framed as two opposing methods. The resolution is that AI allows for seamless navigation between both, making it a "right tool for the job" decision rather than an either/or.
-   **AI as a Patient Tutor / Partner:** A mental model where AI (like ChatGPT or Codeex) is viewed as an infinitely patient assistant or teacher that can explain complex concepts, help learn new skills (like coding), and collaborate on tasks, adapting to the user's level of understanding.
-   **Prototypes, Not PRDs:** A shift in product management strategy where working prototypes, often built quickly with AI-powered tools, are prioritized over or used in conjunction with traditional Product Requirements Documents (PRDs) for faster validation, feedback, and shared understanding within the team.
-   **Total Football (70s Holland Football Metaphor):** A metaphor describing a team dynamic where traditional role boundaries diffuse. Individuals (designers, PMs, engineers) develop "spikes" in their core areas but can also "cover" or contribute across other domains, creating a more fluid, adaptable, and powerful team.
-   **Curiosity as the Defining Skill:** This is highlighted as the most crucial trait for individuals to succeed in the rapidly evolving AI landscape, enabling continuous learning, adaptation, and the ability to leverage new tools effectively.
-   **Seamless Handoff Workflow:** A specific, AI-enabled process where design iterations in a visual tool (Figma) can be directly applied to and updated in a codebase (Codeex), and vice versa, minimizing manual specification, potential errors, and lossiness during translation.