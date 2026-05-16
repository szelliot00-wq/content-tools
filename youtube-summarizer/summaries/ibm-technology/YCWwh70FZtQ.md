# AI skills security, Open AI Deployment Company & zero days

Video ID: `YCWwh70FZtQ`

## Summary
This episode of *Mixture of Experts* covers three major AI topics: IBM Research's Malia skills compiler for securing agentic AI workflows, OpenAI's new "Deployment Company" consulting venture, and Google's disclosure of AI-assisted zero-day vulnerability discovery. The panel features IBM Fellows Kush Varshney and Aaron Botman, cybersecurity expert Dustin Haywood (aka Evilmog), and IBM VP Brianna Frank, who shares insights from Red Hat Summit. Together, they explore how AI is reshaping cybersecurity, enterprise consulting, and software design.

## Key insights
- **Malia Skills Compiler**: IBM Research developed a pipeline that converts natural-language agent skill files (e.g., OpenClaw .mmd files) into structured Python programs, adding safety/security guardrails. This acts like a traditional compiler — keeping authoring in natural language while hardening deployment into deterministic, verifiable code.
- **Skills security is a major unsolved problem**: The current agentic skills ecosystem is chaotic and insecure. Malia addresses prompt injection, tool over-permissioning, versioning chaos, and contradictory instructions by treating skills as compiled, validated programs.
- **Generative computing = best of both worlds**: The vision is to blend classical deterministic computing with LLM calls only where needed (context, composition), drawing on 80+ years of computer science principles like compilers and operating systems.
- **OpenAI's Deployment Company signals a shift**: The consulting/services layer — not the model itself — may be where the real enterprise AI business lives. Anthropic is making similar moves, suggesting model commoditization is accelerating.
- **Consulting will merge with software**: Future enterprise AI delivery will likely blend human consultants with virtual AI workers (agents with verifiable, badged skills), fundamentally changing — not eliminating — consulting jobs.
- **AI-assisted zero-days are already here**: AI has been used to discover vulnerabilities well before the Anthropic Claude Mythos announcement. Open-weight models are already sufficient for file-by-file vulnerability scanning; Mythos's distinction is chaining 30+ exploit steps autonomously.
- **Offense vs. defense is approaching equilibrium**: AI accelerates both attack discovery and patch verification. Faster attacks are also easier to detect. The real policy debate should focus on how to accelerate defensive capabilities faster than offensive ones.
- **Patch management remains the real bottleneck**: Even as AI finds and patches vulnerabilities faster, most organizations cannot deploy patches within 30 days — making "patch apocalypse" management the practical crisis, not zero-days themselves.
- **Enterprise AI adoption is in a scaling phase**: At Red Hat Summit, practitioners are past "should we use AI?" and focused on harder problems: securing AI, model upgrade management, consistent on-prem/cloud architecture, and guardrails.
- **Culture change precedes technology adoption**: Brianna Frank emphasized that AI transformation requires behavioral and cultural shifts first — better documentation, transparency, and workflow changes — before agents can be effectively applied.
- **IBM Red Hat announcements**: IBM launched Red Hat OpenShift Virtualization (fully managed) and a standalone Red Hat AI Inference Service, aimed at eliminating GPU hoarding and over-provisioning battles within enterprises.
- **Design is more critical than ever**: As AI raises user expectations for seamless, intelligent interfaces, proper UX and data/metadata design become essential to unlocking AI's value — visual polish alone is insufficient.