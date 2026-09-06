# AMD Based FreeBSD Desktop Reloaded

Source: https://vermaden.wordpress.com/2026/09/06/amd-based-freebsd-desktop-reloaded/

## Summary
A sysadmin details building a compact Mini-ITX FreeBSD desktop using an AMD Ryzen 7 4750GE CPU and Radeon RX 7700 XT GPU in a Silverstone SG13 case. The build required physically modifying the GPU's plastic shroud and expansion bracket to fit the small case. The article covers the full FreeBSD setup including XLibre X11 (as an alternative to Xorg), firmware fixes, and a PKGBASE upgrade to 15.1p3. It closes with a personal anecdote about the author's son building a PC game using AI tools.

## Key takeaways
- The AMD Ryzen 7 4750GE + Radeon RX 7700 XT combo offers ~25% CPU and 40-60% GPU improvement over the previous Ryzen 7 1700 + 5700 XT build, all within a ~10.8L Mini-ITX form factor for ~995 EUR.
- Physical case modding was required: the GPU's plastic fan shroud and expansion slot bracket both needed cutting to fit the Silverstone SG13.
- The author uses XLibre X11 (`x11-drivers/xlibre-xf86-video-amdgpu`) instead of Xorg, citing concerns about Red Hat's influence on X11; installing the Xorg variant of the amdgpu driver would force-remove XLibre.
- A missing `iwmbt-firmware` package caused Bluetooth firmware errors on boot; installing `comms/iwmbt-firmware` via `pkg` resolved it.
- With `amdgpu.ko` loaded, idle power drops to ~39W; the system runs cool (~47°C CPU at idle) but only supports C1 sleep state.
- FreeBSD PKGBASE makes OS upgrades straightforward: `pkg upgrade -r FreeBSD-base` updated 52 base packages from 15.1 to 15.1p3 cleanly.
- The `fwget(8)` command handles most firmware detection automatically, but does not cover all cases (Bluetooth firmware was missed).