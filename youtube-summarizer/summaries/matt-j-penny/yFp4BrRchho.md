# Stop Making Ugly AI Websites (Google Stitch & Claude Tutorial)

Video ID: `yFp4BrRchho`

## Summary
This video demonstrates a detailed, step-by-step process for non-developers to create professional, beautiful websites using AI tools, dubbed "Vibe Coding." It outlines how to move from inspiration to a live, functional website by leveraging Google Stitch for AI-powered design, Claude Code for generating code from those designs, and then deploying the project using GitHub and Vercel. The core argument is that by integrating these advanced AI tools, especially through a Multi-modal Collaboration Protocol (MCP), anyone can build sophisticated web applications quickly and efficiently, eliminating the "ugly AI website" problem. This process is particularly relevant for beginners, business owners with ideas for software tools but lacking development skills or budget, and individuals looking to turn their concepts into reality.

## Key insights
-   **Structured Workflow for Web Development:** The video presents a 7-step process: (1) find inspiration websites, (2) export/screenshot designs, (3) create a basic Product Requirements Document (PRD) using an LLM, (4) use Google Stitch to create designs, (5) edit designs in Stitch, (6) connect Stitch via MCP to Claude Code to build the site, and (7) create GitHub repos and Vercel projects to deploy live.
-   **Inspiration & Design Export:** Websites like Awards.com can be used for design inspiration. The GoFullPage Chrome extension is recommended for taking full-page screenshots, which should then be compressed to under 5 megabytes (e.g., from 24MB to 4.3MB JPEG) for optimal AI tool processing.
-   **AI-Assisted Planning (PRD):** Tools like Gemini (or Claude/ChatGPT) can generate a basic PRD. This can be enhanced by feeding it a voice prompt, the inspiration screenshot, the website URL, and scraped data (like branding, colors, fonts, icons) obtained using a tool like Firecrawl, ensuring the AI has comprehensive guidelines.
-   **Google Stitch for AI Design:** stitch.withgoogle.com allows users to prompt for professional-level designs, select elements, and make AI-driven or manual edits. It generates design systems (color palettes, fonts) and complete pages (e.g., homepage, services, portfolio, contact us). Users can upload their own images, specify model quality (Flash for speed/cost, 3.1 Pro for best quality), and regenerate variations of pages.
-   **Seamless AI Coding with Claude Code via MCP:** The Multi-modal Collaboration Protocol (MCP) is crucial for connecting Stitch to Claude Code. After setting up the Stitch API key in Claude Code, users can copy an MCP prompt from Stitch that includes project and screen IDs. This allows Claude Code to "see" and accurately build out the designs created in Stitch, ensuring the coded website is almost identical to the designs.
-   **GitHub for Version Control:** A GitHub repository is created (e.g., "Roofing Demo") to store the website's code. Claude Code can commit and push the generated code directly to GitHub, provided it's configured with GitHub MCP access.
-   **Vercel for Easy Deployment:** Vercel (free account available) is used for quick and easy deployment. After granting Vercel access to the GitHub repository, importing the project, and clicking deploy, the website goes live on a real, accessible URL within minutes.
-   **"Vibe Coding" Concept:** The presenter promotes "Vibe Coding" as a method for individuals with great ideas but lacking traditional coding skills or development budgets to build real-world software tools and applications, not just static websites. A free three-day course is offered for those interested in learning more.

## Use cases
-   **Small Business Website Creation:** Quickly generate and deploy professional websites for local businesses (e.g., roofing, electricians) without hiring a web developer.
-   **Personal Project Development:** Individuals can bring personal website ideas or simple web applications to life with minimal coding knowledge.
-   **Validating Software Concepts:** Rapidly prototype and deploy functional web apps to test market viability for new business ideas or software tools.
-   **Non-Technical Founders:** Entrepreneurs can bypass the need for a technical co-founder or expensive development agencies for initial product builds.
-   **Content Creators/Bloggers:** Easily design and deploy custom, visually appealing websites to host content.
-   **Employees in Non-Technical Roles:** Build internal tools or departmental websites without needing to rely on IT or development teams.

## Patterns & frameworks
-   **Vibe Coding:** A philosophy and methodology emphasizing the use of AI tools to build software and web applications without traditional coding expertise, enabling non-developers to turn their ideas into reality.
-   **The 7-Step Web Creation Workflow:** A structured, repeatable process for end-to-end website development using AI tools:
    1.  **Inspiration Gathering:** Finding existing designs to mimic or draw elements from.
    2.  **Design Export:** Capturing inspiration visuals (e.g., full-page screenshots).
    3.  **PRD Generation:** Using an AI (LLM) to create a basic Product Requirements Document, outlining features and pages, enriched with scraped branding data.
    4.  **AI Design (Google Stitch):** Prompting an AI design tool to generate initial visual layouts based on the PRD and inspiration.
    5.  **Design Refinement:** Iteratively editing and modifying the AI-generated designs within the tool, either manually or through AI prompts.
    6.  **AI Coding (Claude Code via MCP):** Leveraging a Multi-modal Collaboration Protocol (MCP) to send the finalized designs from the design tool to an AI coding tool, which then generates the actual website code.
    7.  **Deployment (GitHub & Vercel):** Using version control (GitHub) and a deployment platform (Vercel) to host the generated code and make the website live on the internet.
-   **Multi-modal Collaboration Protocol (MCP):** A crucial integration pattern that allows different AI tools (e.g., Google Stitch and Claude Code, or Claude Code and GitHub) to communicate seamlessly. This enables a high degree of accuracy, where code generated by one AI precisely matches designs created by another, preventing discrepancies that often arise from manual interpretation or traditional handoffs.