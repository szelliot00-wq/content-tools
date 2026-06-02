# macOS needs its grid back

Source: https://blog.hopefullyuseful.com/blog/macos-needs-its-grid-back/

## Summary
The author reflects on how macOS Leopard's "Spaces" feature (2006) provided an intuitive 3x3 grid of virtual desktops that enabled powerful spatial memory for navigation. When Apple replaced Spaces with Mission Control in 2011, the grid was removed in favor of a single horizontal row, destroying that spatial workflow. Frustrated by years of inadequate alternatives, the author built their own app — GridLion — that overlays a grid navigation model on top of native macOS spaces, and shares the technical and business hurdles encountered along the way.

## Key takeaways
- macOS Leopard's grid-based Spaces (3x3) allowed users to build strong spatial memory, treating virtual desktops like physically distinct workstations
- macOS Lion's Mission Control (2011) removed the grid in favor of a horizontal strip, making spatial navigation effectively impossible
- Third-party alternatives either died out or required bypassing system integrity protection, making them unsustainable
- The author built GridLion by exploiting a trick to skip space-switching animations, then modeling native single-row spaces as a grid — without needing private API writes
- macOS permission flows (Accessibility, Screen Recording) are needlessly complex compared to iOS, creating significant onboarding friction for users
- Apps using private APIs cannot be distributed on the Mac App Store, requiring third-party merchant-of-record services like LemonSqueezy
- LLMs were useful for rapid prototyping but don't inherently produce good UX — human judgment and craftsmanship still matter for quality software
- The author believes passion and care in software development remain valuable even in the age of LLM-generated code