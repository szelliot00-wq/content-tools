# ISponsorBlockTV: SponsorBlock client for all YouTube TV clients

Source: https://github.com/dmunozv04/isponsorblocktv

## Summary
iSponsorBlockTV is a self-hosted, open-source application (by dmunozv04) that connects to YouTube TV clients and automatically skips sponsored segments, intros, and other categorized content using the SponsorBlock API. It also auto-mutes ads and clicks "Skip Ad" as soon as the button appears. The project has ~6.7k stars and 293 forks on GitHub, is written in Python, and can be deployed via Docker.

## Key takeaways
- **Broad device compatibility**: Works on Apple TV, Samsung (Tizen), LG (WebOS), Android TV, Chromecast, Google TV, Roku, Fire TV, Nintendo Switch, Xbox, and PlayStation.
- **Self-hosted**: Runs on any computer with internet access to youtube.com — does not need to be on the same local network as the TV after initial setup.
- **Auto-discovery**: Can find devices on the local network automatically, or devices can be paired manually using a YouTube TV code from the app's settings.
- **Active development**: 664 commits, 23 branches, 30 tags, with recent fixes including a blind SSRF security patch in the DIAL discovery feature.
- **Known limitation**: YouTube recently changed its screen ID code format and is revoking existing codes, so users need to re-pair their devices.
- **Shorts limitation**: YouTube Shorts are not fully supported due to platform-side constraints.
- **Home Assistant integration**: An addon exists for users running Home Assistant.
- **License**: GNU GPLv3.