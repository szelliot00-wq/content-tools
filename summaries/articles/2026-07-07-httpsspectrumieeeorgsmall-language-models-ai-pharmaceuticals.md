# Small AI Models Gain Traction In places with unreliable networks

Source: https://spectrum.ieee.org/small-language-models-ai-pharmaceuticals

## Summary
Small AI models — compact systems with a few billion parameters or fewer that run locally on phones, drones, or cheap microcontrollers — are gaining ground in regions where large-model infrastructure (data centers, broadband, reliable power) doesn't exist. The article profiles real deployments across Africa, India, Brazil, and Uruguay that use small AI for drug authentication, crop disease detection, malaria surveillance, and cardiac monitoring. Advocates argue this edge-based, task-specific model of AI will ultimately reach more people than today's giant LLMs, though it still depends on basic infrastructure investments to be sustainable long-term.

## Key takeaways
- Only 0.7% of internet users in the world's poorest countries have used ChatGPT, versus ~25% in the most developed nations — large models are effectively inaccessible to most of the world.
- Small AI models (typically a few billion parameters) can run on a phone, Raspberry Pi, or Arduino using just a few watts, eliminating the need for cloud connectivity.
- Real-world deployments include a handheld drug-authentication spectrometer (RxScanner) in Africa, disease-detection drones for Indian cashew farms, malaria mosquito detection, and ECG devices in rural Brazil.
- Small models are built via pruning large models, distillation (training to mimic a larger "teacher"), quantization (reducing bit precision), or training from scratch on small hardware for narrow tasks.
- Hardware trends support the shift: by end of 2026, over 50% of smartphones shipped will be capable of running small AI models, up from ~35% in 2025.
- Open-weight models like Google DeepMind's Gemma 4 and Alibaba's Qwen 3.5 make fine-tuning for domain-specific use cases (e.g., the dairy industry) straightforward.
- The World Bank now actively funds small AI development, including a Rwanda program to put AI-capable devices in low-income households.
- Large models aren't going away — they're still needed to create small models via distillation and pruning — but small AI proponents see the future as millions of specialized edge models rather than a few centralized giants.
- Infrastructure remains the limiting factor: even offline-capable devices need periodic connectivity for updates, and reliable power is essential for battery longevity.