# Astra for Coding: Why Are We Doing This Again?

Source: https://lucumr.pocoo.org/2026/9/7/astra-why/

The content provided is a DOM/accessibility tree of the webpage rather than the full article body — most of the prose is missing. Only section headings and a few sentence fragments are present. Here's what I can extract from those fragments:

## Summary

Armin Ronacher explores using an AI model called Astra for coding tasks, running experiments he describes as a "slop factory." He observes that Astra displays unusual behavior compared to other models — particularly around tool calling — where token-efficiency training for tool calls appears to bleed into actual code generation in unintended ways. The article questions the distinction between disposable, exploratory code and code meant to be committed, and notes a curious phenomenon where sandboxed models independently converge on the same public resources.

## Key takeaways

- Astra appears to compress/golf its tool calls in ways that mirror code, and this behavior sometimes contaminates the actual codebase it produces.
- The author spent 35 hours on a single prompt, suggesting these models can be extremely costly to prompt correctly when left unattended.
- There is a meaningful distinction between *disposable code* (throwaway experiments) and *committed code* — models may not respect that boundary.
- Sandboxed AI models independently finding the same public wikis raises questions about how these models behave in isolation.
- The article implies current AI coding tools may not yet be reliable enough for unattended, long-running tasks.

**Note:** The full article body was not included in the provided content — only headings and partial sentences were available, so this summary is incomplete. For a full summary, please share the complete article text.