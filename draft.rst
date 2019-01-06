.. class:: center

################################
Kubernetes Introduction Workshop
################################

Golang Warsaw Meetup Workshop by Wojciech Barczynski.
Licence: `CC BY 2.0 <https://creativecommons.org/licenses/by/2.0/>`_

.. raw:: pdf

   PageBreak

.. contents:: Table of Contents

.. raw:: pdf

   PageBreak

0. Prerequiments
################

- Workstation with Linux or OSX recommeded.
- Software:

  - Minikube
  - Kubernetes CLI
  - Docker

- Tools:

  - `jq <https://stedolan.github.io/jq/>`_

- Good to have:

  - hub.docker.com account or alternative docker repository

HowTos:

- `Install Minikube at kubernetes.io <https://kubernetes.io/docs/tasks/tools/install-minikube/>`_
- `Install Kubernetes CLI - kubectl at kubernetes.io <https://kubernetes.io/docs/tasks/tools/install-minikube/>`_

Check:

::

  $ minikube status
  $ minikube start

::

  $ kubectl config use-context minikube
  $ kubectl get nodes

You should see:

::

  ☁ ⚡ kubectl get nodes
  NAME       STATUS   ROLES    AGE   VERSION
  minikube   Ready    master   59d   v1.10.0

1. Kubernetes CLI - Kubectl
###########################

Let's learn first some basics regarding the Kubectl:

::

  kubectl get <ARTIFACT>
  kubectl describe <ARTIFACT>

1. List the nodes:

   ::

     kubectl get nodes

   Q: What the names of our nodes are? . . .

2. Get short info on one node:

   ::

     kubectl get nodes minikube

     # notice:
     kubectl get no minikube
     kubectl get node minikube

3. Get more details:

   ::

     kubectl describe nodes minikube

   Write down:

   - Container Runtime Verison: . . .
   - What the namespaces we have: . . .
   - Note down name of two pods:

     1. ...

     2. ...

4. YAML and JSON output:

   ::

     kubectl get node minikube -o yaml
     kubectl get node minikube -o json

   Use `jq` to get the `kubeletVersion`, write down below:

   . . .

5. More magic, you can specify a jsonpath directly:

   ::

     kubectl get node minikube \
       -o jsonpath="{.status.daemonEndpoints.kubeletEndpoint.Port}"

   ::

     kubectl get node minikube -o jsonpath="{.metadata.labels}"

   Write down a command with jsonpath to get information on how many CPU we have allocated to our minikunbe:

   . . .

6. You can find nodes (and other k8s artifacts) by lables:

   ::

     kubectl get nodes  -l 'kubernetes.io/hostname'=minikube

   Please find another label, you could select our node and run the command.

7. There is so much more:

   ::

     kubectl api-resources

Hints:

- ```kubectx``` and ```kubens``` - https://github.com/ahmetb/kubectx
- ```alias k=kubectl``` or ```alias kb=kubectl```, example: `zprezto-kubernetes-aliases plugin <https://github.com/belak/prezto-contrib/tree/master/contrib-kubernetes>`_

2. Kubectl configuration file
#############################

Good to know. You can find there also your token, certificates, etc.

1. Open:

   ::

     cat ~/.kube/config

2. Find what the `certificate-authority` is for minikube cluster

3. What the main sections are:

   . . .
   . . .
   . . .

3. Namespace kube-system
########################

Let's look around what we have here.

1. What are the namespaces?

   ::

     $ kubectl get ns
     $ kubectl get namespaces

   Notice:

   - you can create namespaces to better organize your components
   - you define resource restrictions for namespaces
   - afect the name: ```<service-name>.<namespace-name>.svc.cluster.local```. We will talk about it later.

   To change the selected namespace:

   ::

     $ kubectl config set-context $(kubectl config current-context) --namespace

2. Get the list of pods in namespace kube-sytem:

   ::

     $ kubectl get po --namespace=kube-system
     $ kubectl get po -n=kube-system

   Using ```kubectl describe po <pod-name> --namespace=kube-system``` find what is the version of:

   - kube-proxy: . . .
   - apiserver: . . .
   - coredns: . . .

3. Get the list of services:

   ::

     $ kubectl get svc --namespace=kube-system

   Using ```kubernetes describe svc <svc-name> --namespace=kube-system``` find what the endpoints are for:

   - kube-dns: . . .
   - kubernetes-dashboard: . . .

4. Logs:

   ::

     $ kubectl logs coredns-c4cffd6dc-l8xl8 --namespace=kube-system
     $ kubectl logs coredns-c4cffd6dc-l8xl8 --namespace=kube-system -f
     $ kubectl logs coredns-c4cffd6dc-l8xl8 --namespace=kube-system --tail=10

   Please display logs of the kube-apiserver, kube-proxy, kube-scheduler, and etcd-minikube.

   Later, we will also cover events: ```kubectl get events.events.k8s.io --namespace=kube-system```.

5. Get the console:

   ::

     $ kubectl exec -it kube-apiserver-minikube /bin/sh --namespace=kube-system

6. Kubernetes Dashboard:

   ::

     # on normal deployment:
     # $ kubernetes proxy
     $ minikube dashboard

7. Basic metrics:

   ::

     minikube addons enable metrics-server
     # after some time:
     kubectl top nodes
     kubectl top pods

4. Kubernetes deployments.yaml
##############################

We have been playing around with kube-system, now let's get our service up and running.

Deploy!
-------

1. Get the deployment file `introduction/kube-deployment.yaml <introduction/kube-deployment.yaml>`_:

   .. code-block:: yaml

     apiVersion: apps/v1
     kind: Deployment
     metadata:
       name: intro-app
       labels:
         app: intro-app
     spec:
       replicas: 1
       selector:
         matchLabels:
           app: intro-app
       template:
         metadata:
           labels:
             app: intro-app
         spec:
           containers:
           - name: app
             image: wojciech11/api-status:1.0.0
             imagePullPolicy: Always
             ports:
             - containerPort: 80

   Notice:

   - if your repo is private, you need to define ````imagePullSecrets```.
   - A force pulling image every time: ```imagePullPolicy: Always```, helpful during development, do not use in *production*

2. Deploy:

   ::

     kubectl create -f introduction/kube-deployment.yaml

3. Check:

   ::

     kubectl get po
     kubectl get po -n default

  ::

    kubectl describe po <POD_NAME>

4. To learn about the deployments:

   ::

     kubectl get deploy
     kubectl get deployment


   ::

     kubectl describe deploy <DEPLOYMENT_NAME>

   What the update strategy do we use?

   . . .

5. Find the following information:

   - What is the IP of your app pod? . . .
   - What is ReplicatSet? . . .
   - Ready? . . .
   - Restart Count? . . .
   - Events? . . .

   Notice: In future, we will learn about Liveness/Readiness probe.

Opening console in your container
---------------------------------

Imagine, we cannot reach our application. Let's check it within the running container.

1. Get the console:

   ::

     kubectl exec -it intro-app-65db487447-lrhb9 /bin/bash

   Notice: There is ongoing discussion whether it is the "new" ssh.

2. Add tool for debugging - curl:

   ::

     apt-get update && apt-get install -qq curl

3. Does it work?

   ::

      # does it work?
      curl 127.0.0.1

      # can we get outside
      curl -I wbarczynski.pl

      # can we reach other services:
      telnet kube-dns.kube-system 53

4. Yes, we fix the bug, let's clean up:

   ::

     kubectl delete po intro-app-65db487447

   ::

     # notice the name change
     kubectl get po

Port-forwarding
---------------

What If I told you, you can debug your app from your laptop.

1. Find the port our service listen, check the deployment file.

2. Setup the port forwarding:

   ::

     kubectl proxy-forward <POD_NAME> 8080:<PORT_NUMBER>

3. Use curl to query our app.

Let's learn about services and ingresses, before learning how to modify deployment and update your application.

5. Kubernetes Service
#####################

Our factory, I mean the deployment defined how we create our applications as pods.

Now, let's define the interface.

1. Get the service file `introduction/kube-service.yaml <introduction/kube-service.yaml>`_:

   .. code-block:: yaml

     apiVersion: v1
     kind: Service
     metadata:
       name: intro-app
     spec:
       ports:
       - port: 80
         protocol: TCP
       selector:
         app: intro-app
       type: LoadBalancer

2. Deploy:

   ::

     kubectl create -f introduction/kube-service.yaml
     kubectl apply -f introduction/kube-service.yaml

3. Check:

   ::

     kubectl get svc

4. Find out the endpoint IP: . . .

5. We few types of services:

   - with ClusterIP
   - ClusterIP: None
   - LoadBalanced

6. Let's access it:

  ::

    export SVC_PORT=$(kubectl get service intro-app \
                     --output='jsonpath="{.spec.ports[0].nodePort}"' \
                    | tr -d '"')
    curl  $(minikube ip):${SVC_PORT}

   Notice: on Azure, AWS, or Google, we would get the loadbalancer created and public IP assigned.

7. How it works?

   ::

     # run bash
     kubectl
     curl api-service

Modyfing kubernetes deployment and service
------------------------------------------

You SHOULD NOT follow 1 and 2:

1. Change the number of pods running to 2 with:

   ::

     kubectl edit deploy

   ::

     kubectl get po

2. Change the value of 'me' to your name in the service definition.

3. Modify the depoyment.yml to get 3 running pods, use: ```kuebctl apply -f <YOUR_DEMPLOYMENT_FILE>```

4. Add one more label to service.

5. What does happen if we add one more selector, apply new vesion of our service:

   ::

     apiVersion: v1
     kind: Service
     metadata:
       name: intro-app
       labels:
         me: wojtek
     spec:
       ports:
       - port: 80
         protocol: TCP
       selector:
         app: intro-app
         break: the-connection-with-pods
       type: LoadBalancer

   ::

     # ?
     curl -I  $(minikube ip):${SVC_PORT}

   ::

     # what has changed
     kubectl describe svc intro-app

   Notice: very common issue :D

6. Fix our service.

6. Updating service
###################

Let's update our app from the version 1.0.0 to 2.0.0:

1. Change in the deployment file and apply changes.

2. You can also change it with set image:

  kubectl set image deployment/<CONTAINER_NAME> \
  <CONTAINER_NAME>=<DOCKER_IMAGE_NAME>:<VERSION>

3. Change two times from 1.0.0 to 2.0.0 and back:

   ::

     curl -I  $(minikube ip):${SVC_PORT}

6. Kubernetes Ingress
#####################



Ingress defs and curl, to show how the ingress rules works.

Good to know: you can secure your ingress with htauth.


1. Change

2. Do:

kubectl apply


1. Deploy your application, minimum.

7. Containers vs Pods
#####################

A scenario with 2 containers per pod, e.g., nginx with caching

8. Failover
###########

1. Open console.

2. Force restart:

   ::

     # :D
     kill -9 1

Repeat 5 times. Observer the output from: ```kubectl get po```.

9. How to debug
###############

Rememmber to ship minimum debugging tools, such as, curl or telnet.

Happy debugging path:

::

  kubectl describe ing
  kubectl describe svc
  kubectl exec -it <> /bin/bash
  # curl, telnet, ...
  kubectl describe po <>

::

  kubectl logs <>
  kubectl logs <> -f
  kubectl logs <> --tail=100

::

  kubectl logs <YOUR_INGRESS_CONTROLER_POD>

::

  kubectl get events

10. Kubernetes config
####################

xxx

11. Upgrade your application
###########################

xyz

12. Kubernetes secret
####################

uuu

13. Opinioneted Configuration
############################

1. envsubst! :D
2. Ksonnect
3. Helm

14. Kubernetes Persistent Volumes
#################################

A persistence storage that survives your pod being deleted.

15. Outlook
###########

What you could learn next.

@wojciech12: for me to see the context of the material in this workshop.

Next course *Immediate*:

1. Liveness/Readiness probes
2. Monitoring with Prometheus
3. Resource and Limits, QoS for your pods, schedule policies
4. Statefulsets
5. DaemonSets

Would be great to touch Observability topics, such as Tracibility or Logging with, e.g., EFK.

*Advance*:

1. Zero-downtime deployment strategies
2. Horizontal scalling (beta: pod scalling for the pets)
3. Continous Deployment and Integration
4. TravisCI and Gitlab
5. (sic :/ ) gitops from weave, have to say few things...

*Network and Security*:

1. RBAC deep dive
2. Networking - Internal Loadbalancing - https://kubernetes.io/docs/concepts/services-networking/
3. Egress - https://kubernetes.io/docs/concepts/services-networking/network-policies/
4. IpBlock

*Kubernetes customization*

1. Write your first CRD
2. ...
3. ...
4. FaaS? Kubeless?

*CloudNative Ecosystem*

1. Observability: Prometheus stack
2. Observability: EFK
3. Observability: Tracing
4. Ingress Controllers: Traefik, ... , talk about standard and controller-specific annotations
5. Cert-manager??
6. Backups? ark?
7. Operators for etcd and Vault

*Optionals*

1. Google Kubernetes Engine
2. Azure Kubernetes Service
3. Amazon Elastic Kubernetes
