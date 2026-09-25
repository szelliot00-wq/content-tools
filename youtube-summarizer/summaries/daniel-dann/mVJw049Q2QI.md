# I Built a Full Website With AI (Gemini 3.8 Flash)

Video ID: `mVJw049Q2QI`

## Summary
Daniel demonstrates building a fully functional bakery website with online ordering and Stripe payments using a single prompt in the AI platform Runnable, powered by Gemini 3.8 Flash, in under 10 minutes and without writing any code. The video walks through the entire workflow: from prompt input and agent clarification questions, to live site generation, customer checkout testing, and back-end dashboard management. The core argument is that Runnable collapses the typical multi-tool project workflow into a single collaborative AI workspace. This video is most relevant to entrepreneurs, small business owners, and non-technical product managers who want to rapidly prototype or launch functional web products.

## Key insights
- **One prompt, full product**: A single natural language prompt produced a working bakery website with a menu, cart, pickup scheduling, Stripe checkout, and back-end dashboard — all in under 10 minutes.
- **Agent asks clarifying questions first**: Rather than immediately generating output, Runnable's agent pauses to gather context — asking about visual style (offering design direction options) and requesting a Stripe API key — before building anything.
- **Transparent build process**: The platform shows the agent's planning and assembly steps in real time rather than hiding work behind a loading screen, making the process feel auditable and less like a black box.
- **Persistent project context**: Unlike one-shot AI tools, Runnable maintains context across the entire project lifecycle, allowing the user to continue refining and editing the same project without starting over.
- **Non-destructive editing**: After generation, the project remains fully editable. Changes apply immediately without triggering a full rebuild, which also conserves platform credits.
- **Integrated dashboard**: The same workspace includes analytics (traffic and visitor behavior), SEO controls, domain management, Stripe payment integration, and a secrets vault — no external tools required.
- **Scheduled recurring tasks**: Runnable supports automated recurring agent tasks (e.g., research local bakery competitors every Monday at 8 a.m., compile a report on promotions, menu trends, and pricing, then send an email notification).
- **Customer journey testable immediately**: The author tested the full ordering flow — browsing the menu, selecting a pastry, scheduling pickup, and completing Stripe payment — confirming the checkout worked end-to-end before any manual configuration.
- **First draft as foundation**: The generated site is described as a "real starting point rather than a rough draft," meaning it is polished enough to build on rather than throw away.

## Use cases
- **Solo founders / small business owners** launching a simple e-commerce or service site without a developer.
- **Product managers** who need a functional prototype to demo to stakeholders or investors quickly.
- **Freelancers or agencies** looking to generate a first-draft client site before customizing it further.
- **Non-technical entrepreneurs** who want to validate a business concept (e.g., a local bakery) with a real checkout flow before committing to a full build.
- **Marketers** who need a landing page with payments and basic analytics without waiting on an engineering queue.
- **Recurring competitive intelligence**: Anyone who needs regular automated research reports on competitors (pricing, promotions, menu trends) delivered on a schedule.

## Patterns & frameworks

**Single-prompt-to-full-product workflow**
The overarching pattern: describe what you want to build in one prompt → agent asks clarifying questions → agent builds iteratively with visible steps → you test and edit → publish. This compresses what normally requires a content tool, a design tool, a code editor, a payment integration, and an analytics dashboard into one linear conversation.

**Clarification-before-generation**
Rather than generating immediately, the agent front-loads context gathering (design style, API keys, business requirements). This reduces rework and aligns the output to intent before any credits or time are spent building.

**Persistent collaborative workspace (vs. isolated task tools)**
Runnable is positioned against the "one tool per task" model. The framework is: keep the project, its history, and all its settings inside one environment so every subsequent action builds on prior context rather than starting fresh.

**Transparent incremental build**
The build is shown step-by-step rather than delivered all at once. This is a trust-building pattern: users can follow along, catch misalignments early, and feel confident in what was generated.

**Edit-in-place (non-destructive iteration)**
Changes are applied to the live project directly, not by regenerating from scratch. This makes the first output a foundation rather than a throwaway, and preserves credits by avoiding unnecessary reruns.

**Scheduled agent tasks**
A recurring automation pattern: define a task (research competitors), set a schedule (every Monday at 8 a.m.), define a delivery channel (email), and let the agent run it autonomously — no manual triggering required.