# Why AI Agents Break Zero Trust at the Last Mile

Video ID: `SbrEk_tXZaE`

## Summary
The video examines the "agentic last mile" problem: the security gap that emerges when AI agents connect to legacy enterprise backend systems that were never designed for agentic workflows. As identity, context, intent, and delegation signals are lost at this boundary, Zero Trust principles break down and systems become vulnerable to rogue agents and tool chaining attacks. The presenter proposes a vault-based architecture with ABAC/PBAC policies, short-lived credentials, and telemetry feedback loops to bridge the new agentic world with legacy infrastructure.

## Key insights
- **The last mile analogy**: Just as ISPs struggled to deliver high-speed internet over old home wiring, AI agents struggle to integrate with enterprise systems built long before agentic computing existed.
- **Identity is lost at the boundary**: A verified user's identity propagates cleanly through the agent layer but disappears when legacy systems rely on shared API keys or application-level credentials that carry no user context.
- **Three critical signals are dropped**: Intent (what the user wanted to do), context (the operating environment), and delegation (an agent acting on a user's behalf) are all invisible to backend systems under traditional integration patterns.
- **Zero Trust breaks at the last mile**: Without those signals, backends cannot enforce least-privilege access, enabling rogue agents to impersonate legitimate ones and chain tool calls across systems unchecked.
- **Vault as a bridging layer**: Inserting a secrets/credential vault between agents and backend systems lets you re-attach identity, evaluate ABAC/PBAC policies, and issue short-lived, rotated credentials instead of long-lived API keys.
- **Short-lived credentials reduce blast radius**: Swapping in ephemeral credentials per request means a compromised credential expires quickly and limits lateral movement.
- **Telemetry closes the feedback loop**: Collecting behavioral telemetry from agent interactions feeds back into policies, allowing automatic privilege narrowing or access denial based on observed anomalies.
- **Recommended stack**: Attribute-Based Access Control (ABAC) + Policy-Based Access Control (PBAC) + a credential vault + telemetry pipeline is the proposed four-part solution to the last mile problem.