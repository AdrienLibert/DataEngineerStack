DOCKER_COMPOSE_FILE=docker-compose.yaml

build:
	docker-compose -f $(DOCKER_COMPOSE_FILE) up --build -d
	python main.py

run:
	python read_streaming.py

down:
	docker-compose -f $(DOCKER_COMPOSE_FILE) down
ps:
	docker ps

network:
	docker network ls

read:
	python read_parquet.py
