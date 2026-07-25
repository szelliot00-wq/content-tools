# UK AISI / Caisi Preliminary Assessment of Kimi K3's Cyber Capabilities

Source: https://www.nist.gov/news-events/news/2026/07/uk-aisi-caisi-preliminary-assessment-kimi-k3s-cyber-capabilities

## Summary
Published July 23, 2026, this NIST/CAISI report details a joint UK AISI and U.S. CAISI evaluation of Moonshot AI's Kimi K3 model (released July 16, 2026) focused on its offensive cyber capabilities. The evaluation used two benchmarks — ExploitBench (exploit development) and The Last Ones (TLO) cyber range — to assess Kimi K3 against other leading U.S. and PRC models. The findings show Kimi K3 surpasses the best open-weight models in cyber capability but falls meaningfully short of top closed-weight U.S. models, while also lacking meaningful safeguards against offensive use.

## Key takeaways
- Kimi K3 outperforms GLM-5.2 (the most cyber-capable open-weight model as of June 2026) on ExploitBench with a 32% score vs. GLM-5.2's 24%.
- Kimi K3 failed to achieve arbitrary code execution (ACE) on any of 41 ExploitBench tasks, while top-tier models averaged ACE on 20/41 — a significant capability gap at the highest-severity level.
- On the TLO cyber range (32-step simulated corporate network attack), Kimi K3 reached step 17 on average vs. 28.5 for leading U.S. models, but completed the full range in 1 of 10 attempts, demonstrating it can autonomously attack small, weakly defended systems.
- TLO completions are no longer exclusive to a small set of models, suggesting broader AI cyber capability proliferation over time.
- Kimi K3's safeguards did not prevent it from attempting exploit development or offensive cyber operations during testing.
- U.S. closed-weight models were tested with safeguards disabled to measure maximum capability; publicly available versions retain those protections.