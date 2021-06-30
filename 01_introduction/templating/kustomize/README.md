## Example of Kustomize

```bash
cd kubernetes

export ENV_NAME=dev
kubectl kustomize "${ENV_NAME}"

kubectl kustomize "${ENV_NAME}" | \
  kubectl apply -f - --dry-run=client

kubectl kustomize "${ENV_NAME}" | \
  kubectl apply -n default -f -

curl --header 'Host: dev-ocr.example.com' http://127.0.0.1:8000/extract
```

### Reference

- [Declarative Management of Kubernetes Objects Using Kustomize](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/)
