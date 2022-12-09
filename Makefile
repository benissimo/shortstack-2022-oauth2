
setup:
	docker network create shortstack

build: build-api-server build-authorization-server build-client

build-client:
	docker build -t shortstack-client:latest . -f docker/client/Dockerfile

build-authorization-server:
	docker build -t shortstack-authorization-server:latest . -f docker/authorization-server/Dockerfile

build-api-server:
	docker build -t shortstack-api-server:latest . -f docker/api-server/Dockerfile

build-attack-server:
	docker build -t shortstack-attack-server:latest . -f docker/attacking/Dockerfile

run-client: build-client
	docker run -p 5050:5050 --net shortstack shortstack-client

run-authorization-server: build-authorization-server
	docker run -p 5051:5051 --net shortstack shortstack-authorization-server

run-api-server: build-api-server
	docker run -p 5052:5052 --net shortstack shortstack api-server
