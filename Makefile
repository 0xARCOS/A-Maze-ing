PYTHON := python3
MAIN := a_maze_ing.py
ARGUMENTS := config.txt
.PHONY: install run debug clean lint lint-strict

install:
	@echo "Installing dependencies..."
	@if [ -f requirements.txt ]; then \
		pip install -r requirements.txt; \
	elif [ -f pyproject.toml ]; then \
		pip install .; \
	else \
		echo "No dependency file found (requirements.txt or pyproject.toml)."; \
	fi

run:
	@echo "Running project..."
	$(PYTHON) $(MAIN) $(ARGUMENTS)

debug:
	@echo "Running project in debug mode..."
	$(PYTHON) -m pdb $(MAIN) $(ARGUMENTS)

clean:
	@echo "Cleaning cache and temporary files..."
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

lint:
	@echo "Running lint checks..."
	flake8 .
	mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	@echo "Running strict lint checks..."
	flake8 .
	mypy . --strict