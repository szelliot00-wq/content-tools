# Unkernel: Real Linux kernel, compiled to WebAssembly

Source: https://unkernel.dev

## Summary
Unkernel is a project that compiles a real Linux kernel to WebAssembly, allowing it to run in a browser environment. The interface shown is a web-based OS shell with a terminal console, dock, and menu bar, currently in the process of booting. The system tracks CPU, memory, and network stats, and supports multiple terminal tabs.

## Key takeaways
- A real Linux kernel can be compiled to WebAssembly and run in a browser.
- The compilation process is incremental and visible to the user (shown at 60% in the UI).
- The browser-based environment mimics a desktop OS with a terminal, dock, menu bar, and system status indicators.
- Resource monitoring (CPU, memory, network) is built into the interface.
- The system supports 2048 MiB of kernel memory, suggesting non-trivial compute capability in-browser.