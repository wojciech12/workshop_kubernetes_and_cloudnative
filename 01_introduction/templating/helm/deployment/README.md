## Simple templating with Helm

```bash
# CI/CD

# prod
export APP_NAME=intro-app
export APP_VERSION=2.0.0

# staging
export APP_NAME=intro-app
export APP_VERSION=1.0.0

# validate
helm template "$APP_NAME" ../deployment \
   --values values_staging.yaml --set image.tag="${APP_VERSION}" \
   | kubectl apply -f - --dry-run=client

# apply
helm template "$APP_NAME" ../deployment \
   --values values_staging.yaml --set image.tag="${APP_VERSION}" \
   | kubectl apply -f -

kubectl get po -n intro-app

# for staging
curl --header 'Host: staging-my.example.com' http://127.0.0.1:8000/echo
```
