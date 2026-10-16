# Claude + Three.js = Premium 3D Motion Graphics

Video ID: `CCUSpJkAfgU`

## Summary
This video demonstrates how to create premium 3D motion graphics using Claude (Anthropic's AI) and Three.js, a web-based 3D rendering framework. The creator argues this workflow delivers studio-quality results for a fraction of the cost of traditional methods (After Effects, Blender, or AI video models), requiring no coding or design skills. The process works by having Claude write code that renders in a browser, which is then screen-captured at 60fps to produce video frames. It is most relevant to content creators, social media marketers, educators, and business owners who want high-quality motion graphics without a large budget or technical background.

## Key insights
- **No coding or design skills required** — you only need to describe what you want; Claude writes all the code
- **Three.js is the key enabling framework** — a web development library that adds 3D capabilities to what is essentially an animated webpage being screen-recorded
- **Shaders unlock premium effects** — shaders use the GPU to render reflections, glows, and particle effects; explicitly telling Claude to use shaders improves visual quality significantly
- **Opus 5.5 is the recommended model** — the creator tested all major providers and found Opus 5.5 outperforms Sonnet 5.5, GPT-based models, and others for this specific task
- **Cost comparison is dramatic**: creating a 15-second video costs ~$0.74 via API or ~$0.05 with a Claude subscription, vs. ~$1.50 with AI video models like Seedance 2.5
- **Iterative editing is far cheaper** than AI video models — changes with Claude/Three.js cost almost nothing, while re-generating with Seedance 2.5 costs $1.50+ each time
- **37,000 output tokens** were used to generate one of the demo videos at Opus 5.5 pricing
- **Claude subscription holders get ~30x cost reduction** vs. API pricing for the same output
- **400 videos per week** is achievable on the cheapest Claude subscription plan
- **Specificity in prompts matters** — break down each scene, what happens in it, and the timing for each element
- **Prompt tip: role framing** — telling Claude "this is your application to a motion graphics job you really want, create a fantastic showreel" measurably improves output quality
- **Camera movement is essential** for the premium feel — prompting for 3D camera movements that fly between scenes (not just slideshows) adds perceived depth and professionalism
- **Glassmorphism** (frosted glass effect) is one specific visual style that elevates perceived quality
- **Verification loop prompt** — instructing Claude to self-check for overlapping elements, small text, and quality issues before finalizing reduces errors
- **Aspect ratio flexibility** — Claude can produce vertical, square, or horizontal videos for any platform
- **Conceptual explainers are a strong use case** — the creator highlights RAG visualization, LLM gradient descent, and internet routing as examples where 3D animation communicates better than text

## Use cases
- **Social media content creators** wanting professional motion graphics for posts and short-form video
- **Podcast creators** adding visual overlays to clips to boost engagement on social platforms
- **Business owners/consultants** repurposing client video calls into polished social content
- **Educators and technical communicators** explaining complex concepts (e.g., how LLMs work, RAG, networking) through 3D animation
- **Product marketers** creating launch videos or feature announcement graphics
- **Service businesses** producing explainer videos without hiring a design agency
- **Developers or founders** who want branded motion graphics without After Effects or Blender skills
- **Anyone replacing expensive agency work** — previously thousands of dollars, now cents per video

## Patterns & frameworks

**Claude + Three.js pipeline**
Claude generates JavaScript/Three.js code describing a 3D animated scene. That code runs in a headless browser, which is screen-captured at 60fps. The frames are assembled into a video. No video model or image model is involved — it is pure code rendering.

**Scene-by-scene prompt structure**
Break your prompt into discrete scenes with specific descriptions of what appears, what animates, and when. Include timings per scene. This mirrors how a director's brief or storyboard works and gives Claude the structure it needs to write coherent, sequenced code.

**Role-framing prompt technique**
Framing the task as a high-stakes professional showcase ("pretend this is your application to a motion graphics job") improves output quality — a carry-over from earlier prompt engineering practices of assigning expert personas to AI.

**Verification loop**
Instructing Claude to run a self-review pass after generating the code — checking for overlapping text, elements that are too small, and general quality — catches errors before the output is used, acting as a built-in QA step.

**3D camera movement as quality signal**
Rather than treating scenes as flat slides that transition, prompting for a camera that physically flies through a 3D space (between elements, around objects) elevates the entire piece and distinguishes it from standard AI-generated flat motion graphics.

**Shader-based effects layer**
Explicitly requesting shaders unlocks GPU-accelerated visual effects (reflections, particles, glows) that are otherwise not generated by default. A capable model will determine where shaders are appropriate if instructed to use them.