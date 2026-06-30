# Popping the GPU Bubble

Source: https://moondream.ai/blog/popping-the-gpu-bubble

## Summary
Moondream's engineering blog explains how their inference engine Photon achieves up to 35% higher decode throughput by eliminating "GPU bubbles" — idle periods where the GPU waits for the CPU to finish housekeeping between token generation steps. The core technique, called pipelined decoding, overlaps CPU bookkeeping for one token with GPU computation for the next. Three supporting mechanisms make this safe: ping-pong slots to prevent buffer collisions, a forward/sample split to handle constrained decoding, and a lightweight reference-counting system ("zombies") to cleanly retire finished sequences.

## Key takeaways
- **GPU bubbles** occur because the CPU must do non-trivial work (batch selection, kernel launch, token commit) between each GPU forward pass, leaving the GPU idle during that window.
- **Pipelined decoding** launches the next token's GPU forward while the CPU is still committing the previous token's result, hiding the bubble entirely.
- **Ping-pong slots** (two alternating buffer sets) prevent the in-flight step from overwriting results the CPU hasn't read yet.
- **Forward-now, sample-later** allows even constrained decoding (structured outputs like coordinates or bounding boxes) to run the GPU forward ahead of time, since the mask is only needed at sampling, not at forward computation.
- **Zombie refcounting** handles sequences that finish mid-pipeline: they ride along harmlessly in the already-launched step and are released only once all in-flight references drop to zero.
- **Gains scale with hardware speed**: on an NVIDIA B200 at 32 concurrent streams, observed throughput improvement was ~35%; on an older RTX 3090 at 1 stream, it was ~6.5%.
- **Prefill and decode share the same pipeline**, which is especially beneficial for short-output workloads dominated by prefill steps.
- The improvement comes from compounding many such low-level optimizations across the full serving stack, not any single technique alone.