# Google Chrome is killing all uBlock Origin bypasses, Edge, Opera to follow

Source: https://www.neowin.net/news/google-chrome-is-killing-all-ublock-origin-bypasses-microsoft-edge-opera-to-follow/

## Summary
Google Chrome is finalizing the removal of Manifest V2 (MV2) extension support, meaning all workarounds that kept uBlock Origin and similar ad blockers running will stop working. The `kExtensionManifestV2Disabled` feature flag has already been removed in Chrome 150, with remaining MV2 bypass options being dropped in Chrome 151. Microsoft Edge and Opera are expected to follow, while Brave and Firefox remain the primary alternatives for users who want full uBlock Origin support.

## Key takeaways
- Chrome 150 removed the `kExtensionManifestV2Disabled` flag; Chrome 151 will remove the remaining MV2 bypass flags (`ExtensionManifestV2Unsupported`, `ExtensionManifestV2Availability`, `AllowLegacyMV2Extensions`).
- The Windows Registry workaround that extended MV2 support will stop working after Chromium 151.
- Google cited technical debt, code complexity, and security vulnerabilities specific to MV2 as reasons for the permanent removal.
- Microsoft Edge began disabling uBlock Origin in February 2026; Opera has signaled it will also drop MV2 support.
- **Brave** and **Firefox** are currently the best alternatives for users who want full uBlock Origin (MV2) support.
- Chrome users who stay can switch to **uBlock Origin Lite** (MV3-based), though it is considered less effective than the original.