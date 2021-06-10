DOCKER_REGISTRY=docker.io
DOCKER_PROJECT_ID=wojciech11

SERVICE_NAME=hello-app
DOCKER_IMAGE_NAME=$(DOCKER_PROJECT_ID)/${SERVICE_NAME}
DOCKER_IMAGE_REPO_NAME=$(DOCKER_REGISTRY)/$(DOCKER_IMAGE_NAME)

release:
	docker build -t $(DOCKER_IMAGE_NAME):1.0.0 .

release_push: release
	docker push $(DOCKER_IMAGE_REPO_NAME):1.0.0

snapshot:
	docker build -t $(DOCKER_IMAGE_NAME):snapshot-$$(git rev-parse --short HEAD) .

snapshot_push: snapshot
	docker push $(DOCKER_IMAGE_REPO_NAME):snapshot-$$(git rev-parse --short HEAD)
