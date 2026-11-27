# Ladybird browser's first downloadable alpha is surprisingly capable

Source: https://arstechnica.com/gadgets/2026/11/ladybirds-new-alpha-shows-theres-life-beyond-chromium/

## Summary
Ladybird, a browser built from scratch over four years by Andreas Kling and contributors, released its first downloadable alpha on November 23, 2026 for macOS and Linux. Unlike Chrome, Edge, Brave, Firefox, and others, Ladybird uses a completely new rendering engine and JavaScript engine — not a fork of any existing project. A reviewer testing it on Fedora Linux found it surprisingly polished for alpha software, handling Google Maps, YouTube, GitHub, and general browsing without major issues.

## Key takeaways
- Ladybird is only the fourth independent browser engine (alongside WebKit, Gecko, and Blink), built entirely from scratch rather than forked from an existing engine.
- The first downloadable alpha supports macOS and Linux; Windows support is planned but not yet available.
- It uses a rolling release model with automatic updates, lowering the barrier from the previous requirement of compiling from source.
- The project is a 501(c)(3) nonprofit with no sponsored search engine deals, meaning no commercial entity influences its roadmap.
- The codebase is migrating from C++ toward Rust, starting with the JavaScript engine.
- Security is explicitly not guaranteed at this stage — the team actively invites security researchers to probe it.
- Despite being alpha software, real-world performance was surprisingly capable: snappy tab switching, fast video downloads, and complex sites like Google Maps rendered correctly.
- A new independent engine has ecosystem value beyond market share — it can expose where the web has drifted toward Chromium-specific behavior rather than published standards.