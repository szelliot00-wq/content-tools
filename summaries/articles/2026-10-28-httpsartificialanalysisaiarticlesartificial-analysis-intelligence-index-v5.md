# Artificial Analysis Intelligence Index v5

Source: https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5

## Summary
Artificial Analysis released Intelligence Index v5 on October 27, 2026, their biggest update since v4 launched in January. The update adds two new benchmarks (FrontierCode 2.0 and Terminal-Bench-Science) and upgrades three existing ones, with 60% of the Index now based on private test sets to reduce contamination. Alongside v5, they launched the Progress Index v1, which tracks model capability across a continuous historical scale going back to November 2022.

## Key takeaways
- **Claude Opus 5.5 leads overall** with a score of 58, ahead of GPT-6 Astra (57) and GPT-6.1 Sol (55); Anthropic and OpenAI hold the top five spots.
- **No single model dominates all benchmarks** — six different models lead individual evaluations across the nine tasks.
- **The open-weights gap has widened sharply**, from 3 points in v4.3 to 12 points in v5; the best open-weights model with released weights (DeepSeek V4.1 Flash 1017) scores 32, lower than Claude Haiku 5.5's 36.
- **Cost varies by 13x among top models** — GPT-6.1 Terra is cheapest at $0.96/task while Claude Fable 5.1 costs $13.04/task; GPT-6.1 Sol scores within 4 points of the leader at roughly one-eighth the cost.
- **Effort settings matter more than before** — Claude Opus 5.5 spans 23 points (35 at low effort vs. 58 at max), and effort gaps grew across most top models compared to v4.3.
- **Tasks are more compute-intensive in v5** — median output tokens per task rose by two-thirds (35k → 59k), with agentic evaluations accounting for ~90% of token use despite being only 55% of Index weight.
- **Knowledge is harder than reasoning for top models** — on HLE-Diamond, Claude Opus 5.5 scores 78% on reasoning but only 58% on knowledge questions.