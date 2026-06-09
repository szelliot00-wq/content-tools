# How To Use Claude Code Anywhere (VPS & Mobile Setup)

Video ID: `UyT-CNalgy8`

## Summary
This video is a technical tutorial on running Claude Code permanently on a Virtual Private Server (VPS) so it is always accessible, never sleeps, and can be reached from any device including a mobile phone. The presenter argues that hosting Claude Code on a VPS is superior to relying on a local machine or Anthropic's managed cloud offerings because it gives you persistent, evolving file context, full control over your agentic OS, and tool/provider portability. The video walks through every step: SSH key generation, VPS provisioning via als.io, VS Code remote connection, cloning a GitHub repo with context, and setting up Telegram + tmux for mobile access. It is most relevant to developers, AI power users, and small teams who want always-on, autonomous Claude Code workflows with persistent context injection.

## Key insights
- **Why VPS over local machine:** A local laptop sleeps, closes, or loses connection — killing any running Claude Code session. A VPS never turns off, making it the foundation for 24/7 agentic workflows.
- **Why VPS over Anthropic's cloud offerings:** Claude.ai chat lacks a persistent, evolving file system. Anthropic's managed agents (e.g., Claude Code on the web) operate in isolated, resetting sessions — they run a task inside a folder, not an evolving folder structure you own.
- **Provider/tool agnosticism:** Owning a VPS means you can swap Claude Code for Codex or any other tool later. The VPS is just a file structure with an AI overlay — the infrastructure is portable.
- **SSH fundamentals:** SSH (Secure Shell) allows you to remotely operate a server as if you were sitting at its keyboard. It uses a key pair (private key stays on your laptop, public key goes on the server) rather than passwords, making it more secure.
- **Key generation command:** Uses `ssh-keygen -t ed25519 -C "your@email.com"` — ED25519 is described as a modern, secure key type. The public key is safe to share; the private key never leaves your machine.
- **VPS provisioning options:** Two paths are presented — DIY via Hetzner (cheapest, most control, but you manage backups/patches yourself) or managed via als.io (~$17/month), which provisions a Hetzner box but handles backups and monitoring automatically. The video demonstrates als.io.
- **VS Code Remote-SSH extension:** Installing this extension lets VS Code connect to and work inside the VPS as if its folders were local. Once connected, the terminal inside VS Code runs commands on the remote server, not the local machine.
- **Security best practice:** Don't run everything as root. Create a new Linux user, grant it sudo privileges, copy the SSH public key to that user's account, and update the SSH config to use the new username.
- **Cloning context into the VPS:** Install git on the server, then clone a GitHub repo (with a personal access token if private) to bring your agentic OS file structure onto the VPS. This is what provides Claude Code with persistent, rich context.
- **Five requirements for a real mobile workflow:** (1) Secure — only you can access it; (2) Phone-accessible; (3) Dispatch and walk away — task keeps running even if you lose connection; (4) Always on; (5) Access to background context/file system.
- **Why most built-in Anthropic mobile features fall short:** Remote control and Channels both fail the "dispatch and walk away" requirement — if you lose connection or 10 minutes pass without interaction, the session dies and must be restarted.
- **The winning stack: Channels + tmux:** Claude Code Channels (official Anthropic plugin) enables Telegram/Discord as input interfaces. tmux keeps the session alive on the server even after disconnects. Together they satisfy all five mobile workflow requirements.
- **tmux role:** tmux is a terminal multiplexer — it creates persistent server-side sessions that survive disconnects. You start a tmux session (`tmux new-s agents`), then run Claude inside it; closing your laptop does not kill the session.
- **Telegram bot setup:** Create a bot via BotFather (`/newbot`), copy the token, install the official `@claude` Telegram plugin inside Claude Code, configure it with `/telegram configure <token>`, launch Claude with the `--channels` flag, DM the bot to receive a pairing code, then lock the bot down so no new pairing codes are issued.
- **One bot per agent pattern:** For multi-agent setups, create one Telegram bot and one tmux window per agent. Each bot is pointed at a different subfolder of the repo (e.g., `clients/acme`, `content`, `admin`), allowing you to switch "agents" simply by switching Telegram chats.
- **Bun requirement:** The Telegram channel plugin runs on Bun (not Node), so Bun must be installed on the VPS alongside an unzip utility.
- **Auto-approve mode:** Claude can be launched with `--dangerously-skip-permissions` to avoid approval prompts being sent to Telegram for every action, enabling a more autonomous workflow.
- **Cost:** The managed VPS path (als.io on Hetzner) is estimated at ~$17/month. Background scheduled tasks/cron jobs consume API credits, but conversational back-and-forth via Telegram uses the subscription plan, not the API.

## Use cases
- **Solo developers** who want Claude Code to keep running overnight or over weekends without leaving a laptop on.
- **Small teams** where multiple members need shared access to the same file structure and Claude context — everyone SSHes into the same VPS.
- **Agentic OS users** (e.g., users of the presenter's "Agentic OS" community product) who need persistent context injection, skills, memory, and scheduled routines that evolve over time.
- **Mobile-first workflows** where a developer or founder wants to dispatch tasks from a phone (Telegram) and walk away, trusting the server will complete the work.
- **Scheduled/automated workflows** — cron jobs, background agents, and routines that need to run on a fixed schedule regardless of whether any user is active.
- **Multi-agent setups** — teams or power users who want separate Claude instances scoped to different projects or clients, each accessible via a dedicated Telegram chat.
- **Users who want provider flexibility** — anyone who wants to avoid lock-in to Anthropic's hosted infrastructure and retain the ability to switch to Codex or other tools later.
- **Security-conscious users** who want a controlled, single-access environment rather than sharing credentials through a cloud platform.

## Patterns & frameworks

**SSH Key Pair Authentication**
Generate a local private/public key pair using `ssh-keygen -t ed25519`. The public key is uploaded to the VPS provider; the private key stays on your machine. Every connection is authenticated cryptographically without a password. The SSH config file (`~/.ssh/config`) maps a friendly hostname (`myVPS`) to the server IP and username, so future connections are a single `ssh myVPS` command.

**Managed VPS + Context Injection Stack**
The core architectural pattern: rent a managed VPS (als.io over Hetzner), clone your context repo (GitHub) onto it, install Claude Code, and run from a non-root user. The VPS is the "always-on" layer; the cloned repo is the "persistent context" layer; Claude Code is the AI overlay. This pattern is explicitly described as tool-agnostic — the overlay can be swapped.

**Channels + tmux Mobile Dispatch Pattern**
A two-layer solution for mobile access: tmux provides session persistence (survives disconnects at the server level), and Claude Code Channels (Telegram integration) provides the human-facing interface. The combined result satisfies all five mobile workflow requirements: secure, phone-accessible, dispatch-and-walk-away, always-on, and context-aware.

**One Bot Per Agent Pattern**
For multi-agent setups, create one Telegram bot and one tmux window per logical agent. Each agent is scoped to a specific subdirectory of the VPS file system. Switching agents = switching Telegram chats. All agents share a single tmux session (`tmux new-s agents`) with multiple named windows inside it.

**Five-Requirement Mobile Workflow Evaluation Framework**
The presenter uses a five-criteria rubric to evaluate any mobile Claude access solution: (1) Security, (2) Phone accessibility, (3) Dispatch-and-walk-away persistence, (4) Always-on infrastructure, (5) Background context/file system access. Each solution (Remote Control, Channels, SSH+tmux, third-party apps like Cllell) is scored against these criteria, with Channels + tmux emerging as the best fit.