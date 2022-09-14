DOCKER := docker
TAG := trade_image
DOCKER_COMPOSE := docker-compose

.PHONY: venv
venv:
	pip install virtualenv && virtualenv venv

.PHONY: build
build:
	pip install -r requirements.txt

.PHONY: trade
trade:
	python3 main.py

.PHONY: history_trades
history_trades:
	cd History_price && python view_all_files.py

#.PHONY: build
#build:
#	$(DOCKER) build -t $(TAG) .
#
#.PHONY: integration
#integration: build
#	$(DOCKER_COMPOSE) up -d
#
#.PHONY: run
#run:
#	$(DOCKER_COMPOSE) up
#
#.PHONY: makemigrations
#makemigrations:
#	$(DOCKER_COMPOSE) exec trades python manage.py makemigrations
#
#.PHONY: migrate
#migrate:
#	$(DOCKER_COMPOSE) exec trades python manage.py migrate
#
#.PHONY: superuser
#superuser:
#	$(DOCKER_COMPOSE) exec trades python manage.py createsuperuser
