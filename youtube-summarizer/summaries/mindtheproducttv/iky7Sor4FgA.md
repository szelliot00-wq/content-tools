# Claude Can Now Pass Coding Interviews. Now What?

Video ID: `iky7Sor4FgA`

## Summary
This video, hosted by Mike Belceto for Mind the Product, examines what happens to technical hiring now that Claude can pass — and in many cases beat — standard coding interviews. It traces how two Anthropic engineering managers (Felix Reezberg and Tristan Hume) independently discovered their interview frameworks were broken and what each did next. The video argues that the skills being screened for must shift from raw coding ability toward judgment, taste, and business impact — and then draws direct implications for product managers and hiring managers rethinking their own interview loops. It is most relevant to PMs, engineering managers, and anyone involved in technical or product hiring.

---

## Key insights
- Felix Reezberg (Electron co-maintainer at Anthropic) declared coding interviews dead for his team on October 27th, noting that Claude passes them — making them useless as a differentiator between candidates.
- He replaced coding tests with portfolio reviews, specifically looking for small prototypes that demonstrate **taste, empathy, and principled thinking** — qualities that closely mirror the product management role.
- Tristan Hume (performance optimization lead at Anthropic) built a take-home test in late 2023 that over 1,000 candidates took over 18 months. It was designed around real work and AI use was explicitly allowed.
- By May 2025, Claude 3.7 Sonnet was already beating more than half of candidates on Tristan's test. A pre-release Claude Opus 4 produced a better solution than almost all humans within the 4-hour limit.
- A pre-release Opus 4.5 cleared the passing bar in under an hour, got stuck, then — once told what cycle count was achievable — found a trick and matched the best human score (who had also heavily used Claude).
- Tristan explored three paths: ban AI (hard to enforce, misaligned with real work), raise the bar so candidates must beat Claude (encourages just watching Claude work), or redesign around what Claude can't do. He chose the third.
- His new test uses a **tiny, heavily constrained instruction set** far outside training data — Opus 4.5 failed a medium-to-hard version. Crucially, there is no debugger or visualizer: candidates must build their own tools, revealing judgment.
- The tradeoff Tristan explicitly acknowledged: the original test worked because it resembled real work; the new test works because it simulates **novel** work — and the harder you make a test AI-proof, the further it drifts from the actual job.
- At Anthropic, junior technical hires fell from **27% to 9%** of technical hires since early 2025; junior share of technical staff dropped from **21% to 14%**. Code commits per engineer are up **5x** in six months.
- One Anthropic Institute finding: the strategic portion of engineering work shifted from **20% to 90%** of the job — explaining why a React coding exercise stopped predicting team fit.
- Canva now **requires** candidates to use AI tools (Copilot, Cursor, Claude) in interviews. Their finding: strong candidates controlled problem scope and reviewed AI output critically; weak candidates couldn't evaluate what the AI gave them.
- A CoderPad survey of ~650 developers and recruiters found: 34% ban AI completely, 46% allow it in some form, 20% decide case by case.
- LinkedIn renamed its APM program to "Associate Product Builder," removed the resume upload, and now asks for a 60-second video of a product the candidate uses plus answers to six questions.
- Felix's advice to junior engineers: focus on **business impact over backlog**, pick one good idea, build a working prototype over a weekend rather than writing a PRD. He cites Anthony Morris and Alice Ziao, who built a graphical UI for Claude Code over a weekend — the first public version shipped 8 days later.
- Felix's "fresh eyes" argument: newcomers don't know why something is supposedly impossible, so sometimes they try it anyway. Experienced practitioners can be held back by what they already know.
- A polished prototype is now cheap to produce with AI, so demos alone risk becoming a weak signal — they show someone *can* build, but not whether they build the *right* thing, kill wrong ideas, or collaborate effectively.
- Subjective evaluation criteria (taste, judgment) without a scoring rubric introduce bias — you risk hiring whoever sounds most like the interviewer.

---

## Use cases
- **Engineering managers** redesigning technical interview loops to account for AI-assisted candidates.
- **Product managers and APMs** rethinking case study or take-home formats that AI can now answer adequately on its own.
- **Hiring managers at any company** auditing whether their current interview questions still differentiate candidates or just measure chatbot access.
- **Junior engineers and PMs** trying to break into the field — understanding that a well-built, impact-driven prototype now carries more weight than a coding test score or years-of-experience proxy.
- **Senior PMs** who need to stay open to beginner's mind and avoid letting accumulated assumptions block unconventional solutions.
- **Recruiting teams** evaluating whether job postings still reflect what the role actually requires (e.g., listing 5–10 years of experience when what's really wanted is judgment and taste).
- **Companies competing for junior talent** who can treat Anthropic's reduction in junior hiring as a competitive opening.

---

## Patterns & frameworks

**The Audit Interview**
Hand the candidate a piece of flawed AI-generated work and ask them to review it. For engineers: a repo with a confident bug. For PMs: a metrics plan tracking the wrong thing, or a launch plan missing a key approval stakeholder. Evaluate what they catch, what they miss, and how they explain it. Requires a rubric written *in advance* to avoid bias. The video positions this as potentially more revealing in 20 minutes than three traditional case studies.

**The AI-Constraint Treadmill (Tristan Hume's Model)**
A framework for understanding why interview tests have a shrinking shelf life: design a test → AI improves → test is invalidated → redesign further from real work → repeat. The further you push to stay ahead of AI, the less the test resembles actual job tasks. Awareness of this cycle is itself a design constraint for anyone building assessments.

**Novel Work vs. Real Work Test Design**
Tristan's explicit tradeoff: tests that resemble real work are vulnerable to AI; tests insulated from AI simulate novel work but drift from the job. This is a named tension hiring teams must consciously manage rather than assume away.

**The Prototype-as-Signal Framework (Felix Reezberg)**
Replace credentials and coding tests with small prototypes the candidate has built independently. Evaluate along three axes: taste (aesthetic and product judgment), empathy (understanding of users), and principled thinking (reasoning behind decisions). Business impact is the north star — not lines of code or sprint velocity.

**The "Run Your Test Through Claude Cold" Check**
A practical self-audit: take one exercise from your interview loop, submit it to Claude with no coaching, and read the output. Ask yourself honestly: if a candidate submitted this, would I advance them? If yes, the exercise is measuring AI access, not human judgment — and it's time to redesign it.