# What Is Jev? The AI Model That Doesn't Generate Text

Video ID: `YGgNBcIgI4s`

## Summary
The video introduces Jev, a new AI model from TypeSafe that classifies and scores structured decisions rather than generating text. Inspired by Daniel Kahneman's "System 1" thinking (fast, automatic judgments), Jev returns calibrated probability scores for predefined question types — yes/no, multiple choice, or scaled scores — making it significantly faster and cheaper than LLMs for routing and classification tasks. The video argues that Jev and LLMs are complementary, not competing, technologies.

## Key insights
- **No text generation**: Jev answers by assigning probabilities to a fixed set of options, not by producing tokens sequentially. All answers return simultaneously in a single request.
- **Calibrated probabilities**: Unlike LLMs (which can sound confident even when wrong due to RLHF training), Jev is trained with RLCD (Reinforcement Learning for Calibrated Decisions), rewarding the model when its stated probabilities match real-world accuracy rates.
- **Three question types supported**: null (yes/no), choice (pick one from a list), and score (position on a scale) — covering most structured classification needs.
- **Threshold-based routing**: Because probabilities are calibrated, code can use numeric thresholds to decide whether to automate an action, escalate to a human, or ignore it entirely — and the threshold value gives a rough estimate of the error rate.
- **Speed and cost advantage**: Skipping text generation makes Jev fast and cheap enough to run on high-volume data like every row in a database or every line in a log file — use cases where LLMs are too expensive.
- **Jevons Paradox risk**: The model is named after economist William Stanley Jevons, nodding to the possibility that cheaper, faster judgment calls may dramatically expand the *volume* of AI-driven decisions rather than simply replacing existing ones.
- **Limitations**: Currently text-only, poor at math/counting, and vulnerable to prompt injection hidden in input data.
- **Best used in hybrid workflows**: Jev handles fast classification steps (System 1); LLMs handle slower, open-ended tasks like drafting replies (System 2) — mirroring how Kahneman describes human cognition.