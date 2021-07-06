## Continuous Deployment


### Exercise 1

```
$ cd exercise_1
$ ls .cicd # .gitlabci

run_cicd.sh
```

```
$ ls
|- deployment
|
|- Makefile
|
\-VERSION
```

### Exercise 2

We have learnt about a simple approach with envsubst, let's see an alternative with helm:

```
$ cd exercise_2
$ ls .cicd # .gitlabci

run_cicd.sh
```


```bash
$ export APP_NAME=my-app
$ export APP_VERSION=snapshot-9911

$ helm template "${APP_NAME}" deployment_v2 \
   --set image.tag="${APP_VERSION}" \
   --version "${APP_VERSION}"

# in CI/CD, dry run for safety :)
$ helm template "${APP_NAME}" deployment_v2 \
   --set image.tag="${APP_VERSION}" \
   --version "${APP_VERSION}" | kubectl apply -f - --dry-run=server


# in CI/CD, again --dry-run for safety
$ helm install "${APP_NAME}" deployment_v2 \
   --set image.tag="${APP_VERSION}" \
   --version "${APP_VERSION}" --dry-run --debug
```

### Exercise 3

and kustomize

```
$ cd exercise_3
$ ls .cicd # .gitlabci
```

### Exercise 4

Argocd:

```
$ cd exercise_4
```
