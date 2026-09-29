# Show HN: Pac-Bench – How well can models one-shot a Pac-Man game?

Source: https://jonclegg.github.io/pacman-bakeoff/

## Summary
Pac-Bench is a benchmark that tests how well AI models can one-shot implement a functional Pac-Man game from a short prompt. Models are scored out of 100 and run through various AI coding tools (Claude Code, Codex, Grok Build, Cursor Cloud, etc.). The leaderboard shows a wide range of results, with top performers scoring in the 90s and the weakest barely breaking single digits.

## Key takeaways
- Claude models dominate the top spots: claude-opus-5-5 via Claude Code scored highest at 99/100, with claude-fable-5-1 (96) and claude-sonnet-5.5 (95) close behind.
- Grok and GPT models are competitive mid-tier performers, with grok-4.7 at 94 and gpt-5.6-sol (Codex) at 90.
- There is a steep performance cliff — scores drop sharply below rank ~10, with many models scoring under 40.
- The "high effort" flag correlates with better scores across most providers, suggesting extended thinking/reasoning modes matter for this task.
- Gemini models (via Antigravity) underperformed relative to their tier, scoring 38 and 17.
- Code size varied significantly (3.6 KB to 16.7 KB), with no clear correlation between output size and score.
- The benchmark uses a single short prompt with no follow-up ("one-shot"), making it a test of a model's ability to produce complete, working game code in one attempt.