# The end of the AArch64 desktop experiment

Source: https://marcin.juszkiewicz.com.pl/2026/06/26/the-end-of-the-aarch64-desktop-experiment/

## Summary
Marcin Juszkiewicz, a Red Hat ARM developer, spent ~11 months using an Ampere Altra Q80-30 (80-core AArch64) system as his primary desktop and has concluded the experiment. The setup required constant workarounds — including self-built kernels to patch a PCIe erratum — and ultimately collapsed when AMD GPU failures made the system unusable for media and gaming, and a fallback Nvidia GPU couldn't run key Flatpak apps (FreeCAD, OrcaSlicer) on AArch64. He reverted to a 6-core x86-64 Ryzen machine and repurposed the Altra for RISC-V package builds.

## Key takeaways
- **AArch64 desktop use is still not plug-and-play:** The Ampere Altra required custom kernel builds every week to work around a PCIe controller erratum (erratum 82288), making maintenance a significant ongoing burden.
- **Server hardware ≠ desktop hardware:** The ASRock Rack motherboard's QVL doesn't include AMD Radeon cards; getting them to work required extra patches that complicated debugging when things broke.
- **Core count doesn't equal desktop performance:** 80 cores at 3.0 GHz felt slower for typical desktop workloads than 6 cores/12 threads on a Ryzen 5 3600, because single-threaded performance matters more for everyday tasks.
- **Software ecosystem gaps remain a blocker:** Key Flatpak apps like FreeCAD and OrcaSlicer lacked AArch64 builds, making the platform a non-starter for maker/engineering workflows.
- **The hardware excels at parallel server workloads:** The Altra now runs RISC-V package builds where its many-core design is genuinely useful.
- **Another attempt would need a purpose-built platform:** The author rules out repeating this experiment unless a proper AArch64 desktop platform (not repurposed server hardware) becomes available at a reasonable price.