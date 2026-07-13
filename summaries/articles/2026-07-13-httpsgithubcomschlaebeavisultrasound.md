# Beavis Ultrasound PnP ISA Sound Card Replica

Source: https://github.com/schlae/BeavisUltrasound

## Summary
The Beavis Ultrasound PnP is an open source hardware replica of the classic Gravis Ultrasound PnP ISA sound card, published by GitHub user "schlae" (Tube Time). It stands out from other clones by including the full schematic and reverse-engineered GAL source code. The project is newly created (initial commit only) and has not yet been fabricated and tested, so builders proceed at their own risk.

## Key takeaways
- **Core chip required:** The design centers on the AMD InterWave chip (AM78C201), which handles nearly all sound card functionality.
- **Board specs:** 4-layer PCB, 8.2 x 4.2 inches (208 x 107mm); ENIG edge finger plating is acceptable as a cost-effective alternative to hard gold.
- **Programmable devices:** Three programmable components — a 1MB sample ROM (or substitute 27C800), a 93C66 EEPROM (loaded with the provided `ultrasound_pnp.bin`), and a GAL16V8 (loaded with `gr_gal.jed`) for IDE/CDROM interfacing.
- **EEPROM bit-reversal quirk:** The 93C66 EEPROM stores data with bits reversed 16 bits at a time; a Python script (`pnp_reverse.py`) is included to help with custom configurations.
- **GAL is optional:** The GAL chip is only needed if you want the CDROM IDE port functionality.
- **Component substitutions allowed:** The LM833 op amps can be swapped for JRC5532 or any low-noise ~10MHz op amp rated for +/-8V; ferrite beads can be replaced with 0-ohm resistors.
- **License:** Released under CERN-OHL-P-2.0 (permissive open hardware license).