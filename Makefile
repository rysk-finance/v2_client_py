.PHONY: tests
tests:
	poetry run pytest tests -vv

install:
	poetry install

fmt:
	poetry run black tests rysk_v2 examples
	poetry run isort tests rysk_v2 examples

lint:
	poetry run flake8 tests rysk_v2 examples

all: fmt lint tests

test-docs:
	echo making docs

release:
	$(eval current_version := $(shell poetry run tbump current-version))
	@echo "Current version is $(current_version)"
	$(eval new_version := $(shell python3 -c "import semver; print(semver.bump_patch('$(current_version)'))"))
	@echo "New version is $(new_version)"
	poetry run tbump $(new_version)

