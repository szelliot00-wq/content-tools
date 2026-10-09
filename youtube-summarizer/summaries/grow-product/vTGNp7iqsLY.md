# Product Builders Getting Paid 20%+ More | Ankit Shukla | Product Growth

Video ID: `vTGNp7iqsLY`

## Summary
Ankit Shukla, founder of Hello PM, makes the case that "product builder" is a real and rapidly growing role — not hype — based on analysis of 12,500 job postings. The core argument is that AI has compressed the discovery, delivery, and distribution pipeline enough that product people who can identify the right AI use cases and build working prototypes are commanding a 15–50% salary premium over traditional PMs. The video walks through the POWER framework for structuring AI adoption, a five-level engineering ladder for building AI products, a step-by-step roadmap for landing a product builder role, and a live case study of building a production email marketing platform overnight using Claude Code. It is most relevant to PMs, engineers, analysts, marketers, and anyone in a problem-solving role who wants to stay competitive and command higher compensation in an AI-first job market.

---

## Key insights
- **The role is data-backed, not hype.** Analysis of 12,500 job postings found that 30%+ of PM roles now require meaningful AI skills — not just tool familiarity, but judgment about when AI should and should not be applied.
- **Salary premiums are substantial.** AI/product builder roles pay 15–20% more than traditional counterparts in the US and Europe, and 30–50% more in India. US median AI PM salary is ~$195K; senior roles range $250K–$560K; top labs can reach $800K+. Netflix advertised an AI PM role at up to $900K.
- **India-specific numbers.** Freshers with AI skills: 12–16 LPA. Two years experience: ~22 LPA. Senior (5+ years + AI portfolio): significantly higher, with top-lab roles pushing well above that.
- **The biggest bottleneck was always delivery, not discovery.** Historically, PMs had to be highly selective about what reached engineering because building was slow. AI-assisted coding (Claude Code, Cursor, etc.) has collapsed that constraint, enabling rapid prototyping and experimentation without engineering bandwidth.
- **The #1 skill companies pay for is use-case identification, not engineering.** Across 12,000+ job descriptions, identifying the right AI use case ranked above RAG, agentic AI, or prompt engineering. The judgment about what to build (and what not to) is the scarce commodity.
- **Empathy at scale via AI personas.** Ankit's Hello PM team fed 200 student intro-call transcripts into Claude, generated representative user personas, and now runs every product decision through those personas — enabling systematic empathy without individual 1:1s.
- **The overnight build case study.** Ankit built a production-grade email marketing platform (replacing a $550–700/month third-party tool) in ~24 hours using Claude Code + AWS MCP, with no prior Node.js/TypeScript experience. The system handles 120K subscribers, 1M+ emails/month, and includes segmentation, A/B testing, automations, and documentation — at a projected AWS cost of ~$110/month.
- **The 80/20 split in AI-assisted building.** Claude can get a product to ~80% quickly; the last 20% (edge cases, security, production hardening) still requires human judgment. In most companies, PMs build the prototype; engineers own the last mile.
- **Don't start with tools.** The most common mistake is jumping into N8N, Make, or Zapier before understanding the problem space. Tool knowledge creates a false sense of progress. Problem-first thinking (the POWER framework) is what produces actual ROI.
- **LinkedIn killed its APM program and replaced it with an Associate Product Builder program** — a concrete signal that the industry is formalizing this role.

---

## Use cases
- **PMs who want a salary increase** without switching companies — acquiring AI skills and building a portfolio can unlock a 15–50% premium.
- **Engineers transitioning to product** — technical background is a strong foundation; add use-case judgment and discovery skills.
- **Analysts, marketers, or customer success managers** moving into product — domain expertise and customer empathy are existing strengths to leverage.
- **Founders or solopreneurs** building internal tools — the case study demonstrates replacing SaaS spend with a custom-built production tool at a fraction of the cost.
- **PMs at traditional companies (fintech, healthtech, banking)** — internal productivity use cases (credit underwriting automation, analytics briefings, research synthesis) are immediately applicable without building AI-native products.
- **Anyone doing repetitive research tasks** — competitive analysis, meeting summaries, user interview synthesis, PRD drafting — all can be systematized via skills and connectors.
- **Job seekers breaking into AI PM roles** — the roadmap (align → acquire skills → reach out → cold outreach with portfolio) gives a concrete 1–4 month path.
- **PMs preparing for interviews** — simulating edge-case questions about their AI projects using Claude is a specific, actionable prep tactic.

---

## Patterns & frameworks

### POWER Framework
A five-step framework for getting measurable ROI from AI in any company or role:
- **P — Possibilities:** Research what AI can do broadly (across industries, competitor case studies, Anthropic/OpenAI customer story pages). Build a database of possibilities before narrowing. Uses the UTG sub-framework: AI can *Understand*, *Transform*, and *Generate* text/content/code.
- **O — Opportunities:** Map your company's specific workflows and identify where AI application would generate ROI. Never pick just one use case — look at the whole picture first. Two types: optimization (doing existing tasks faster) and innovation (entirely new capabilities that weren't attempted before).
- **W — Workflow:** Go deep on exactly how work currently gets done. Conduct internal stakeholder interviews. Understand step-by-step processes before designing AI interventions. This is where you identify both optimization gaps and innovation gaps.
- **E — Engineering:** Only after P-O-W does tool selection happen. Choose the right level (see Engineering Ladder below). Starting here is the most common and costly mistake.
- **R — Results/ROI:** Measure the actual impact. The framework is explicitly oriented toward producing measurable business outcomes, not just AI adoption metrics.

---

### Five-Level Engineering Ladder
A hierarchy of AI implementation complexity, used to match the right tool to the right problem:
- **Level 0 — Prompting:** Direct use of ChatGPT/Claude.ai. Good for one-off tasks; inefficient for recurring work.
- **Level 1 — Reusable Prompts:** Google Gems, Custom GPTs. Encapsulate recurring workflows (e.g., a resume optimizer gem, a PRD generator). Limitation: context switching between windows; context length limits.
- **Level 2 — Skills + Connectors:** Claude Code skills (progressive disclosure — skills load only when relevant, preserving context). Connectors link Gmail, Slack, Calendar, PostHog, Amplitude, Tableau, GitHub directly. Best practice: do the task with Claude first, then ask Claude to generate the skill from the conversation.
- **Level 3 — Vibe Coding:** Build custom interfaces and tools users interact with directly (Google AI Studio recommended as a free starting point). More autonomy and control than connectors.
- **Level 4 — AI Workflow Automation:** N8N, Make, Zapier for backend automations that run without human initiation (e.g., auto-research incoming leads, auto-generate daily analytics briefings). These platforms now have AI assistants that generate workflows from prompts.
- **Level 5 — Agentic / Loop Engineering:** Claude Code + Cursor + MCPs (AWS, Vercel, etc.) for production-grade applications. AI plans, executes, evaluates, and iterates autonomously. This is where the email platform case study lives.

---

### Product Builder Roadmap (Job-Landing Steps)
A sequenced job search strategy:
1. **Step 0 — Align:** Review 25–30 AIPM job descriptions. Build a personal skills map manually (no AI). Identify existing strengths (domain, technical, customer-facing) vs. gaps.
2. **Step 1 — Acquire Skills:** Learn via YouTube, then build something concrete. Reach out to 10+ active AI PMs on LinkedIn, offering to compensate for their time (most won't take money but will help).
3. **Step 2 — Reach Out:** Apply across at least 5 job platforms (LinkedIn, Instahire, Indeed, Wellfound, AngelList). Always include portfolio/built projects.
4. **Step 3 — Cold Outreach with Work Product:** Pick 25–30 target companies. Build a deck, prototype, or research doc answering "what would I do in my first 6 months as PM here?" Send to 2+ decision-makers per company via Apollo or Rocket Reach. Follow up 3 times before moving on.

---

### Interview Preparation Framework (Three Round Types)
- **Round 1 — Fitment/Behavioral:** Match your background and domain to the company's JD. Portfolio projects in the target domain substitute for direct experience.
- **Round 2 — Product Sense:** Standard PM questions (improve this product, measure success of X). Classic judgment and empathy questions.
- **Round 3 — AI/Project Deep Dive:** Interviewers probe edge cases of your built projects (e.g., "what happens to your RAG system with 100M documents?", "how do you evaluate model quality?"). Build projects you can defend thoroughly under pressure.