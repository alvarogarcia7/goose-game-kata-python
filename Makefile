virtualenvironment:
	python3.12 -m venv venv
.PHONY: virtualenvironment

virtualenvironment-finish: check-virtual-env
	python3.12 -m ensurepip --upgrade
	pip3.12 install --upgrade setuptools
.PHONY: virtualenvironment-finish

check-virtual-env:
	@# Test if the variable is set
	@if [ -z "${VIRTUAL_ENV}" ]; then                                               \
  		echo "Need to activate virtual environment: source ./venv/bin/activate";    \
  		false;       																\
  	fi

install: requirements install-githooks
.PHONY: install

install-githooks: check-virtual-env
	pre-commit install
.PHONY: install-githooks

test: check-virtual-env typecheck test-python
.PHONY: test

requirements.txt: check-virtual-env
	pip3 freeze > requirements.txt
.PHONY: requirements.txt

freeze: requirements.txt

test-python: check-virtual-env
	pytest .
.PHONY: test-python

typecheck: check-virtual-env
	mypy . --exclude venv
.PHONY: typecheck

requirements: check-virtual-env
	pip3 install -r requirements.txt

pre-commit: test
.PHONY: pre-commit
