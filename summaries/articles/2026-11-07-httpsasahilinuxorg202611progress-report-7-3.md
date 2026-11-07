# Asahi Linux Progress Linux 7.3

Source: https://asahilinux.org/2026/11/progress-report-7-3/

## Summary
This is a progress report from the Asahi Linux project covering developments aligned with Linux 7.3. The report highlights major milestones including the upstreaming of the macaudio and AVD drivers, M3 chip support going generally available, advances in GPU/graphics support, and long-awaited Thunderbolt progress. Additionally, the team is working on enabling x86 Windows games to run outside of a virtual machine on Apple Silicon hardware.

## Key takeaways
- The macaudio driver (covering Apple Silicon audio hardware) is finally ready for upstream submission after extensive ALSA core changes — a ~3,100 line patchset.
- M3 chip support has reached general availability (GA).
- Thunderbolt support, long-delayed after an over-promised timeline, has now appeared on the mailing list.
- Graphics work ("Hello Triangles!") is progressing, with contributors working on GPU rendering capabilities.
- A major development allows x86 Windows games (e.g., GTA IV, Fallout: New Vegas via DXVK/WINE) to run directly on Apple Silicon without the muvm virtual machine, by fixing Linux to support userspace mapping of 4 KiB pages.
- Microphone performance improvements ("Mics, but faster") were also contributed by community members.
- Fedora Asahi Remix continues to be updated to keep pace with upstream changes.