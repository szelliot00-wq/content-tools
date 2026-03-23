# How to Design and Code with Claude Code and Figma MCP in 50 Min | Felix Lee

Video ID: `ydiMKfljb-I`

## Summary
This video demonstrates how designers can leverage AI coding tools like Claude Code and Figma's MCP (Multi-Modal Connector Protocol) to rapidly design and develop functional applications. Felix Lee, CEO of ADPList, showcases building complex websites and games directly within Claude Code from simple prompts or flowcharts, often bypassing traditional Figma-first design workflows. The core argument is that many designers are overly reliant on Figma and underutilizing powerful AI tools that can act as a "coding agent" to accelerate product creation, potentially making Figma a bottleneck. The content is highly relevant for designers, developers, and product managers seeking to integrate AI into their design-to-code pipelines for faster prototyping and development.

## Key insights
-   **Claude Code's High-Quality Output:** Felix emphasizes that Claude Code produces significantly higher quality code and "wins it all from a taste perspective" compared to other coding agents he's tried, such as Gemini AI Studio or Cursor's Codex, even with identical AI models.
-   **Rapid AI-First Development:** Felix, as a designer, built several full-stack applications (e.g., a personal website with AI chat, an ADPList globe visualizing live data, and a Growth Analyzer app with Stripe integration) primarily using Claude Code. The ADPList globe was built in about 12 hours, while the Growth Analyzer app took over 48 hours across three weeks, demonstrating rapid iteration.
-   **Figma MCP's Dual Capabilities:** The Figma Multi-Modal Connector Protocol (MCP) allows for two key workflows:
    *   **Design-to-Code:** It can convert a Figma design (e.g., a landing page) into a working, interactive web prototype in under 15 minutes, automatically integrating assets and reducing manual back-and-forth.
    *   **FigJam Flowchart-to-Code/Game:** It can interpret a FigJam flowchart (e.g., for a simple Flappy Bird game) and generate the corresponding functional code, building a playable game in minutes. Felix noted Claude likely "just knows how to build" the game based on the high-level concept rather than intricate flowchart details.
-   **New Code-to-Figma Function:** Figma recently launched a feature allowing users to convert a running local host web application (code) back into editable Figma components (SVGs), rather than just screenshots. While impressive for deconstructing designs, the video highlights a perceived irony as the design would still need to return to code for production.
-   **Designers Are Not "Freaked Out Enough":** Felix contends that most designers are overly reliant on Figma and are not actively exploring advanced AI coding tools. He notes that at ADPList, conversations about deep AI tools like Claude Code have only increased by 10-20% in the last six months, attributing this to the daunting nature of IDEs and terminals for many designers.
-   **Challenges in AI Visual Recognition and "Taste":** While powerful, AI visual recognition has limitations; for his Growth Analyzer app, Felix found Gemini Pro with Nano Banana performed better than Claude's Opus LM API for accurately identifying "hotspots" on a landing page. He is also personally trying to train Claude to replicate specific "taste" or design styles, finding it a significant challenge despite dedicated effort.
-   **Custom Claude Skills for Specialized Tasks:** Claude Code allows users to create custom "skills" – essentially text-based instruction sets – to guide the AI in performing specific tasks (e.g., a "UX Reviewer" skill for design critiques). Claude can even generate these skills itself based on user prompts, though Felix emphasizes the need to explicitly prompt Claude to "use skill" for it to be applied.

## Use cases
-   **Rapid Prototyping and MVP Development:** Quickly building functional web pages, apps, or even games from design mockups, text prompts, or flowcharts.
-   **Marketing and Growth Experimentation:** Creating landing pages, microsites, and A/B test variations with minimal developer overhead, allowing for faster market validation.
-   **Automated Design Feedback and Review:** Generating AI personas (Claude Skills) to conduct UX reviews, provide design critiques, or suggest copy improvements for landing pages and UIs.
-   **Bridging Design and Engineering Workflows:** Converting Figma designs into code for engineers to implement, or vice-versa, converting existing code into editable Figma components for design review and iteration.
-   **Learning and Experimentation for Designers:** Empowering designers to directly create and manipulate code without extensive prior coding knowledge, fostering a deeper understanding of how designs translate into functional products.
-   **Personal Website/Portfolio Creation:** Quickly developing feature-rich personal websites with custom functionalities like AI chatbots or dynamic data visualizations.
-   **Building Internal Tools/Utilities:** Generating simple applications or tools based on high-level requirements described in text or flowcharts.

## Patterns & frameworks
-   **AI-First Design / Vibe Coding:** This refers to Felix's methodology of commencing product development directly within an AI coding environment (like Claude Code) by providing prompts and iterating on the generated code, rather than starting with traditional design tools like Figma.
-   **Figma Multi-Modal Connector Protocol (MCP):** A Figma feature that enables seamless integration with AI agents. It facilitates several cross-platform workflows:
    *   **Design-to-Code:** Translating Figma design files into functional web code.
    *   **FigJam-to-Code:** Interpreting high-level flowcharts or diagrams created in FigJam into executable code (e.g., for a game or application logic).
    *   **Code-to-Figma:** A recently introduced feature that converts a running web application's code (e.g., from localhost) into editable vector components within a Figma canvas.
-   **Claude Skills:** A core functionality within Claude Code where users define custom instruction sets (text files) that guide Claude's behavior, persona, and output for specific tasks. These skills can be manually written or generated by Claude itself, allowing for tailored AI assistance (e.g., a "UX Reviewer" skill for structured design critiques).
-   **Iterative Prompting/Conversational Development:** The process involves continuously interacting with the AI agent by providing initial prompts, evaluating the generated output, and then issuing follow-up prompts to refine, add features, correct errors, or modify the design, mimicking a conversational approach to development.