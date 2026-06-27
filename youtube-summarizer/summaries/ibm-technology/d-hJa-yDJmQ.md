# New AI models, token minimization and IBM’s new sub-1nm chip

Video ID: `d-hJa-yDJmQ`

## Summary
This episode of IBM's "Mixture of Experts" podcast covers four main topics: IBM's sub-1nm chip breakthrough using a new "nano stack" 3D transistor architecture, two new AI models (Sakana's Fugu and Z.ai's GLM 5.2), Google DeepMind's $75M partnership with film studio A24, and the emerging shift from "token maxing" to "token mining" in enterprise AI usage. Guests include IBM researchers and product leaders who provide both technical depth and industry perspective on each topic.

## Key insights

- **IBM's nano stack is a 60-year first in semiconductor history.** For the first time, transistors are stacked vertically (Z-direction) rather than scaled in 2D. Compared to current best-in-class 2nm chips, the sub-1nm technology delivers 50% better performance or 70% power savings, plus 40% more area density — headroom the industry hasn't seen in over a decade.

- **Sakana's Fugu is an orchestration system, not a new model.** It routes requests across existing frontier models rather than introducing novel weights. This produces impressive benchmark numbers but also wider quality variance, since output depends on routing accuracy. The panel sees multi-model orchestration as a product category in itself, not just a model improvement.

- **GLM 5.2 continues the pattern of Chinese open-weights models catching up to proprietary frontier labs.** It rivals Claude Sonnet 4.6 in size and performs strongly on coding benchmarks, but its scale makes it impractical to run locally, raising governance and access questions for enterprise users.

- **Benchmarks for orchestration systems should be read skeptically.** Peak benchmark scores reflect optimal routing conditions; real-world quality has a much wider spread. The analogy offered: robot demos showing the one successful trial out of 100.

- **The DeepMind–A24 deal flips the usual dynamic — Google is paying A24 $75M, not the reverse.** The motivation is that DeepMind needs to learn professional filmmaking workflows, and A24's domain expertise is worth that price. The initial tool is an AI storyboarding assistant, framed deliberately as augmentation rather than replacement.

- **Token maxing is giving way to token efficiency ("token mining").** Companies like Uber and Microsoft have burned through annual AI budgets in months. The more important insight is that token count is a poor proxy for output quality past roughly 5–15 million tokens/day per user; after that point, more tokens correlates with gamification of the metric, not productivity.

- **Not all tokens are equal — local and small models can absorb a large share of workloads cheaply.** Running 30–100B parameter models locally handles research, summarization, and routine coding without touching expensive frontier APIs. True efficiency means routing tasks to the cheapest model that can handle them, not simply using fewer tokens overall.

- **Moore's Law is shifting from lithography scaling to architectural innovation.** The semiconductor industry spent 60+ years shrinking transistors in 2D; nano stack opens a third dimension that IBM believes provides a clear 10–15 year technology roadmap ahead.