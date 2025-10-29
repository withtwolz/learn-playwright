.PHONY: setup

format:  # Run black formatter
	@python3 -m black

setup:  # Setup dependencies and pre-commit hooks
	@python3 -m venv venv && \
	source ./venv/bin/activate && \
	pip install . && \
	pre-commit install && \
	echo "[learn-playwright]: Setup complete! Source the virtual environment with 'source ./venv/bin/activate'"

test:  # Run pytests
	python3 -m pytest -vv ./src