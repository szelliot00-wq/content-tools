# Implementing automatic eSIM installation on Android

Source: https://medium.com/proandroiddev/integration-of-automatic-esim-installation-on-android-6c5f6d7124cb

## Summary
This article details the implementation of automatic eSIM installation on Android, leveraging the `EuiccManager` API to streamline the user experience. It outlines a process where carrier applications can programmatically initiate the download and activation of an eSIM profile using an activation code, significantly reducing manual steps like QR code scanning. While automating the technical download, the process still requires crucial user consent via a system-level prompt for security and control.

## Key takeaways
- Automatic eSIM installation on Android aims to simplify the activation process, moving away from manual QR code scanning or data entry.
- The core technology enabling this is Android's `EuiccManager` API, specifically `downloadSubscriptionFromActivationCode`, which is available since Android 9 (API level 28).
- The process involves a carrier application obtaining an activation code from its backend and then using the `EuiccManager` to initiate the eSIM profile download.
- Crucially, even with an automated download, Android requires explicit user consent via a system UI prompt before an eSIM profile is installed and activated.
- Implementing this feature requires robust error handling for various scenarios, including network issues, invalid activation codes, and system failures, to ensure a smooth user experience.
- This automation significantly enhances the user experience, making eSIM adoption more seamless and user-friendly for mobile operators.