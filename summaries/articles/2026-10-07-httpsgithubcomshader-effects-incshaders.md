# Shaders, WebGPU Components for React, Vue, Svelte, Solid, JavaScript and Framer

Source: https://github.com/shader-effects-inc/shaders

## Summary
Shaders is an open-source library (1.7k stars) that packages WebGPU visual effects as drop-in components for React, Vue, Svelte, Solid, and vanilla JavaScript. It pairs with a visual design editor at shaders.com where you can compose effects, tune props live, and export ready-to-use component code. A CLI syncs designed effects directly into your project, and a Pro tier adds an extended component library plus a Framer plugin.

## Key takeaways
- **Framework-agnostic components**: install via `npm install shaders` and use the same effect API across React, Vue, Svelte, Solid, or plain JS
- **GPU-native rendering**: effects run on WebGPU — a `<Shader>` canvas renders layered child components blended on the GPU
- **200+ pre-built components** with live previews and full prop documentation
- **Visual editor**: design effects at shaders.com with real controls and export the component tree for your chosen framework — free with an account
- **CLI sync**: detects your framework, writes component files locally, and tracks installed effects in a lock file
- **AI-ready**: ships an MCP guide and `llms.txt`/`llms-full.txt` so coding agents can use the same tooling
- **Custom components**: write your own via `defineShader` using either std primitives or raw WGSL shader code
- **MIT licensed**; Pro tier adds extended library, Framer plugin, and additional workflow features