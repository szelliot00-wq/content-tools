# Jev Ultrafast: A browser agent with a dynamic, indexed action space

Source: https://github.com/browser-use/jev-ultrafast

## Summary
Jev Ultrafast is an open-source browser agent that uses a dynamic, indexed action space to automate web interactions with minimal LLM overhead. Rather than relying on screenshots or site-specific scripts, it builds a numbered element table from each page observation and uses TypeSafe's Jev model to pick an operation and target in a single network round trip — only invoking a small text-generation LLM when typing is needed. The approach achieves a Google Flights search (Zürich → London) in 7.1 seconds including real page loads.

## Key takeaways
- **Dynamic action space**: Each page observation produces a fresh indexed element table (e.g., `[3] combobox Where to? · empty`), and the model picks from only valid operations (`CLICK`, `TYPE_TEXT`, `SELECT`, `SCROLL_UP/DOWN`, `WAIT`, `DONE`, `BLOCKED`) and compatible targets.
- **One round trip per step**: Operation and target heads are resolved in a single TypeSafe API call; a separate small LLM is only called when the chosen operation is `TYPE_TEXT`, minimizing latency.
- **No site-specific scripting**: There are no hardcoded action scripts or prepared field strings — the policy generalizes across tasks and sites from a natural-language goal alone.
- **Safety by design**: Model output never becomes selectors, coordinates, shell commands, or executable JavaScript; text-helper output must parse as a small JSON object before being typed.
- **Speed optimizations**: Tight post-interaction waits (≤200 ms for combobox suggestions, ≤50 ms otherwise), focus emulation to prevent background throttling, and filtering of offscreen content from model context all contribute to fast execution.
- **Small, readable codebase**: The core logic is spread across six files (`agent.py`, `snapshot.js`, `browser.py`, `model.py`, `questions.py`, `demo.py`), making it easy to audit and extend.
- **Flexible text model support**: The text-generation helper supports OpenRouter, Gemini, GLM, and DeepSeek via an OpenAI-compatible interface; the demo uses `inception/mercury-2.5`.