# Makefile for Python project using Poetry and Pytest

# .PHONY is used to specify targets that are not filenames
.PHONY: help install test lint format clean

.DEFAULT_GOAL := help

# Specify the shell used by Make
SHELL = /bin/bash

# Define colors for pretty printing
RED = \033[0;31m
GREEN = \033[0;32m
YELLOW = \033[0;33m
NC = \033[0m # No Color

##@ General

help:  ## Display this help message
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

##@ Development

install:  ## Install project dependencies
	@echo -e "$(YELLOW)Installing dependencies...$(NC)"
	@poetry install

test:  ## Run tests
	@echo -e "$(YELLOW)Running tests...$(NC)"
	@poetry run pytest

#lint:  ## Lint the codebase
#	@echo -e "$(YELLOW)Linting code...$(NC)"
#	@poetry run flake8

format:  ## Format the codebase
	@echo -e "$(YELLOW)Formatting code...$(NC)"
	@poetry run black .

##@ Cleanup

clean:  ## Clean up Python file artifacts
	@echo -e "$(YELLOW)Cleaning up...$(NC)"
	@find . -type d -name "__pycache__" -exec rm -r {} +
	@find . -type d -name ".pytest_cache" -exec rm -r {} +
	@echo -e "$(GREEN)Cleanup complete!$(NC)"

##@ Deploy

# Build the project
build: clean test
	@echo "Building the project..."
	poetry build

# Build the documentation
#docs:
#	@echo "Building documentation..."
#	cd docs && poetry run make html

# Publish the package to PyPI
publish:
	@echo "Publishing to PyPI..."
	poetry publish --build


