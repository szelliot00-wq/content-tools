# Cracking Windows Open: Porting RADV to Win32

Source: https://www.collabora.com/news-and-blog/news-and-events/cracking-windows-open-porting-radv-to-win32.html

## Summary
Collabora engineers have ported RADV — Mesa's open source Vulkan driver for AMD GPUs — to run natively on Windows, building on earlier feasibility work by Faith Ekstrand. The port works by reverse-engineering the private data structures used in AMD's kernel-mode driver interface (WDDM2), which has no public documentation. The project reached a significant milestone by successfully running Counter-Strike 2 on Windows using the open source driver, though it is not yet conformant or production-ready.

## Key takeaways
- RADV is already the de facto open source Vulkan driver for AMD on Linux; AMD even discontinued their proprietary PAL-based alternative in its favor.
- The Windows port builds on Faith Ekstrand's XDC 2024 proof-of-concept, extending it with hardware flexibility, native Windows support (no WSL required), and dramatically improved stability.
- The core technical hurdle is the undocumented "private driver data" passed in D3DKMT calls between the user-mode driver (UMD) and AMD's proprietary kernel-mode driver (KMD) — reverse-engineered via a custom WDDM2 logging layer.
- Counter-Strike 2 now runs on the port via the `-vulkan` launch argument, marking the first real game running on RADV on Windows.
- The biggest remaining blockers are: (1) the fragile reliance on reverse-engineered private data structures that can change without notice between driver versions, and (2) presentation performance — currently only a slow CPU path is used instead of DXGI swapchains.
- Zero-copy presentation (a potential 3x performance gain for non-GPU-bound apps) would require direct cooperation from AMD and Microsoft.
- The work is Valve-sponsored and available in a public Mesa branch.