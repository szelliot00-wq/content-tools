# Shrimple – A Simpler, Nicer Markdown

Source: https://qount25.dev/Shrimple/

## Summary
Shrimple is a Markdown alternative written in Go that prioritizes readability in both raw text and rendered HTML form. It replaces inline URLs with footnote-style references, uses indentation-based code blocks with optional syntax highlighting, and introduces a "parse & render dictionary" system for applying consistent formatting without cluttering source documents. It also includes a static site generator capable of building navigable, menu-linked HTML documentation from a directory of Shrimple files.

## Key takeaways
- **Footnote-style links**: URLs are kept out of the document body and referenced by number, keeping source text readable.
- **Code blocks use 6-space indentation** rather than backtick fences, with optional language hints for Prism.js syntax highlighting.
- **Only two header levels** (h1 via `===`, h2 via `---`), keeping document structure simple.
- **Parse & render dictionaries** let you define words or phrases to highlight/style globally without adding any markup to the source text.
- **Built-in static site generator** converts a directory of Shrimple files into a full HTML site with menus and prev/next navigation, no server required.
- **Lists support both bullet and numbered formats**, with numbered items automatically normalized to be consecutive even if source numbers are out of order.
- **Requires Go** to compile; usage is straightforward via CLI flags (`-s`, `-w`, `-g`, `-n`, `-m`).