DOCKER_COMPOSE_FILE=kafka/docker-compose.yaml

build:
	docker-compose -f $(DOCKER_COMPOSE_FILE) up --build -d
	pip install -r requirements.txt
	python faker/main.py

run:
	pip install -e .
	python etl/etl.py

down:
	docker-compose -f $(DOCKER_COMPOSE_FILE) down

ps:
	docker ps

network:
	docker network ls