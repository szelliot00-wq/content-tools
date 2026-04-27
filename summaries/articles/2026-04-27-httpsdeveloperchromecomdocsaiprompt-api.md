# The Prompt API

Source: https://developer.chrome.com/docs/ai/prompt-api

## Summary
The Prompt API is a browser-native API developed by Google for Chrome that allows developers to interact with a built-in AI language model (Gemini Nano) directly within the browser, without requiring external API calls or server-side infrastructure. It provides a straightforward interface for sending prompts and receiving AI-generated responses locally on the user's device. The API is part of Chrome's broader initiative to bring AI capabilities natively into the browser environment.

## Key takeaways
- **Browser-native AI:** The Prompt API enables direct access to an on-device language model (Gemini Nano) built into Chrome, eliminating the need for external API dependencies.
- **Privacy benefits:** Since inference runs locally on the user's device, data does not need to be sent to external servers, improving privacy.
- **Simple interface:** The API offers a straightforward way to send prompts and stream or receive responses, lowering the barrier for developers to integrate AI features.
- **Experimental/Origin Trial stage:** The API is still in an experimental phase, available through Chrome's origin trials, meaning it is not yet a stable, widely-deployed feature.
- **Offline capability:** Because the model runs on-device, AI-powered features built with this API can function without an internet connection.
- **Resource considerations:** On-device models have limitations in capability and size compared to cloud-based models, which developers must account for in their applications.