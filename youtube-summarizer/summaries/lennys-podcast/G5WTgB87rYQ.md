# How to ship hardware in the AI era | Caitlin Kalinowski (Apple, Meta, OpenAI)

Video ID: `G5WTgB87rYQ`

## Summary
Caitlin Kalinowski — hardware leader who helped build the MacBook Air, Meta's VR/AR headsets (including Orion), and OpenAI's robotics division — makes the case that physical AI, robotics, and hardware are the next frontier after software intelligence saturates. She argues that VR was a necessary technological stepping stone to robotics, that supply chain independence is now a national security issue, and that humanoid robots are over-hyped relative to purpose-built robots. The conversation covers the full arc of her career across Apple, Meta, and OpenAI, with detailed frameworks for how to build hardware teams and ship physical products. Most relevant to hardware PMs, robotics founders, and anyone building physical AI products.

## Key insights
- **VR as a stepping stone, not a failure**: The SLAM positioning, depth sensing, and spatial computing built for VR are now foundational to robotics. The social barrier (face-covering) limited VR adoption, but the technology investment was not wasted.
- **AR glasses are still the destination**: Orion (Meta's AR prototype) achieves 70-degree binocular field of view — wide enough to feel immersive. The blocker is manufacturing yield on waveguides and microLEDs, not the concept itself.
- **Hardware only gets 4–5 "compiles" total** — ever. Unlike software that can be updated daily, each hardware build iteration takes 3–5 months, and mass production is final. This forces extreme conservatism, tolerance analysis, and front-loaded risk resolution.
- **Define KPIs before you start and barely change them**: If a price target shifts from $300 to $150 mid-program, you've wasted much of the early design work. Quest 2's price reduction required a full product redesign but made it the highest-selling VR headset ever.
- **Do the hardest part first, not the easiest**: The best hardware architects find the pinch points (e.g., cable routing through a hinge) and resolve those before touching anything else. Most engineers do the opposite — they design what they know first.
- **Focus iteration budget on what users touch most**: Trackpad and keyboard on a laptop get far more iteration cycles than internal components. The part of the product with the most user contact must be excellent.
- **Act immediately — you never actually have more time**: A principle from Apple (Shelley Goldberg, Kate Berseron): if you know something needs to be done, do it now. In two days there will be a surprise that consumes that time.
- **Supply chain is both a product and a national security problem**: The chain for actuators (motors) traces back to raw magnets → magnet processing → actuator assembly, all largely outsourced to China, Japan, and Korea over 25 years. The same supply chain underpins drones and robots.
- **Actuators are the bottleneck for robotics**: If rare earth magnets become restricted, actuator designs must change — larger, less efficient, different materials. This cascades to all robots and drones. No equivalent US actuator industry exists yet.
- **Memory prices are a coming crisis**: AI data centers are consuming DRAM at a rate that is outpacing supply, with prices potentially doubling (one cited figure was 6x already). Her advice to hardware startups: pre-buy memory now.
- **A missing component = nothing ships**: If RAM changes form factor, it's a catastrophic redesign (new board layout, new supply chain, full re-test cycle). Simpler parts like diecast components take 3–5 months to re-source. Silicon changes are the worst-case scenario.
- **Humanoid robots are prototypes, not products**: Most strong humanoids carry a warning: no humans within 3 feet. The key safety parameters are mass distribution (pull mass inward), arm compliance (soft = lower impulse force), and actuator energy. 1X Neo cited as a thoughtful safety design.
- **Purpose-built robots will outpace humanoids in real deployment**: Modern factories already operate with near-zero human labor on PCB and mechanical assembly lines. You don't need humanoids to replace humans there — you need better dedicated robots. Humanoids serve long-tail general tasks.
- **AI can do PCB routing today but not solid CAD**: Claude and other LLMs can generate surface/point-cloud approximations but not parametric solid CAD with tolerance stacks. PCB component layout and routing is getting close. Full mechanical CAD requires world models that understand friction, contact, pressure, and surface texture — not yet available.
- **CAD training data is the bottleneck for AI in hardware**: Companies won't share proprietary 3D CAD files with model vendors. Hobbyist/open-source CAD is where AI-native hardware design will likely start, then move to on-prem fine-tuning within company walls.
- **AI-native engineers (age ~20) are categorically different**: Young engineers who grew up with AI use it from the ground up for problem-solving, not as a bolt-on tool. They are measurably faster. Senior engineers need to learn from them, not just vice versa.
- **Robot UX requires telegraphing intent**: Robots should look before turning, acknowledge humans entering the room, appear soft and non-threatening. Leila Takayama's research on human-robot interaction: sudden movement is alarming; preparatory gesture is not. Pixar/Disney are the world leaders in designing perceived intent through motion.
- **OpenAI departure rationale**: Left over governance concerns and lack of defined guardrails around the announcement of a "department of war" deal — specifically the speed and process of decision-making, not the people involved.
- **Lessons from legendary leaders**:
  - *Sam Altman*: Default to thinking 100x or 10,000x bigger. Forces recalibration on scope and ambition.
  - *Steve Jobs*: The quality bar was non-negotiable and consistent throughout the org. Being told something isn't good enough is highly motivating to an ambitious person.
  - *Mark Zuckerberg*: Decisions made at the lowest possible level for speed. Clear review cadence, well-defined objectives, technically engaged leadership (Zuck and Boz could read 20-page engineering trade-off docs and contribute substantively).
- **Verticalization is the hedge against supply chain fragility**: Elon's approach at Tesla (and especially Starlink — "raw materials in, silicon chips out") allows rapid PCB redesign when silicon supply is disrupted. Vertically integrated companies survived the chip shortage better than those with classic supply chains.
- **War is changing faster than consumer electronics**: Drones with 3D-printed parts being updated daily in Ukraine represent the future of conflict. Investment should favor drones over aircraft carriers. The cost asymmetry (missile vs. intercept cost) currently favors attackers.

## Use cases
- **Hardware startup founders** deciding where to invest early design effort and how to structure a product development process
- **Software-native companies entering hardware** (AI labs, consumer tech) that underestimate compile-cycle constraints and part variance
- **Robotics PMs and engineers** evaluating humanoid vs. purpose-built robot strategies for manufacturing or service deployment
- **Supply chain strategists** assessing risk concentration in memory, actuators, or rare earth magnets
- **Hardware procurement teams** considering pre-buying memory or other constrained components ahead of price spikes
- **Team builders at 0-to-1 hardware companies** figuring out the right mix of specialists, generalists, autonomous vehicle veterans, and AI-native junior engineers
- **Investors** evaluating the robotics/physical AI landscape, specifically the gap between prototype capability and manufacturable scale
- **Defense technology strategists** thinking about drone investment, supply chain independence, and adversarial AI threats to robotic systems
- **Robot UX/interaction designers** designing how robots signal intent, acknowledge humans, and avoid uncanny valley responses
- **AI researchers** considering what model architectures (world models vs. LLMs) are needed to enable CAD generation and physical simulation

## Patterns & frameworks

**The Hardware Compile Model**
Hardware gets 4–5 total design iterations ("compiles"), each taking 3–5 months. The last compile is mass production — irreversible. This forces decisions to be made correctly before you run out of iterations. Implication: front-load risk, lock KPIs early, never assume you have more time.

**Works-Like / Looks-Like Prototyping**
Build two parallel artifacts in early-stage hardware: a functional prototype (works-like) and an industrial design model (looks-like). They don't need to be the same object. The works-like prototype validates that the design can fit inside the looks-like envelope. Off-the-shelf components are preferred in this phase to maximize speed.

**KPI-Driven Hardware Design**
Define a small set of quantitative goals (price, weight, display resolution, clock speed, etc.) before starting and change them as little as possible. Trade-offs between KPIs should have explicit ratios (Kalinowski cites Elon's practice of assigning numeric values to weight-vs-cost trade-offs). When KPIs are clear, engineering decisions "fall out pretty easily."

**Hardest Part First**
Identify the architectural pinch points — where the design is most likely to fail — and resolve those before designing anything else. Example: routing cables through a hinge was designed before the hinge itself was finalized. Counterintuitive because engineers tend to start with the familiar.

**Component Hierarchy by Redesign Cost**
Classify components by the cost of losing supply: (1) Silicon/SOC — catastrophic redesign of the entire board; (2) RAM — catastrophic if form factor changes; (3) Actuators — severe, weeks-to-months delay; (4) Diecast parts — recoverable in 3–5 months. Secure highest-risk components first, both in design lockdown and supply chain agreements.

**Supply Chain Stack (Robotics)**
Raw materials (rare earth magnets) → material processing → actuator manufacturing → subassembly → final robot assembly. Each layer has been offshored over 25 years. Rebuilding independence requires working bottom-up. Disruption at any layer cascades upward.

**Robot Social UX Principles (from Leila Takayama's research)**
- Acknowledge humans entering a space (look up, orient toward)
- Transmit intent before acting (look before turning)
- Appear soft, non-threatening, reactive
- Study Pixar/Disney animation for motion design that conveys emotion and approachability
- Reduce arm mass and use compliant (soft) materials to lower impact impulse force

**Zero-to-One Hiring Stack**
For novel hardware categories: (1) Strong generalists who can transfer knowledge across domains; (2) Some domain specialists (robotics, autonomous vehicles for sensing/safety stacks); (3) People with experience scaling other hardware products; (4) AI-native young engineers (age ~20) who problem-solve AI-first — bring them in to teach the team; (5) Mission-aligned people, because cross-disciplinary teams (AI researchers + hardware engineers) need shared direction to communicate effectively.

**The Frontier Saturation Model**
AI capabilities behind a keyboard will eventually saturate (digital intelligence). When that happens, the next frontier is physical: robotics, manufacturing, sensing, autonomy, space. Companies that built VR/AR infrastructure (SLAM, depth sensing, spatial computing) are ahead on this transition because the underlying technology transfers directly.