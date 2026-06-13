# Claude Fable 5 & Apple’s NVIDIA deal

Video ID: `aByPOYCEH6I`

## Summary
This episode of *Mixture of Experts* covers Anthropic's release of Claude Fable 5, including its capabilities, controversial silent quality-degradation feature, and unusual availability model. The panel also discusses Apple's WWDC announcement that it will use Nvidia hardware and Google's Gemini model for cloud AI features, effectively walking back its on-device-only privacy pitch. A third segment covers AI models' difficulty detecting sarcasm and what it would take to fix it.

## Key insights
- **Fable 5 is a genuine step change**, particularly for long-horizon coding tasks, spatial reasoning, and deep in-context analysis — panelists consider it meaningfully better than prior models, not just incremental.
- **Anthropic silently degraded responses** for queries it classified as frontier AI research (training pipelines, chip design) without telling users. After public backlash, Anthropic reversed course within ~20 hours and apologized, promising to make restrictions visible rather than covert.
- **Tiered routing is the real architectural story**: Fable routes queries to cheaper/safer models (e.g., Opus 4.8) based on topic. One panelist argues this router — not the model itself — is the most important design decision, and the industry race is shifting from "whose model is smartest" to "whose model can you trust and afford to run."
- **Fable's availability is deliberately unstable**: free on all plans at launch, then pay-per-credit, then eventually restored to subscriptions "when capacity allows" — a structure that reflects Anthropic's push toward profitability ahead of an anticipated IPO.
- **Apple is abandoning its all-on-device AI story**: it will use Nvidia Blackwell GPUs (not Apple Silicon) for hard cloud tasks and Google Gemini's 1.2-trillion-parameter model, because Apple Silicon lacks the high-bandwidth memory (HBM) required for frontier model inference at competitive speed.
- **Nvidia won Apple's cloud AI slot partly on security, not just speed**: Nvidia's confidential computing support (encrypted PCI bus, encrypted on-card data) let Apple maintain its privacy narrative even while offloading to third-party hardware.
- **Apple's three-tier architecture**: easy tasks on-device (Apple small models), medium tasks on Apple's private cloud (Apple Silicon), hard tasks on Google Cloud (Nvidia Blackwell + Gemini). The on-device pitch survives only for simple queries.
- **AI sarcasm detection sits around 60–70% accuracy** on clean examples and degrades further in messy real conversations. Panelists debate whether the bottleneck is text-only training data (needing multimodal signals like tone and facial expression) vs. simply poor training sets (e.g., using *The Golden Girls* as a sarcasm corpus).
- **The true cost of AI is finally becoming visible**: token consumption may be declining as enterprises confront real pricing after years of Silicon Valley-subsidized access. This is forcing rational economic decisions about when to use large vs. small models.