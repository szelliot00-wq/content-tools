# AI Agent Architecture: Where Does Your Agent Actually Run?

Video ID: `_iTbNy5aOR0`

## Summary
This video breaks down AI agent deployments into four distinct workloads — reasoning, the agent loop, the action plane, and state — each with different resource, security, and scaling requirements. It's aimed at production engineers and argues that treating an agent as a single monolithic workload leads to poor architectural decisions. The talk walks through how each plane should be deployed on a Kubernetes cluster and closes with four diagnostic questions to evaluate any agent deployment.

## Key insights
- **An agent is four workloads, not one:** reasoning (model inference), the agent loop (lightweight orchestration code), the action plane (tool calls that touch the world), and state (memory/checkpointing).
- **Never co-schedule the agent loop on GPU nodes.** The loop is essentially a sleeping while-loop waiting on network I/O — it belongs on cheap CPU nodes scaled horizontally with HPA.
- **The action plane is the security-critical layer.** This is where model output has real side effects (HTTP calls, DB writes, shell commands). It should run in ephemeral, sandboxed pods with a default-deny network policy and a narrowly scoped service account — never inheriting the loop's credentials.
- **Externalizing state is the most important architectural fork.** An agent that stores state in-process loses everything on pod restart. Checkpointing to Postgres or Redis lets pods crash, reschedule, or scale to zero and resume seamlessly.
- **Scale each plane on its own signal:** KV cache pressure (reasoning), request concurrency (loop), job queue depth (action), and storage I/O (state). One autoscaler for all four will be wrong for at least three.
- **Make tool calls idempotent and checkpoint before every tool call**, not just after — a resumed loop may retry the call it died on mid-execution.
- **Keep the loop boring and stateless.** The more logic pushed into the loop container, the harder it becomes to make it disposable and replaceable.
- **Four diagnostic questions for any agent deployment:** Where do the weights live? Where does the loop run? What can the tools touch, and as whom? Where does state survive after a restart?