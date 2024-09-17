DOCKER_COMPOSE_FILE=kafka/docker-compose.yaml

build:
run:
	pip install -e .
	python etl/etl.py

down:
	docker-compose -f $(DOCKER_COMPOSE_FILE) down

ps:
	docker ps

network:
	docker network ls