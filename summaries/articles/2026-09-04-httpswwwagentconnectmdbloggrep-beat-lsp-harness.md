# Grep beats LSP? Why coding agents ignore your fancier tools

Source: https://www.agentconnect.md/blog/grep-beat-lsp-harness/

## Summary
A study comparing grep (lexical search) against LSP-backed semantic navigation tools found that coding agents overwhelmingly preferred grep, using LSP tools only 0–57% of the time depending on task type. The key insight is that tool usefulness for agents isn't about semantic precision alone — it depends on whether the tool returns enough immediately readable context to support the next action. When LSP tools were modified to include inline code context alongside file locations, agent performance improved significantly, narrowing the gap with grep.

## Key takeaways
- Agents rarely used LSP tools even when available: near 0% on localization tasks, and only 45–57% on reference-completeness tasks across three Claude models.
- Grep's advantage was interface design, not accuracy: it returns the matching line inline (e.g. `src/auth.ts:42: return validateToken(token)`), while LSP tools initially returned only a file path and line number, forcing extra read calls.
- LSP with location-only output had a pass@1 of 0.67 and required 15.2 follow-up reads; grep achieved pass@1 of 1.00 with only 4.3 follow-up reads and 40% fewer tokens.
- Adding inline context to LSP output (LSP + inline context) improved pass@1 to 0.83 and cut follow-up reads to 3.2, confirming that output shape — not tool sophistication — drives agent behavior.
- LSP did outperform grep in noisy repos where grep had low precision (e.g. hono TypeScript: +0.246 F1), but at lower token cost — suggesting LSP's value is repo/task-dependent.
- The harness (instructions, tool schemas, result formatting, action loop) is part of the system and must be evaluated together with the model, not in isolation.
- A more semantically correct tool is not automatically better for agents; every result that requires extra steps to interpret adds friction that degrades performance.