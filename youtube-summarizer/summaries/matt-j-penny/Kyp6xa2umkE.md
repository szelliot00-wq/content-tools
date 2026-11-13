# The EASIEST Way To Create AI Influencers Videos (Step-by-Step)

Video ID: `Kyp6xa2umkE`

## Summary
This video is a step-by-step tutorial on creating AI-generated influencer characters and inserting them into videos using the Higsfield platform. The presenter demonstrates a three-step framework: generate a base character image, create a multi-angle character sheet, then produce videos featuring that character. The video uses a "biker granny" concept as a worked example throughout. It is most relevant to content creators, marketers, and social media managers looking to build viral AI character accounts without any camera, acting, or technical video production experience.

## Key insights
- **Quirky contradiction characters perform best**: Viral AI characters tend to be "offputting" in an interesting way — a contradiction (someone who looks like they should be doing one thing but is doing another). The example used is an elderly granny dressed as a biker gang member.
- **Use cheaper image models for iteration**: GPT Image 2.5 Flare is recommended for the initial character design phase because it's fast and low-cost, allowing rapid tweaking without wasting credits.
- **Switch to the premium model for the character sheet**: GPT Image 2.5 Sunburst is slower and more expensive but significantly better at preserving consistent facial features and details — critical because the character sheet feeds the video generator.
- **A character sheet is the key to video consistency**: The character sheet shows the character from multiple angles (full-body front, full-body side, close-up face) on a plain background. Feeding this to the video model ensures the character looks right at any camera distance or angle.
- **Reference the character sheet explicitly in your video prompt**: In Kling/CogVideoX (Cance 2.5), you must use `@image1` syntax to tell the model which uploaded reference image is the main character.
- **Suppress automatic cuts in your prompt**: Advanced video models now auto-insert cuts; specify "one continuous shot" in the prompt to prevent this.
- **Be highly specific about sound design in prompts**: The presenter includes audio cues (metal bar creaking, boots on gravel, birdsong, distant city traffic) and explicitly excludes music, dialogue, and on-screen text.
- **Video generation settings used**: 7-second duration, 1080p, 16:9 aspect ratio, high bitrate — costs 112 Higsfield credits per generation.
- **Character insertion into existing videos**: Higsfield's "Genjitsu" model can replace a person in an existing video with your AI character. It offers 3 free generations and can work with either Higsfield's built-in viral video bank or user-uploaded videos.
- **Blank prompt works for character swaps**: When inserting your character into an existing video, leaving the prompt blank lets the model infer what to replace automatically.
- **Plan recommendation**: The Higsfield Plus plan is required to access Cance 2.5 and GPT Image 2.5/2.6; a 50% discount is mentioned via the video's affiliate link.

## Use cases
- **Solo content creators** building a faceless AI character account on TikTok, Instagram Reels, or YouTube Shorts without appearing on camera.
- **Social media managers** experimenting with branded mascots or persona-driven content at low cost.
- **Marketers** wanting to produce viral "oddly satisfying" or curiosity-gap content using memorable character archetypes.
- **Entrepreneurs** testing content niches or audience concepts before investing in real production.
- **Anyone reacting to or remixing viral videos** by inserting a consistent AI character into trending formats.
- **Game or fiction worldbuilders** who want a consistent visual identity for a character across multiple short-form video vignettes.

## Patterns & frameworks

**Three-Step AI Character Video Framework**
A repeatable production pipeline:
1. *Character Creation* — Use a fast/cheap image model (Flare) to iteratively design the character through conversational prompting and reference-image attachment.
2. *Character Sheet Generation* — Use a high-quality image model (Sunburst) to produce a multi-angle, high-resolution reference sheet (front, side, close-up) on a neutral background. This is the "source of truth" for the character's appearance.
3. *Video Generation* — Feed the character sheet as a reference into a video model (Cance 2.5), reference it explicitly in the prompt, and describe the scene, action, camera movement, and sound in detail.

**Iterative Prompting with Reference Images**
Rather than writing a single perfect prompt, the presenter chains generations: generate → critique → attach prior output as reference → refine with a delta instruction ("keep everything the same except..."). This avoids full regeneration and preserves features the creator wants to keep.

**Character Consistency via Explicit Attribute Anchoring**
In video prompts, repeat the character's specific visual attributes verbatim (e.g., "white bob, studded vest, tank top, floral skirt, red boots") to prevent the model from drifting across frames. This acts as a constraint list rather than relying on the model to infer consistency from the reference image alone.

**Cheap-to-Expensive Model Progression**
Use lower-cost models for high-iteration early stages and reserve premium models only for final, production-quality outputs. This minimizes credit spend while maintaining output quality where it matters most.