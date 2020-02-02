===================
Kubernetes Workshop
===================

Workshops
=========

0. Docker Best Practices:

   - `summary <docker/docker.md>`_

1. Introduction:

   - `workshop manual <introduction.pdf>`_
   - `slides <introduction_deck/index.pdf>`_ (notice: 14MB)

2. Advanced:

   - security
   - observability
   - `zero-downtime deployments <https://github.com/wojciech12/workshop_kubernetes_and_cloudnative/blob/master/README.rst>`_
   - see the Outlook section in `workshop manual <introduction.pdf>`_

Development topics, e.g., building your own operator or kubectl plugin, see `workshop_golang <https://github.com/wojciech12/workshop_golang>`_.

Prerequisites
=============

- laptop at least 8GB, the best: 16GB memory (preferable: linux or macOS)
- installed:
  
  - git
  - `docker <https://docs.docker.com/install/>`_
  - `kubectl client <https://kubernetes.io/docs/tasks/tools/install-kubectl/>`_
  - `minikube <https://minikube.sigs.k8s.io/>`_
  - python

Setup
=====

::

  # notice: you need to have pandoc installed
  pdflatex  --shell-escape  introduction.tex

Contact 
=======

| Looking for a Kubernetes, CloudNative, Golang, or Machine Learning training, reach me at
| wbarczynski.pro@gmail.com or `LinkedIN <https://www.linkedin.com/in/wojciechbarczynski/>`_.
