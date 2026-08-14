# GLM-5.3: Frontier Coding with Emergent Cyber Capabilities

Source: https://z.ai/blog/glm-5.3

## Summary
GLM-5.3 is a new model from Z.ai that achieves significant gains over its predecessor GLM-5.2 purely through scaled post-training — same base model, more environments, more diverse tasks, and more compute. It sets a new open-weights state of the art in coding and demonstrates unexpectedly strong emergent cybersecurity capabilities, including identifying 2,436 real-world vulnerabilities across 269 open-source projects. Model weights will be released publicly in two weeks following safety evaluation.

## Key takeaways
- **Post-training scaling alone drove all gains** — no new base model, just more RL training on more diverse long-horizon environments using the slime framework.
- **Top open-weights coding model**: 50% improvement over GLM-5.2 on Z.ai Code Bench; scores 28.3 on Terminal Bench 3.0 (up from 4.6), and 66.9 on DeepSWE v1.1 (up from 46.2).
- **Emergent cyber capabilities exceeded expectations**: GLM-5.3 more than doubled GLM-5.2 on exploitation benchmarks (ExploitBench: 54.4% vs. 24.4%), reasoning across full multi-stage exploitation chains rather than just identifying isolated flaws.
- **Real-world vulnerability discovery**: Working with Chinese security teams, the model found 2,436 vulnerabilities (1,097 critical/high severity) across 269 projects, with the oldest flaw dating to 1981 — averaging 26.6 years undetected.
- **Token efficiency improved**: GLM-5.3 outperforms GLM-5.2 at every effort level while using fewer output tokens (e.g., 34.5% task completion at ~75K tokens vs. 23.4% at 96K).
- **Thinking is now always-on**: The API no longer supports `thinking.type: "disabled"`; only `low`, `high`, and `max` effort levels are supported, defaulting to `max`.
- **slime training throughput improved 2.3×** via better scheduling and resource-aware heuristics, enabling practical scaling over longer trajectories.