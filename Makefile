VENV := .venv
PROJECT_DIR := assisted_test_infra_client
APP_NAME :=  assisted_test_infra_client

# default target
all: venv

$(VENV)/bin/activate:
	python3 -m venv $(VENV)
	./$(VENV)/bin/pip install -r requirements.txt

# venv is a shortcut target
venv: $(VENV)/bin/activate

lint: pylint

pylint: venv
	./$(VENV)/bin/pip install -q -r test-requirements.txt
	./$(VENV)/bin/pylint ./${PROJECT_DIR}

run: venv
	./$(VENV)/bin/python3 assisted_test_infra_client/main.py

clean:
	rm -rf $(VENV)
	find . -type f -nam
	e '*.pyc' -delete

.PHONY: all venv run clean

# Docker helpers

docker-build-image:
	docker build -t ${APP_NAME} -f Dockerfile .

docker-cleanup:
	docker ps -q --filter "name=${APP_NAME}" | xargs -r docker kill && sleep 3
	docker ps -a -q --filter "name=${APP_NAME}" | xargs -r docker rm

docker-run: docker-cleanup
	docker run --name ${APP_NAME} -d ${APP_NAME}

docker-rebuild-and-run: docker-build-image docker-run
