# Headlong: A Microharness for Persistent Agents

Source: https://www.laude.org/updates/headlong-a-microharness-for-persistent-agents

## Summary
Headlong is an open-source agent microharness from the Laude Institute built around "persistent agency" — a design where an agent continuously generates thoughts in a self-guided inner monologue loop rather than waiting to be triggered by external input. The entire harness is implemented in under 10,000 lines of Bash, keeping it small enough for an agent to read and modify itself. The team ran their agent, Audel, in a shared Slack/Telegram environment for weeks, observing it autonomously debug its own code, audit team git branches, and self-correct errors without being asked.

## Key takeaways
- **Persistent vs. reactive agents:** Traditional harnesses freeze between tasks; Headlong agents think continuously, treating human messages as just another observation in an ongoing thought stream.
- **Single shared thought stream:** All users interact with one agent timeline — no per-user sessions — which makes the agent feel more like a team member but also means it cannot keep secrets between users.
- **Bash as the foundation:** Using Bash as the sole tool/framework layer keeps the system composable and self-inspectable; the agent can modify its own harness and has contributed 50+ commits back to the main repo.
- **Exponential-decay memory compaction:** To address poor short-term memory (catastrophic for persistent agents), Headlong keeps the full trajectory in context at progressively summarized resolution, with older entries summarized more aggressively.
- **DAG trajectory format:** Agent history is stored as a directed acyclic graph of JSONL files supporting fork and merge, giving the agent full access to its own history.
- **Real failure modes observed:** The agent repeatedly killed its own service by accident (now guarded against), and a self-built recall process silently failed for weeks due to an environment variable never being set — which the agent eventually diagnosed and fixed on its own.
- **Evaluation gap:** Standard agent evals are poorly suited to measuring persistent agency; the team currently evaluates improvements qualitatively and is seeking better measurement approaches.