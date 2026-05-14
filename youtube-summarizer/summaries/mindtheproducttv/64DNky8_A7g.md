# Why the best public-sector PMs delete systems instead of building them- Ayushi Roy

Video ID: `64DNky8_A7g`

## Summary
This interview features Aayushi Roy, Chief Program Officer at New America's New Practice Lab and lecturer at Harvard Kennedy School, discussing the unique challenges and approaches required for effective product management in the public sector. The core argument is that private-sector product frameworks do not translate directly to government work, and that successful public-sector PMs must think in terms of full service delivery, policy design, and — critically — "unbuilding" legacy systems rather than defaulting to building new ones. The conversation covers real examples including a text-based 911 alternative, IRS Direct File, CHIP healthcare systems, childcare vouchers, and FAFSA simplification. It is most relevant to product managers, technologists, and policy professionals working in or transitioning to government or civic tech roles.

---

## Key insights

- **Private-sector product practices don't directly transfer to government.** The assumption that you can "transliterate" private-sector PM frameworks into the public sector is flawed — it took years and a winding road for this to become more widely understood.

- **Public-sector PMs cannot choose their customer base.** Unlike private companies that target a specific market segment, government must serve everyone, including the fringes. Success is measured by reach and improved outcomes across the full public, not ROI.

- **There is no product marketing in government — demand already exists.** People are already struggling to access food stamps, tax credits, healthcare, and other services they are owed. The job is to lower barriers, not generate demand.

- **Build for the lowest common digital denominator first.** Aayushi describes building a rental assistance app on MacBooks and iPhones, then discovering that unhoused users in Oakland had $20 flip phones and couldn't use it at all. The lesson: test on the cheapest, most accessible devices your users actually have — like library computers or budget smartphones.

- **Unbuilding is often more valuable than building.** When brought in to build a 15th system for CHIP (Children's Health Insurance Program), Aayushi's team discovered 14 existing systems serving the same function, each with its own vendor contract, budget line item, and reporting burden on state departments. Instead of adding a new system, she proposed removing 10 — streamlining workflows, reducing costs, and achieving the actual goal more effectively.

- **The product is the easiest part of the job in government.** The harder challenges are: creating executive and legislative buy-in, navigating budgets and "colors of money," managing legacy technical debt, handling media and oversight, working with general counsel, and managing both analog and digital workflows simultaneously.

- **Thin slicing in government requires enabling safe failure in public.** Using IRS Direct File as an example, the team first rolled out to IRS employees internally to build agency-wide support, then rolled out by complexity of tax scenario (rather than household income), allowing people from all tax brackets to participate and generate broad public support — while creating a safe environment for iterative learning under congressional scrutiny.

- **Technology cannot fix upstream policy problems.** Implementation does not compensate for poor policy design. The childcare voucher example in Illinois illustrates this: there is no waitlist by policy, so modernizing the application form just funnels more demand into a broken system without fixing it.

- **Design problems vs. engineering problems.** Policy makers often frame design problems (where the solution is unknown) as engineering problems (where the outcome is clearly defined and can be reverse-engineered). This leads to prescriptive, compliance-driven builds rather than user-centered ones. Example: designing a cordless mouse is a design problem; ensuring a laptop hinge withstands 5,000 open/close cycles is an engineering problem.

- **FAFSA Simplification Act as a cautionary tale.** Well-intentioned policy to simplify college financial aid applications by linking the Department of Education to IRS tax data inadvertently created massive security requirements for cross-agency data sharing, separate "contributor workflows" for students and multiple parents (including joint custody scenarios), years of delays, and nearly prevented FAFSA from going out at all one year — a case study in the gap between policy design and implementation reality.

- **Non-traditional PM backgrounds can be an advantage in government.** Aayushi values hiring people who don't come purely from software delivery backgrounds, because the service, policy, and change management dimensions of the role are often more important than coding skills.

- **AI tooling helps but doesn't solve the core structural problem.** While AI enables faster prototyping and allows policy makers to "play with their words before the ink dries," the real fix requires a genuine feedback loop between policy designers and policy implementers — which requires cross-disciplinary respect, awareness, and bilingual fluency between policy and product.

- **A key interview question for PMs:** "What's something you built that you wish you never had?" — used to identify candidates who understand the value of restraint and simplification, not just delivery.

- **Aayushi's origin story:** She built a text-based alternative to 911 for campus safety (addressing gender-based violence and Title IX issues) with two friends at a WeWork in NYC. In 8 months it was deployed to 800,000 students across 13 universities. This led directly to a role building a 311 system for the city of Oakland.

- **Scale and motivation:** Aayushi is a child of immigrants with a refugee background and views her work as giving back — she has served under three US presidents and emphasizes that the population living below the federal poverty line is often "untouched no matter who's in seat."

---

## Use cases

- **Product managers transitioning from private to public sector** who need to recalibrate their assumptions about customers, demand, success metrics, and the role of marketing.
- **Civic technologists and digital government teams** deciding whether to build new systems or audit and reduce existing ones before scoping new work.
- **Policy makers and legislators** who need to understand the difference between design problems and engineering problems before writing prescriptive policy mandates.
- **Government agencies managing legacy system sprawl** — such as situations where 10–15 redundant systems serve the same function with separate vendor contracts and reporting burdens.
- **Product teams working on social safety net programs** (childcare subsidies, healthcare, tax filing, financial assistance) where application modernization alone will not fix a broken upstream policy or funnel.
- **Digital transformation leads in health and human services agencies** who need to align technical delivery with policy change management.
- **Academic and training programs** preparing the next generation of technologists and policy professionals to work across disciplines.
- **Teams evaluating whether to build, buy, or eliminate** — especially when discovery reveals duplication, technical debt, or policy constraints that make new builds counterproductive.
- **Anyone building for low-income or marginalized populations** who must design for accessibility, low-cost devices, and minimum viable digital access rather than premium user environments.

---

## Patterns & frameworks

**1. "Unbuilding" as a product strategy**
The deliberate identification and removal of redundant or counterproductive systems rather than adding new ones. Applied at CHIP by discovering 14 parallel systems and proposing to remove 10 instead of building a 15th. Works by starting with a discovery phase that maps the full existing system landscape before scoping any build.

**2. The Curb Cut Effect**
A design principle where building for the most marginalized or underserved user first creates solutions that work better for everyone. Contrasted with private-sector practice of starting with early adopters and mainstream customers. In government, the "edge case" is the primary case.

**3. Design Problem vs. Engineering Problem Framework**
Engineering problems have a defined outcome that can be reverse-engineered (hinge stress-testing). Design problems require exploration because the solution is unknown (how to create a cordless mouse). Policy makers who misclassify design problems as engineering problems generate prescriptive mandates that lead to compliance-driven feature factories instead of user-centered solutions.

**4. Safe Failure Architecture in Public Builds**
Creating the conditions for iterative, public-facing failure through: (a) internal rollout to build agency support before public launch, (b) thin slicing by a dimension that allows diverse user exposure (e.g., tax complexity rather than income bracket), and (c) executive sponsorship that protects the product team's ability to learn and iterate under scrutiny. Applied to IRS Direct File.

**5. The Broken Funnel Diagnostic**
Before modernizing an application or interface, map the full service funnel to identify upstream policy or operational constraints that will invalidate the improvement. If a policy prevents waitlists (as in Illinois childcare), a better application UI just delivers more people into a dead end. Fix the policy first, or design around it.

**6. Policy-Product Bilingualism**
A training and hiring philosophy aimed at creating professionals who can fluently operate in both policy design and product delivery. Enables the feedback loop between implementers and policymakers that closes the gap between what is legislated and what can actually be built and used. Aayushi teaches this explicitly at Harvard Kennedy School.

**7. Lowest Common Digital Denominator Testing**
A testing methodology in which products are validated on the cheapest, most accessible devices and connectivity available to the target population — not on developer hardware. Applied after the Oakland rental assistance incident: switched from MacBooks/iPhones to library-grade computers and budget phones from Target as the baseline test environment.