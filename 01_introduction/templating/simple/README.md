## Simple CD with generic templating

Other options are: Jinja2, Go templating, etc.

```bash
# prod - injected as a part of CI/CD
export HOST=my.example.com
export REPLICA_COUNT=3
export APP_VERSION=2.0.0

# staging
export HOST=staging-my.example.com
export REPLICA_COUNT=1
export APP_VERSION=1.0.0

# dev
export HOST=dev-my.example.com
export REPLICA_COUNT=1
export APP_VERSION=snapshot-989

# CI/CD
touch tmp_all.yaml
find . -iname "*.yaml" | \
       grep -v 'tmp_all.yaml' | \
       xargs -I {} bash -c "envsubst < {}; echo '---'" >> tmp_all.yaml

# let's check whether it works
kubectl apply -f tmp_all.yaml --dry-run=server

# apply!
kubectl apply -f tmp_all.yaml

# for prod
curl --header 'Host: my.example.com'  http://127.0.0.1:8000/echo

# let's clean up
kubectl delete -f tmp_all.yaml
```