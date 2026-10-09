# You Should Be Using Jev’s Browser Agent, Here’s Why

Video ID: `zac3kEUwIlg`

## Summary
This video explains how Jev (a "judgment model") dramatically accelerates browser agents by replacing slow, expensive AI screenshot-based reasoning with fast, cheap classification decisions. The presenter demonstrates that Jev reduces browser calls by ~90% compared to traditional methods, making tasks that previously took 10–20 minutes feasible in seconds. It covers how Jev works, how to combine it with Claude for reasoning and text generation, and walks through building a working browser agent in ~15–20 minutes using Claude Code. It is most relevant to product managers, developers, and AI builders who want to automate web-based workflows at scale.

---

## Key insights
- **Jev is a judgment/classifier model, not a general LLM.** It takes structured input (text + questions) and returns answers from predefined options with confidence scores — no free-text output. This makes it extremely fast (~1/3 second per decision) and cheap (~$0.04 per million input tokens, output is free).
- **Three question types are supported:** `null` (yes/no), `choice` (pick one from a list), and `score` (a described scale). The right type depends on what you'll do with the answer: yes/no for binary actions, choice for routing, score for ranking/sorting.
- **Jev does not replace Claude.** Jev handles thousands of small, fast classification calls; Claude handles reasoning, writing, and verification. They are complementary.
- **The key trick for browser speed:** Instead of passing screenshots/pixels to an LLM, Playwright or Jev Ultrafast reads all interactable elements on a page, numbers them (e.g., "1: pricing link, 2: free trial button, 3: email input"), and passes that structured list as text into Jev.
- **Each browser step involves two Jev questions in a single call:** (1) What action type? (click / type / scroll / wait / done / blocked), and (2) Which numbered element to act on (or "none")?
- **Confidence thresholds gate execution.** If both answers return above a set threshold (e.g., 0.7), Playwright/Jev Ultrafast executes the action deterministically. Below the threshold, Claude is invoked for reasoning.
- **browseruse.com validated the approach:** Using this method, their Google Flights search dropped from 1,092 browser calls to 101 — roughly 10% of the original, completed in 7 seconds.
- **Claude intervenes at three specific points:** (1) When Jev confidence is too low, (2) When Jev says it's "blocked," and (3) When text input is needed (Jev picks the field; Claude writes the text). Claude also performs final "done" verification since Jev's "done" signal cannot be trusted blindly.
- **Executable scripts (not AI) handle the actual browser actions.** The action set is pre-defined code; Jev just selects which script to run. This makes execution deterministic and fast.
- **The presenter built a working tool in ~20 minutes using Claude Code** with a single prompt, a TypeSafe API key, and a Jev-specific skill that teaches Claude how to format questions correctly for Jev.
- **Known limitations the presenter hit in testing:**
  - Cookie/consent banners fail unless explicitly taught with a yes/no Jev question
  - iFrames and file upload buttons are invisible to Playwright/Jev's element reader
  - False positives: Jev can declare "done" when the goal hasn't actually been achieved (requiring Claude's final verification)
  - Memory is limited to the last 5 actions, so goals must be kept short and chained (one goal per page/form)

---

## Use cases
- **SaaS competitive research:** Automatically screenshot and document competitor pricing pages, onboarding flows, or blog content at scale
- **QA and UX auditing:** Navigate through any web app flow programmatically to document UI states
- **Web scraping workflows:** Retrieve structured data from dynamic pages without brittle selectors
- **Automated form filling / onboarding flows:** Drive sign-up or lead capture forms across multiple sites
- **AI search visibility research (the presenter's own use case):** Auditing competitor blog content to inform SEO/AI recommendation strategy
- **Any task where a human currently manually navigates a website repeatedly** (the video frames this as the core replacement use case)
- **Developers and AI builders** who want to add browser automation to agent pipelines cheaply and at speed
- **Product teams** evaluating competitive products or pricing structures at scale

---

## Patterns & frameworks

**Jev + Claude Collaboration Pattern**
A division-of-labor architecture where Jev handles all fast, cheap classification decisions (thousands per second) and Claude handles reasoning, writing, and verification. Neither model does the other's job. The rule of thumb: if it requires writing or complex judgment, use Claude; if it requires picking from options quickly, use Jev.

**Numbered Element Extraction → Structured Classification Loop**
The core browser agent loop:
1. Playwright/Jev Ultrafast reads all interactable page elements and numbers them
2. The numbered list + goal is passed to Jev with two questions (action type + target element)
3. If confidence ≥ threshold → execute deterministic script; if below → escalate to Claude
4. Page reloads, elements are re-read, loop repeats

**Confidence Threshold Gating**
Set a minimum confidence level (e.g., 0.7) for Jev answers. Actions only execute when both answers (action type AND target element) clear the threshold. Anything below triggers Claude as a fallback reasoner. This creates a fast/cheap default path with a slower/smarter fallback.

**Plan → Classify → Execute → Verify Sequence**
The full agent workflow:
1. **Plan** with Claude (interpret goal, define question set)
2. **Collect** page data (Playwright/Jev Ultrafast)
3. **Classify** with Jev (answer action questions)
4. **Execute** with deterministic scripts
5. **Verify** with Claude (check if goal was actually achieved)
6. Loop back to step 2

**Chained Short Goals Pattern**
Because Jev's memory window is only ~5 recent actions, complex multi-page workflows must be broken into short, single-page goals that chain together sequentially rather than one long open-ended goal.

**Independent Verification for "Done" Signals**
Never trust an AI's self-reported "done" status. Always route the completion claim through an independent model (Claude) that checks the output against the original goal. This is explicitly recommended in the browser-use project's own documentation.