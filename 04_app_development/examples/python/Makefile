SERVICE_NAME=hello_world

snapshot:
	docker build -t hello_world:snapshot-$$(git rev-parse --short HEAD) .

release:
	docker build -t hello_world:1.0.0 .

fmt:
	black hello test *.py

lint:
	black --check hello test *.py
