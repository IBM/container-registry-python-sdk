# This makefile is used to make it easier to get the project set up
# to be ready for development work in the local sandbox.
# example: "make setup"

setup: deps dev_deps install_project

all: setup test-unit lint

deps:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

dev_deps:
	pip install -r requirements-dev.txt

install_project:
	pip install -e .

test: test-unit test-int

test-unit:
	python -m pytest test/unit

test-int:
	python -m pytest test/integration

test-int-registry:
	python -m pytest test/integration/test_container_registry_v1.py

test-int-va:
	python -m pytest test/integration/test_vulnerability_advisor_v4.py

lint:
	./pylint.sh

ci: deps dev_deps install_project test-unit lint
