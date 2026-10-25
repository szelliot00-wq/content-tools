# Five Qwen3.8-27B models match Fable 5 Using GVS5H Harness

Source: https://github.com/slee-persis/GVS5H

## Summary
The GVS5H paper introduces a training-free method called "ledger-based zero-shot self-orchestration," where multiple fresh instances of the same model coordinate through a shared filesystem to solve hard coding problems. Tested on 100 hard LiveCodeBench problems across 11 models, the approach enables smaller open-weight models to match or exceed Claude Fable 5's coding performance at a fraction of the cost.

## Key takeaways
- Five orchestrated Qwen3.8-27B instances rise from 66.8% to 92.4% pass@1, matching Claude Fable 5's 90.4% — on a single GPU with open-weight models
- Orchestrated Qwen3.8 Flash Next reaches 93.0% pass@1 (beating Fable 5) at roughly 9% of the cost
- The gains come from decomposition and persistent context: models share a plan, notes, and current solution via a shared filesystem, not from fine-tuning
- Gains are not universal — some models are unchanged or perform worse with orchestration
- The method offers two practical paths: frontier-level accuracy at low cost (API), or slightly exceeding frontier accuracy on self-hostable hardware