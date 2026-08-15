# IBM’s cloud collab, Meta’s Muse Glimmer & OpenAI’s upcoming Astra model

Video ID: `FVXDXi4es8E`

## Summary
This episode of the *Mixture of Experts* podcast covers three main stories: IBM's new cloud partnership with Together AI and Nvidia to provide B300-generation GPU compute at scale; Meta's release of Muse Glimmer, a 30B parameter on-device open model; and OpenAI's decision to delay its Astra model due to cybersecurity concerns. The panel — Tim Hwang, Chris Hay, Rynne Whitnah, and Volkmar Uhlig — discusses broader themes of AI infrastructure economics, the open vs. closed model debate, and the growing intersection of AI and cybersecurity.

## Key insights
- **IBM is moving AI compute from internal use to public market scale**, partnering with Together AI and Nvidia to offer B300 GPU infrastructure, signaling a shift from AI as a niche tool to industrial-scale computing.
- **Neo-clouds still have a role**, but large hyperscalers are catching up fast. Neo-clouds retain an advantage in agility and faster adoption of new architectures, but traditional clouds are closing the gap.
- **Vertical integration makes economic sense at scale.** Frontier labs designing their own chips and owning infrastructure can undercut a 43% cloud margin (like AWS) once their workloads are large and stable enough to eliminate the need for elasticity.
- **Load shifting and batch processing are how GPU operators smooth out the 3x day/night utilization swing**, with batch jobs backfilling off-peak hours — though data sovereignty rules complicate cross-region shifting for regulated industries.
- **Meta's Muse Glimmer is a genuinely strong small model** — 30B dense parameters, optimized for laptops (M3 Macs at 30–40 tokens/sec), using speculative decoding, efficient context windowing borrowed from Gemini/Gemma, and targeting agentic/tool-calling workloads.
- **On-device AI is driven by privacy and connectivity needs**, particularly for enterprises with regulatory data-sovereignty requirements, not just consumer preference.
- **Model routing will become standard practice**: large models handle advanced reasoning; smaller specialized models handle routine tasks to keep per-token costs manageable.
- **OpenAI's Astra delay is framed as a genuine cybersecurity response**, not just marketing — the panel notes that AI systems are now capable enough to be weaponized, and defenders (enterprises, governments) are structurally slower to adapt than attackers.
- **The open vs. closed model debate has security implications**: closed models create asymmetric access, leaving less-resourced actors unable to defend themselves with equivalent tools. The Hugging Face example (forced to use a Chinese open-weight model for defense) illustrates the risk of closed-model gatekeeping.
- **Open models are exerting real pricing pressure on closed providers**, with API token prices dropping as open-weight model quality has risen — a dynamic the panel sees as healthy and likely to continue.
- **The panel's prediction**: open-weight models will eventually surpass closed models in capability — it's a matter of when, not if.