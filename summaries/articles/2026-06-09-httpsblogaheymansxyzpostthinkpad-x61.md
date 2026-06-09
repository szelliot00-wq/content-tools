# Porting the ThinkPad X61 to Coreboot

Source: https://blog.aheymans.xyz/post/thinkpad_x61/

## Summary
A coreboot developer documents their process of porting the ThinkPad X61 (GM965/ICH8 platform) to coreboot using AI-assisted reverse engineering, since no leaked hardware documentation exists. Despite initial hopes that LLMs could automate the work ("vibe reverse engineering"), the port required extensive expert hand-holding and subsequent review by a seasoned coreboot contributor to fix numerous bugs before it could be upstreamed.

## Key takeaways
- LLMs (Claude Opus 4.6) significantly accelerated reverse engineering but could not replace deep domain expertise — the author needed prior knowledge of adjacent platforms (X60, X200) to steer the model correctly.
- The AI-generated code had real problems: hallucinated register names, wrong register access sizes, incorrect bitfield meanings, and timing tables indexed backwards — bugs that only a human expert reviewer (Angel Pons) caught.
- Traditional firmware dumping (PCI config space, ACPI tables, EC RAM, HDA codecs) before starting reverse engineering provided invaluable reference data for debugging.
- The author found at least 3 versions of raminit in the vendor BIOS image, consistent with Lenovo's documented A/B recovery layout where the top 64K of flash is write-protected.
- "Vibe reverse engineering" produces code that works on the developer's machine but is not upstreamable without a real engineer doing thorough review.
- The project also produced a libgfxinit port for GM965 graphics and an early port to the `fstart` firmware framework.
- Tooling friction (clang-format conflicts between the LLM agent, Emacs, and coreboot conventions) was more frustrating than the LLM limitations themselves.