# Avian Visitors

Source: https://theodore.net/projects/AvianVisitors/

## Summary
Teddy Warner built "Avian Visitors," a bird detection station using a Raspberry Pi and USB microphone mounted on an apartment balcony. It forks BirdNET-Pi to handle audio capture and species identification via Cornell's BirdNET acoustic classifier, overlaid with a kachō-e (Japanese woodblock print) style collage UI. The project went viral on Twitter, prompting a writeup for others to replicate it for roughly $80 in hardware.

## Key takeaways
- **Hardware is minimal and cheap**: A Raspberry Pi (4B/5/Zero 2W), 32GB microSD, USB lavalier mic, and power supply totals ~$80.
- **Setup is a single curl command**: After flashing Raspberry Pi OS Lite and SSHing in, one installer script handles everything (BirdNET-Pi, the overlay, Caddy web server) in 20-40 minutes.
- **Illustrations are AI-generated in kachō-e style**: 450 species illustrations were pre-generated using Gemini's `gemini-2.5-flash-image` model (~3-5% had anatomical defects requiring manual culling).
- **Collage layout uses a smart packing algorithm**: Tiles are sized proportionally to detection frequency using viewport-normalized area budgets (not naive clamping), packed via a center-out spiral with pixel-mask collision detection.
- **Real-time updates**: The frontend polls every 30 seconds; the full re-pack of ~10 species takes <20ms, making transitions seamless.
- **Optional enhancements**: A Gemini API key enables illustration restyling; an eBird API key filters species to your geographic region, reducing rendered species from ~3,000 globally to locally relevant ones.