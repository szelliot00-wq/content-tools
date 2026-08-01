# Ten Ways NAS Is Getting Enshitified

Source: https://nascompares.com/2026/07/31/the-10-ways-nas-is-getting-enshitified/

## Summary
A July 2026 article from NAS Compares argues that the consumer and prosumer NAS market has steadily degraded over the past 18–24 months, shifting from open, modular storage devices toward locked-down appliances. The author identifies ten hardware and software trends driven primarily by cost-cutting and ecosystem lock-in rather than genuine engineering progress. The cumulative effect is higher total cost of ownership, reduced repairability, and diminishing long-term value for buyers.

## Key takeaways
- **Soldered RAM**: x86 NAS units (especially Intel N100/N150 based) increasingly use non-upgradable LPDDR memory, capping expandability and creating single-point-of-failure mainboards.
- **Stagnant networking**: Many mid-range units still ship with 1GbE despite 2.5GbE being mainstream; 10GbE is artificially gated behind expensive proprietary add-ons.
- **Drive lock-in**: Vendors like Synology restrict core features (storage pool creation, health monitoring) unless proprietary branded drives are used, inflating per-TB costs.
- **Fixed low-capacity OS drives**: Soldered eMMC/UFS or small M.2 2230 OS drives create permanent failure points and consume slots that users need for storage.
- **PCIe lane starvation**: Advertised high-speed features (USB4, multi-NVMe slots, 10GbE) are wired to x1/x2 lanes internally, bottlenecking real-world throughput significantly below spec.
- **Recycled hardware**: Manufacturers re-release 2–4 year old silicon under new model numbers with cosmetic changes, masking stale platforms from buyers.
- **Hard drive squeeze**: Consumer HDD supply is compressed at both ends — small drives phased out, large drives diverted to enterprise — leaving a narrow, expensive middle range.
- **DRAM-less SSDs**: HMB-based NVMe drives poorly handle sustained NAS workloads; reduced NAND channel counts further hurt write performance during rebuilds and large ingests.
- **Opaque RAM sourcing**: Rising memory costs push manufacturers toward unverified RAM with proprietary stickers, risking stability for ZFS/Btrfs and containerized workloads.
- **Software homogenization**: New NAS OS platforms are converging on near-identical Debian-based stacks, offering little meaningful differentiation between vendors.
- **Bottom line**: The gap between off-the-shelf NAS and custom DIY builds (TrueNAS, etc.) is widening, pushing power users toward self-assembled systems to preserve control, repairability, and value.