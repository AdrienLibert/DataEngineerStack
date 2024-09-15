IMAGE_NAME=mon-generator
DOCKER_COMPOSE_FILE=docker-compose.yaml
CONTAINER_ID=$(shell docker ps -qf "ancestor=$(IMAGE_NAME)")

build:
	docker build -t $(IMAGE_NAME) .
	docker-compose -f $(DOCKER_COMPOSE_FILE) up --build

run
	docker network create kafka-net
	docker network connect kafka-net kafka
	docker run --network kafka-net -e KAFKA_BOOTSTRAP_SERVERS=kafka:9092 $(IMAGE_NAME)

down:
	docker stop $(CONTAINER_ID)
	docker rm $(CONTAINER_ID)
	docker-compose -f $(DOCKER_COMPOSE_FILE) down
	docker network rm kafka-net

ps:
	docker ps

network:
	docker network ls
