# Agentic Trust: Securing AI Interactions with Tokens & Delegation

Video ID: `lUQ2NKkCW_Q`

## Summary
This video explains how to establish and maintain trust and security in agentic AI systems, addressing unique challenges like non-deterministic behavior. It details a typical AI interaction flow and identifies key risks such as credential replay, rogue agents, impersonation, and overpermissioning. The presentation then outlines various security mechanisms, including verifiable agent identities, token delegation, token exchange, scope restriction, and secure credential management for tool access, to ensure reliable and authorized AI interactions.

## Key insights
- A typical agentic AI flow involves users, chat, orchestrators, multiple AI agents, LLMs, and various tools, with an initial user authentication generating a token propagated through the system.
- Key risks include credential replay (e.g., tokens exposed to LLMs or intercepted via man-in-the-middle attacks), rogue agents (spoofing identities), agent impersonation of users, insecure token propagation, and overpermissioning at the tool level.
- To mitigate these, secure communication (TLS/mTLS) and encrypted storage are crucial, and identity information should *not* be passed to LLMs.
- Verifiable agent identities are established by authenticating agents via an identity provider, preventing rogue agents from operating within the system.
- Delegation addresses agent acting on behalf of a user by creating combined tokens (subject=user, actor=agent) validated by the identity provider, ensuring authorized representation.
- Secure token propagation is achieved through token exchanges at each node in the flow, validating and restricting token scopes to enforce least privilege for each interaction.
- The "last mile" of security (AI system accessing tools) is secured by using a vault to manage and issue temporary credentials, preventing AI components from persistently storing sensitive tool access information.