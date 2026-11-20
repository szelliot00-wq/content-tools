# Everyone Ignore These Claude Concepts, But They Change Everything

Video ID: `6VjeXzvpoJo`

## Summary
This video by Simon covers nine underused but still-valid Claude/AI prompting concepts from Anthropic's official documentation that most users overlook or never knew about. The core argument is that many of Anthropic's best practical tips get buried under new feature releases, yet they still produce significant improvements in cost, accuracy, and reliability. The video walks through each tip with concrete examples, numbers, and real-world applications. It is most relevant to power users, prompt engineers, product managers, and anyone building workflows or agents with Claude.

## Key insights
- **Avoid reading large files into Claude's context.** When Claude reads a file directly, it ingests every row — even if you only need a few. Anthropic demonstrated that one job dropped from 150,000 tokens to 2,000 (a 98% reduction) by having Claude write a script to process the file instead, so only the result enters the chat.
- **Use the "write a script" pattern for file processing.** For deterministic tasks (moving files, calculating sums, extracting specific columns), instruct Claude to write a script rather than opening the file. Add a line like "don't open this file, write a script that gives me X" to your prompt.
- **Large files get read twice, doubling cost.** A two-hour meeting transcript (~50,000 tokens) costs ~40 cents at current pricing *per read*. If Claude reads it twice in one workflow, that's 80 cents every single time — which compounds quickly at scale.
- **Break big projects into two phases: setup, then execution.** Anthropic found that asking Claude to do an entire large project in one go causes either context rot (losing track halfway) or premature stopping. Solution: session one creates only a checklist and progress file; every subsequent session does one item, checks it off, and updates the file.
- **Use JSON (not Markdown) for checklists and progress files.** Claude is less likely to silently rewrite, merge, or drop items in a JSON file than in a Markdown list. Anthropic uses a JSON file where each task starts as `false` and Claude can only flip it to `true` after validated completion.
- **Use hooks and deny rules instead of repeated emphasis in Claude.md.** If you keep adding "IMPORTANT" or "ALWAYS" to a Claude.md line and Claude still ignores it, that instruction belongs in a hook or deny rule — Claude cannot bypass those, whereas it can choose to ignore Claude.md lines.
- **Deny rules double as a security layer.** You can add a deny rule on a sensitive folder (e.g., `/exports`) so Claude literally cannot read raw client data, protecting both token usage and data privacy.
- **"Be ambitious" is one of the few prompt phrases that still works.** Most legacy phrases like "think step by step" and "be thorough" no longer have special effects. Anthropic's prompting guide singles out "be ambitious" as still influencing how much Claude builds or expands on a request.
- **Put data before the question in your prompt.** Anthropic found placing all context/data first and the question at the very end improved results by up to 30%, especially with large or multiple documents. Most people do the opposite instinctively.
- **Ask Claude to quote exact lines before answering.** Instructing Claude to cite the specific lines it is drawing from keeps it grounded in the provided data and reduces hallucination.
- **Use examples over instructions for consistent output formatting.** Adding 3–5 examples of what good output looks like improved accuracy from 72% to 90% in Anthropic's own tests — without changing any other instructions.
- **Explicitly permit Claude to say "I don't know."** By default Claude will attempt to answer everything. Adding a phrase like "if you're unsure, say 'I don't have enough information to confidently assess this'" can drastically reduce false or fabricated answers.
- **Research: start broad, then narrow.** Anthropic found ~80% of research quality differences came from effort and breadth. Start with short, broad search terms, survey the landscape, then focus in. This principle applies beyond research — to tool selection, content ideation, supplier shortlisting, etc.

## Use cases
- **Data pipeline automation**: Processing CSVs, spreadsheets, or exports without loading full files into context
- **Long-running agentic projects**: Multi-session tasks like building a codebase, writing a report series, or managing a campaign calendar
- **Sensitive data workflows**: Client data, financial exports, or PII that should never be directly read by the model
- **Weekly recurring analysis**: Any report that runs repeatedly where token costs compound (e.g., weekly spend reports, SEO tracking)
- **Skill/prompt engineering**: Improving layout and format consistency in reusable Claude skills or system prompts
- **Research workflows**: Competitive analysis, supplier selection, content strategy, market research
- **RAG and document Q&A**: Situations where Claude is answering questions over pasted documents or large context blocks
- **Checklist-driven automation**: Any workflow where Claude needs to track multi-step progress across sessions
- **Reducing hallucinations in reporting**: Anywhere factual accuracy matters, such as summarizing contracts, meeting notes, or financial data

## Patterns & frameworks

**Poka-yoke (error-proofing via system design)**
Borrowed from manufacturing. Instead of repeating instructions to prevent a mistake, redesign the system so the mistake cannot occur. In Claude Code: move a rule from Claude.md into a hook or deny rule so Claude has no ability to bypass it, rather than adding emphasis hoping it will comply.

**Script-as-intermediary pattern**
Instead of handing Claude a file to read, ask Claude to write a script that reads the file externally. Only the script's output (the answer) enters the chat context. Reduces token usage by up to 98% for data-heavy tasks.

**Two-phase project structure (Setup → Execute)**
Phase 1: a dedicated session that does no actual work — it only creates a JSON checklist (all tasks set to `false`) and a progress file. Phase 2+: each session picks one task, completes it, validates it, and flips it to `true`. Prevents context rot and premature stopping on large projects.

**JSON-as-guardrail**
Using JSON instead of Markdown for structured task tracking because the model treats JSON as data (less likely to rewrite it) versus Markdown prose (more likely to silently edit). Each task is a boolean that Claude may only change in one direction: false → true, after validation.

**Data-first prompting**
Structuring prompts so all context, documents, and data appear first, with the actual question or instruction at the very end. Supported by a 30% accuracy improvement in Anthropic's internal tests.

**Broad-to-narrow research funnel**
Start with short, general search queries to map the full solution space, then progressively narrow to the most relevant options. Match the number of research agents/searches to the complexity of the question. Applies to research, tool selection, content ideation, and supplier evaluation.

**Example-driven prompting (over rule-driven)**
Instead of adding more instructions to fix output quality, provide 3–5 concrete examples of ideal output. Anthropic's tests showed this alone moved accuracy from 72% to 90%. Reference examples either inline in the skill document or in a linked reference file.