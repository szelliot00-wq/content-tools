# Xiaomi-Robotics-1

Source: https://robotics.xiaomi.com/xiaomi-robotics-1.html

## Summary
Xiaomi-Robotics-1 is a robot foundation model that addresses the data scarcity problem in robotics by using 100,000 hours of embodiment-free (UMI) video trajectories for pre-training, followed by a post-training stage with 7,200 hours of real-robot data to align the model with physical robots and natural language instructions. The model follows the LLM training paradigm and demonstrates clean scaling laws: performance improves predictably as data volume and model size increase, with no signs of saturation. After post-training, it achieves strong generalization to unseen environments and adapts to new tasks with minimal data.

## Key takeaways
- **Embodiment-free pre-training at scale**: 100K hours of UMI trajectories across 1,700+ scenarios (household, commercial, industrial, outdoor) break the traditional robot data bottleneck without requiring a physical robot.
- **Two-stage training mirrors LLMs**: Pre-training builds general action-generation representations; post-training aligns those capabilities to real robot embodiments and natural-language instruction following.
- **Scaling laws transfer to real robots**: Larger pre-trained models yield higher real-robot success rates after post-training, and the gains show no sign of saturation.
- **High data efficiency for new tasks**: With under 10 hours of demonstrations per task, XR-1 achieves 75% overall success on novel tasks (phone packing, laundry loading, etc.), nearly doubling the π0.5 baseline (40%); under 40 hours lifts it to 85%.
- **State-of-the-art on simulation benchmarks**: XR-1 tops all four evaluated benchmarks — RoboCasa, RoboCasa365, VLABench, and RoboDojo — with relative gains ranging from +2.6% to +58.3% over second place.
- **Auto-labeling pipeline enables scale**: A VLM-powered annotation system labels long video trajectories by describing gripper/object state transitions, making large-scale labeling feasible without human annotators.