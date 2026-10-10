# OpenAI's always-on agents, 700+ math manuscripts & HackerRank's AI interviewer

Video ID: `IO6Bhs2iNfk`

## Summary
This episode of IBM's *Mixture of Experts* podcast covers four AI news stories: OpenAI's persistent agent "Dots" unveiled at DevDay, an explosion of AI-generated mathematics (722 papers from OpenAI), HackerRank's AI job interviewer "Chakra," and a technical explainer segment on mixture-of-experts architecture and open weights prompted by Reflection AI's new model "Beam."

## Key insights
- **Always-on agents are converging across labs**: OpenAI's Dots and Meta's Muse launched within a week of each other, both featuring cartoonish personas — panelists see this as over-capitalized labs copying each other rather than genuine differentiation.
- **True delegation is still unproven**: The key test for persistent agents like Dots isn't whether they can run tasks, but whether they can do so without repeatedly surfacing for permissions or clarifications — which would undermine the value of delegation entirely.
- **AI math output is creating a human bottleneck**: OpenAI dropping 722 math manuscripts at once raises the question of whether human mathematicians can ever catch up, potentially shifting their role from producers to interpreters of AI-generated proofs.
- **Generating new math questions may matter more than solving old ones**: Terence Tao's challenge to AI — can it ask the *next* great mathematical question, not just answer decades-old ones — remains unanswered by the current wave of papers.
- **AI interviewers can screen for AI proficiency**: Chakra's design (allowing AI use during the coding task, then probing *why* choices were made) reframes the interview as an evaluation of how well a candidate leverages AI, which panelists see as an increasingly valuable signal.
- **Machine bias is more correctable than human bias**: Panelists argued that algorithmic bias in hiring tools is easier to detect and fix than human bias, and that AI interviewers can expand opportunity by removing the bottleneck of finite human interviewer time.
- **Mixture of experts activates only relevant "tabs"**: MoE models partition parameters into specialized expert subnetworks; a learned router activates only the relevant subset per query, making inference faster while keeping total capacity large.
- **Open weight ≠ open source**: Releasing model weights gives others the numbers but not the training data, training code, or compute — full open source means releasing all three, and the distinction matters for reproducibility and trust.