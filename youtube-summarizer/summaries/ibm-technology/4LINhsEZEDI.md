# 4 Types of AI Agent Loops: From Human-Led to Autonomous

Video ID: `4LINhsEZEDI`

## Summary
The video explains four types of AI agent loops that differ in how autonomous they are. All loops share the same core pattern — take a goal, perform an action, observe the result, adjust, and repeat — but vary in who (or what) sets the goal, judges progress, and decides when the task is complete. The progression moves from fully human-controlled to nearly fully autonomous, with each type trading human oversight for scalability.

## Key insights
- **All agentic loops share a common structure:** receive a goal → take an action → observe the outcome → adjust → repeat until done.
- **Interactive loop:** A human sets the goal and judges every iteration. Best for fuzzy tasks without a clear finish line, but doesn't scale for repetitive work.
- **Delegated loop:** A human sets the goal but includes an explicit stopping condition (e.g., "stop when the build turns green"). An AI check handles the judging each cycle; the human only reviews the final result.
- **Scheduled loop:** The human writes the goal once and a schedule (e.g., nightly cron) triggers the loop automatically. Good for work that goes stale over time or needs recurring execution. Human still reviews each result.
- **Event-driven loop:** A real-world event (e.g., a pull request opening) triggers the loop, tailoring the goal to that event. A second "reviewer" agent checks the output instead of a human — humans only see exception cases the reviewer can't resolve. Most autonomous of the four.
- **The key design question is who owns each step:** goal-setting, judging progress, and reviewing results can each be held by a human or delegated to an AI, and the four loop types represent different combinations of those ownership choices.
- **Autonomy trades oversight for scale:** the more you delegate to AI, the less human time it requires — but also the less direct human control over intermediate decisions.