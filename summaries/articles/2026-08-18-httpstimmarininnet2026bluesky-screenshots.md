# How Bluesky draws its logo on screenshots

Source: https://timmarinin.net/2026/bluesky-screenshots/

## Summary
The article investigates how Bluesky automatically stamps its logo onto screenshots taken within the app. The author noticed the logo appearing in the top-right corner of post screenshots and traced the implementation to a file literally named `GrowthHack.tsx`, authored by a developer called `mozzius`. The feature uses a package called `expo-privacy-sensitive` to overlay the logo, and the article notes that Signal does something analogous to protect its "secret" chats from being easily screenshotted without context.

## Key takeaways
- Bluesky intentionally overlays its logo on in-app screenshots as a viral growth mechanism, ensuring brand visibility when posts are shared externally.
- The feature lives in a file explicitly named `GrowthHack.tsx`, making the intent transparent in the codebase.
- The implementation relies on `expo-privacy-sensitive`, a React Native/Expo package that can control what appears in screenshots.
- This pattern — watermarking screenshots at the OS/framework level — is not unique to Bluesky; Signal uses a similar mechanism to obscure sensitive content in screenshots.
- It's a low-effort, high-reach marketing tactic: every shared screenshot becomes free advertising without requiring any action from the user.