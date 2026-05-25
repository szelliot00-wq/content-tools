# Jira Is Turing-Complete

Source: https://seriot.ch/computation/jira.html

## Summary
The article by Nicolas Seriot demonstrates that Jira, the project management tool, is Turing-complete by mapping it to a Minsky register machine. The author shows that Jira's automation rules, issue types, and status transitions can model arbitrary computation. As a proof of concept, he implements addition and even Fibonacci number generation using only native Jira features.

## Key takeaways
- **Jira is Turing-complete**: Its built-in features are expressive enough to simulate any computable function.
- **Minsky register machine as the model**: Registers map to counts of linked issue types (Bugs, Tasks), the program counter maps to an Epic's status, and instructions map to Automation rules.
- **Automation rules drive execution**: JQL-conditioned rules act as the dispatch table, with status transitions serving as the clock/control flow.
- **Addition is implementable**: By deleting Bug-type issues one at a time and transitioning Epic statuses, basic arithmetic can be encoded directly in Jira.
- **Fibonacci in three states**: The Fibonacci sequence can be computed using only three Epic statuses and issue type reassignment (e.g., Bug → Story → Task).
- **Practical implication**: Any sufficiently flexible workflow/automation system with conditional logic and mutable state risks being Turing-complete — a humorous but genuine observation about over-engineered tooling.