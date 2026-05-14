# Arena AI Model ELO History

Source: https://mayerwin.github.io/AI-Arena-History/

## Summary
A developer built a live dashboard to track historical ELO ratings of flagship AI models from Arena AI, aiming to visualize whether the perception of models degrading after launch is measurable or just subjective. The tool plots one continuous curve per major AI lab, tracking their highest-rated flagship model over time to highlight generational jumps and performance decays. The developer posted on Hacker News seeking community input on a key data gap: finding historical ELO or evaluation datasets based on consumer web UI testing rather than API endpoints.

## Key takeaways
- **Performance decay is measurable:** The tool was built to validate the common user experience that AI models feel less capable weeks after their initial launch.
- **Simplified visualization:** Rather than plotting every model variant, the dashboard shows one curve per major AI lab, making trends clearer and easier to interpret.
- **API benchmarks have limitations:** Arena AI tests API endpoints, which may not reflect the consumer experience, as chat UIs often use heavy system prompts, safety wrappers, or quantized models under load.
- **A data gap exists:** There is a lack of historical ELO or evaluation datasets that specifically test consumer-facing web UIs rather than raw APIs.
- **Open-source project:** The tool is publicly available and the developer is actively seeking community feedback and dataset contributions.