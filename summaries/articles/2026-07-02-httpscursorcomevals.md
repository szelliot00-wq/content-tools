# CursorBench 3.1

Source: https://cursor.com/evals

## Summary
CursorBench 3.1 is Cursor's benchmark for evaluating AI coding agents on ambiguous, multi-file tasks drawn from real Cursor sessions. The benchmark ranks 36 model configurations across score, cost per task, tokens per task, and steps per task. Fable 5 dominates the top rankings, while the results reveal significant tradeoffs between performance and cost across all model families.

## Key takeaways
- **Fable 5 leads overall**: The top 4 spots all belong to Fable 5 variants (Max: 72.9%, Extra High: 72.0%, High: 70.6%, Medium: 69.8%), making it the highest-performing model family on this benchmark.
- **Composer 2.5 is the best value**: At only $0.55/task and a score of 63.2% (rank 9), it offers by far the best cost-efficiency of any model — roughly 30x cheaper than Fable 5 Max for a modest score reduction.
- **GPT-5.5 is competitive and affordable**: GPT-5.5 Extra High scores 64.3% at $4.37/task, outperforming much more expensive options like Opus 4.8 Max ($7.59/task, 63.8%).
- **Higher spend generally improves scores, but with diminishing returns**: Within each model family, increasing the budget tier raises scores, but the gains shrink at the top end.
- **Gemini 3.5 Flash and Kimi underperform**: At similar price points, these models score notably lower (49.8% and 52.7% respectively) compared to GPT-5.5 or Opus 4.8 variants.
- **Token usage varies wildly**: Sonnet 5 Max uses 93,485 tokens/task despite ranking 13th, while GPT-5.5 Low uses only 4,923 tokens/task — efficiency is not correlated with score.