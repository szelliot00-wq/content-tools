# IBM MCGA Gate Array Reverse Engineering

Source: https://github.com/schlae/IBM_MCGA

## Summary
This is a GitHub repository by "schlae" documenting the reverse engineering of IBM's MCGA (Multi-Color Graphics Array) chipset, specifically the two gate arrays used in PS/2 models 25 and 30. The project covers both the Memory Controller Gate Array (72X8300) and Video Formatter Gate Array (72X8205), both implemented on Seiko gate array processes. The reverse engineering uncovered undocumented registers and hidden features not described in IBM's official technical reference manuals.

## Key takeaways
- The MCGA chipset consists of two gate arrays: the 72X8300 (memory controller, ~4,342 cells) and 72X8205 (video formatter, ~3,312 cells), both fabricated on a 2µm CMOS Seiko process with 2 metal layers.
- A hidden genlock feature was discovered in the 72X8300: writing bit 3 of register 0x12 enables locking to external HSYNC/VSYNC signals via the video connector pins 11 and 12, a capability IBM documented only as "Reserved = 0."
- The 72X8300 contains factory test "speedup mode" bits that inject clocks into counter bits to make counters run faster during chip testing.
- The 72X8205 has undocumented extended mode register bits (0x1A) that may force 256-color mode or fill the entire display with the border color.
- Hidden manufacturing test registers in the 72X8205 (accessed via registers 0x18/0x19) expose internal data buses (RAMDAC output, VRAM input) and allow software-triggered hard reset.
- The reverse engineering was done by importing die photos into KiCAD, mapping basic cells to schematic footprints, and back-propagating nets — a laborious process due to two metal layers and limited via connection rules.
- A future goal is generating Verilog from the KiCAD netlist, which would enable FPGA reimplementation of the MCGA chipset.