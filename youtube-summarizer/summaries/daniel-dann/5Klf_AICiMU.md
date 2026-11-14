# WPVibe Review (2026) - Can WordPress MCP Let ChatGPT & Claude Work on Your Site?

Video ID: `5Klf_AICiMU`

## Summary
This video by Daniel reviews WPVibe (also called WP Vibe/WP Wipe in the transcript), a WordPress plugin that implements the Model Context Protocol (MCP) to connect AI assistants like ChatGPT and Claude directly to a WordPress site. The plugin acts as a bridge allowing AI tools to retrieve site information and execute tasks — from design tweaks to content creation — without the user opening the WordPress dashboard. Daniel demonstrates live tests with both assistants, showing real changes made and reversed on a site, and highlights the built-in approval mechanism for irreversible actions. The video is most relevant to WordPress site owners, content managers, and non-technical users who want to manage their sites more efficiently using conversational AI.

## Key insights
- **WPVibe bridges WordPress and AI tools** via MCP (Model Context Protocol), enabling assistants like ChatGPT and Claude to interact directly with a WordPress site through natural language prompts.
- **ChatGPT requires reconnection per conversation** — the plugin must be re-added each time a new chat is started, which adds minor friction to repeated use.
- **Claude's connector is account-level**, meaning it persists across conversations once set up — a notable usability advantage over ChatGPT's per-session connection.
- **Both assistants can retrieve live site data**, such as a list of installed plugins with their version numbers, confirming an active, real-time connection to the WordPress backend.
- **Design changes are bidirectional** — both AIs successfully changed the header background color and then reversed it on prompt, demonstrating reliable read-write capability.
- **Claude built a full landing page ("AI Insight Newsletters")** using the site's existing theme colors and elements, saving it as a draft without auto-publishing, so the user retains review control.
- **Image-to-post workflow**: Claude cannot upload files directly from chat, so it opens a dedicated panel for the user to add images. It then moves them to the media library and generates draft posts with corresponding images, correct styling, and category assignments — all without manual editor work.
- **Irreversible actions trigger an approval gate** — permanently deleting a page (as opposed to moving it to trash, which is restorable) caused WPVibe to pause and ask for explicit user confirmation before proceeding. This is a core safety feature.
- **Drafts-first content model**: Pages and posts created by the AI are saved as drafts by default, keeping the user in control of what actually goes live on the site.

## Use cases
- **Solo WordPress site owners** who want to manage content and design without navigating the dashboard repeatedly.
- **Content creators** who want to batch-create posts from images or media files using simple chat prompts.
- **Non-technical users** who find the WordPress editor intimidating and prefer natural language instructions.
- **Freelancers or agencies** managing multiple sites who want to speed up repetitive tasks like page creation or style adjustments.
- **Marketers** who need to quickly spin up landing pages aligned with an existing site theme without designer involvement.
- **Anyone iterating on site design** who wants to test visual changes (e.g., header colors) and easily revert them through conversation.
- **Site administrators** who want a safety net for destructive actions — the approval gate is useful when delegating tasks or working quickly.

## Patterns & frameworks

**MCP Bridge Pattern**
WPVibe implements MCP (Model Context Protocol) as a middleware layer between the AI assistant and WordPress. The AI sends instructions through this bridge, which translates them into WordPress actions. This pattern abstracts the CMS interface entirely, letting users interact with their site through the same chat tool they already use.

**Draft-First Content Creation**
Any content the AI generates — pages, posts — is saved as a draft and never published automatically. This creates a human-in-the-loop review step before anything goes live, balancing AI efficiency with editorial control.

**Reversibility-Gated Approval**
WPVibe categorizes actions by reversibility. Recoverable actions (e.g., moving a page to trash) execute immediately. Irreversible actions (e.g., permanent deletion) are paused and require explicit user confirmation before proceeding. This is a practical risk management pattern for AI-driven automation.

**Iterative Prompt-and-Check Loop**
The demo follows a consistent test pattern: issue a prompt → AI executes → user refreshes the site to verify → issue a reversal prompt → verify again. This confirm-and-revert loop is a simple quality-assurance workflow for AI-assisted site management.