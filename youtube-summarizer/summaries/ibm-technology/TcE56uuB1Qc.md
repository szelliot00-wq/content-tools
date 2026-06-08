# Kubernetes vs. OpenShift: Choosing DevOps and CI/CD Workflows

Video ID: `TcE56uuB1Qc`

## Summary
This video compares Kubernetes and OpenShift, explaining how OpenShift extends Kubernetes into a full platform with built-in tooling for CI/CD, security, and operations. It walks through the infrastructure layers OpenShift can run on and demonstrates a typical dev-to-deployment workflow. The goal is to help viewers decide which approach fits their needs based on complexity and team requirements.

## Key insights
- **Kubernetes is a foundation, not a full platform.** It handles container scheduling, scaling, and networking, but you must assemble pipelines, security, and monitoring separately.
- **OpenShift is Kubernetes with a pre-built platform layer.** It adds CI/CD pipelines, operators, web console, image registry, and ready-to-use configurations on top of core Kubernetes.
- **OpenShift supports broad infrastructure flexibility.** It runs on public cloud, private cloud, VMware, and bare metal — all with the same platform experience.
- **The dev workflow is streamlined in OpenShift.** A code push triggers a pipeline, which builds a container image, stores it in a registry, and deploys it via image streams — one cohesive flow.
- **Ops teams get a unified management experience.** The web console allows cluster management, resource monitoring, and issue resolution in one place without stitching together separate tools.
- **Scaling is simplified.** Teams can scale horizontally by adding nodes or vertically by running more pods, with straightforward controls available through the platform.
- **The core tradeoff is DIY vs. integrated.** Kubernetes gives flexibility and control; OpenShift trades some of that for speed, consistency, and reduced operational overhead.