# This Setup Gives Your Team the Same Claude Memory (Steal it)

Video ID: `PzaC81yCJg0`

## Summary
This video addresses a common pain point for teams using Claude: nearly all of Claude's infrastructure (memory, MCP connections, third-party tools) is designed for single users, not teams. The presenter demonstrates an 80/20 solution using three existing tools — Notion, Composio, and Supermemory.ai — to create a shared context layer, shared tool access without key sharing, and a shared memory system accessible to all team members. The core argument is that teams should stop treating AI context as something each individual owns and instead treat it as shared infrastructure. It is most relevant to small-to-medium business teams already using Claude Desktop who want to collaborate on AI workflows without custom engineering.

## Key insights
- **~70% of the presenter's community members are trying to use Claude as a team but almost none have a clean way to do it** — confirming this is a widespread, unsolved problem.
- **Y Combinator lists "team infrastructure for agents" on its Requests for Startups list**, signaling this is a recognized gap that no one has solved well yet.
- **The mental model shift required**: stop treating context as something each person's Claude individually owns; treat it as shared infrastructure everyone plugs into.
- **Three-layer architecture**: (1) Notion for shared documents and permissions, (2) Composio for shared tool access without API key sharing, (3) Supermemory.ai for shared conversational memory.
- **Notion as shared drive**: Each team member connects Claude to Notion via their own MCP login. Claude can only read/write what that user is already permitted to see in Notion, so the existing Notion permission system does all the access control work — no custom permission layer needed.
- **Composio for tool access without key sharing**: A single Composio connector lets each team member authenticate into 1,052+ apps with their own credentials. The API key never leaves the Composio vault. Pricing: free tier includes 20,000 tool calls/month + 3 team members; $29/month for 50,000 calls + unlimited members (pricing changing August 15).
- **Composio's MCP Gateway** enables a rarer scenario: scoping access to a shared login (e.g., a single company LinkedIn or affiliate dashboard) and distributing it as a scoped MCP URL without exposing the underlying key.
- **Supermemory.ai for shared memory**: Uses a shared "container" (called "team OS") that all team members write to and read from. Each member uses their own API key but points to the same container tag, creating one shared brain. Pro plan at $19/month supports team usage.
- **Setup for Supermemory**: Install the plugin via Claude's marketplace from the repo `supermemoryai/claude-supermemory`, run `/project config` to set the API key and container tag, then all teammates repeat the same steps pointing to the same container tag (e.g., `team-OS-demo`).
- **Critical caveat on Supermemory**: The admin account has visibility into all members' memories, including personal ones — a meaningful privacy concern the presenter acknowledges openly.
- **Memory revocation gap**: If you share a Notion document with a user, they use it in a session and Supermemory captures it, then you revoke their Notion access — they still have access to that context through saved memory. The permission revocation does not propagate retroactively into the memory system.
- **No personal vs. shared memory split**: Everything in any session where the plugin is active goes into the shared team container automatically. The workaround is to be deliberate about which project folders you run the plugin in, and to keep client-sensitive work out of those folders.
- **All sessions should run from one shared project folder** to ensure the container tag persists across sessions rather than spinning up new random container tags per session.
- **Alternative tools work with the same logic**: Notion can be swapped for Google Drive or any cloud file system with permissions; Composio can be swapped for another MCP gateway.

## Use cases
- **Small business teams (2–10 people)** wanting to share brand voice, positioning docs, and creative guidelines across everyone's Claude sessions without manual copying.
- **Operations or project teams** where multiple people work on the same client or project and need access to prior decisions and context from each other's Claude conversations.
- **Teams with shared inboxes or accounts** (e.g., a brand Gmail, a company LinkedIn, an affiliate dashboard) that need Claude to access them without distributing raw credentials.
- **Non-technical business users** who can't or won't manage GitHub-based context syncing but need a shared AI workspace.
- **Admins managing tool access** for a team — Composio's gateway model means one person sets up auth and everyone benefits without ever seeing the API key.
- **Content or marketing teams** that want a shared voice profile, visual identity doc, or editorial guidelines baked into every team member's Claude sessions with controlled edit permissions.
- **Consultancies or agencies** that want to keep client work segmented from shared team memory (with the caveat that you must be deliberate about folder usage to achieve this today).

## Patterns & frameworks

**Shared Context Infrastructure Pattern**
Stop treating AI context (memory, tools, documents) as per-user and instead build it as infrastructure. The mental model: just as teams use a shared drive rather than copying files to each person's machine, teams should use shared context layers that each Claude instance plugs into.

**Three-Layer Team Claude Stack**
1. *Shared Documents Layer* (Notion/Google Drive): Holds persistent team knowledge (brand voice, contacts, SOPs). Permission-controlled at the file level; Claude inherits whatever the logged-in user can see.
2. *Shared Tool Access Layer* (Composio/MCP Gateway): Lets each team member reach the same apps (CRM, Gmail, accounting software) through their own credentials, with the API key staying centralized. Scoped MCP URLs handle edge cases like single-login shared accounts.
3. *Shared Memory Layer* (Supermemory.ai): A single container tag that all team members write to and read from, capturing conversational context and decisions automatically at the end of each session.

**Container Tag Pattern (Supermemory)**
Rather than letting the memory system auto-generate random container IDs per session, explicitly name and pin a container (e.g., `team-OS-demo`). All team members point their API keys at this same container tag. Result: one shared searchable brain. Work from a single shared project folder so the container tag persists across sessions without re-running config.

**Permission Inheritance Pattern**
Rather than building a custom permission system for AI, leverage the permission system already present in your existing tools (Notion, accounting software, Google Drive). Claude inherits read/write access exactly matching what the human user already has — no additional access control layer required.

**80/20 Team AI Setup**
The presenter explicitly frames this as "80% of a team working system for 20% of the work" — a pragmatic heuristic for teams wanting fast results without waiting for purpose-built team AI infrastructure that doesn't yet exist commercially.