# MkLinux and the pimped-out Apple Workgroup Server 9150

Source: http://oldvcr.blogspot.com/2026/08/mklinux-and-pimped-out-apple-workgroup.html

## Summary
The article chronicles the rebuild and upgrade of an Apple Workgroup Server 9150 at the "Floodgap lab," weaving in a detailed history of Apple's early 1990s server strategy — from the failed Macintosh Office concept through A/UX and the Workgroup Server line. The author then installs MkLinux (Apple's official Mach microkernel-based Linux distribution) alongside Mac OS 8.6 for a dual-boot configuration, and attempts to maximize the machine's hardware for both operating systems with a Sonnet G3 upgrade card, additional RAM, and NuBus video cards.

## Key takeaways
- The WGS 9150 was Apple's only server with no corresponding desktop Mac model, born from the "Green Giant" project as a PowerPC successor to the Quadra 950-based AWS 95.
- A/UX (Apple's System V UNIX) never made the jump to PowerPC, leaving Apple without a credible Unix server OS through most of the mid-1990s — a gap MkLinux was intended to address.
- MkLinux was Apple's first official open-source project, developed in near-secrecy by a small team using the OSF Mach microkernel with Linux running as a single task on top of it.
- Apple disbanded the MkLinux team in 1998 after acquiring NeXT, transferring the project to the community; the Mach kernel code directly influenced early Mac OS X.
- The WGS 9150's brittle "Spindlerplastic" ABS is a common failure point; the author resorted to nylon screws and binder clips to keep the logic board stable after the original plastic clips fractured.
- MkLinux has a hard RAM limit per-configuration — booting with more than ~191MB requires passing the `-m` flag in `lilo.conf` to cap Mach's memory usage, or the kernel hangs.
- A Sonnet G3 PDS upgrade card works in Mac OS 8.6 but causes Mach to hang on boot; the workaround is loading the Sonnet extension as a standard INIT (after the MkLinux Booter) so Linux still runs on the stock 601 CPU.