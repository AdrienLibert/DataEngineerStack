DOCKER_COMPOSE_FILE=kafka/docker-compose.yaml

build:
	docker-compose -f $(DOCKER_COMPOSE_FILE) up --build -d
	python faker/main.py

run:
	python etl/read_streaming.py

down:
	docker-compose -f $(DOCKER_COMPOSE_FILE) down
ps:
	docker ps

network:
	docker network ls

read:
	python read_parquet.py
