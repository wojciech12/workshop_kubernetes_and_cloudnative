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

3. Devs:

   Covered: liveness and readiness probes + more examples, and how to shutdown your application correctly, QoS.

4. Basics CI/CD - how to work with manifests and how to generate them.

   Covered: envsubst, helm, and kustomize.

5. CI/CD for Kubernetes in your company

6. Observability:

   - [Monitoring with Prometheus stack](https://github.com/wojciech12/talk_monitoring_with_prometheus)
   - Structured logging

7. Next:

   - [zero-downtime deployments](https://github.com/wojciech12/workshop_kubernetes_and_cloudnative/blob/master/README.rst)
   - ArgoCD

8. Next++:

   - RBAC
   - security
   - observability
   - see the Outlook section in [workshop manual introduction.pdf](01_introduction/introduction.pdf)

Development topics, e.g., building your own operator or kubectl plugin, see [workshop_golang](https://github.com/wojciech12/workshop_golang).

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

Looking for a Kubernetes, CloudNative, Golang, or Machine Learning training, reach me at  wbarczynski.pro@gmail.com or [LinkedIN](https://www.linkedin.com/in/wojciechbarczynski/).
