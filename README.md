# Kubernetes Workshops

## Workshops

0. Docker Best Practices:

   - [Quick summary](00_docker/README.md)

1. Introduction part 1 - quickstart:

   - [workshop manual](01_introduction/introduction.pdf)
   - [slides](01_introduction/slides/index.pdf) (notice: 14MB)

   Covered: service, deployment, ingress, configmap, secrets, and daemonsets.

2. Introduction part 2 - k8s namespace and more resources to learn:

   - [workshop manual](02_advanced/main.pdf)
   - slides as above

   Covered: kubernetes namespace, daemonsets, statefulsets, volumens, PVC, and job/cronjob.

3. Continuous Deployment - how to work with manifests and how to generate them.

   - [workshop manual](03_continuous_deployment/README.md)
   - [slides](03_continuous_deployment/slides/index.pdf)
   - [examples](03_continuous_deployment/)

   Covered: continuous deployment, envsubst, helm, and kustomize.

4. Development for Kubernetes:

   - [slides](04_app_development/slides/index.pdf)
   - [examples](04_app_development/examples)

   Covered: liveness and readiness probes + more examples, and how to shutdown your application correctly, QoS. Quickstart with observability.

5. CI/CD for Kubernetes in your company

6. Observability deep dive [WIP]:

   - [Monitoring with Prometheus stack](https://github.com/wojciech12/talk_monitoring_with_prometheus)

7. Zero-downtime deployment deep dive:

   - [zero-downtime deployments presentation](https://github.com/wojciech12/talk_zero_downtime_deployment_with_kubernetes)

8. CloudNative, selected projects:

   - Istio
   - ArgoCD
   - [Open Policy Agent](https://www.openpolicyagent.org/)
   - [conftest](https://www.conftest.dev/)

8. Next:

   - RBAC
   - security
   - building your own operator or kubectl plugin, see [workshop_golang](https://github.com/wojciech12/workshop_golang)
   - see the Outlook section in [workshop manual introduction.pdf](01_introduction/introduction.pdf)

## Prerequisites

- Workstation with at least 8GB, the best: 16GB memory
- Preferable *nix: Linux or MacOS
- Installed:

  - git, curl or [httpie](https://httpie.io/), wget, [jq](https://stedolan.github.io/jq/)
  - [docker](https://docs.docker.com/install/)
  - [kubectl client](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
  - [k3d](https://k3d.io/)
  - python3 and your development language of choice

## Development

Manuals are written in Latex, for slides I use [revealjs](https://revealjs.com/).

```
$ cd 01_introduction
$ make pdf
```

## Contact

Looking for a Kubernetes, CloudNative, Golang, or Machine Learning training, reach me at  wbarczynski+trainings@gmail.com or [LinkedIN](https://www.linkedin.com/in/wojciechbarczynski/).
