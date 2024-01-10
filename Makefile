.PHONY: setup format notebooks clean

# Set the shell to bash in case some bash-specific syntax is used.
SHELL := /usr/bin/bash

# The default target of the makefile. It sets up the project environment.
all: format clean

# Set up the Python environment
setup:
	@echo "Setting up the Python environment..."
	python3 -m venv .venv
	source .venv/bin/activate
	pip install -r requirements.txt

# Clean and format Python code using Ruff and isort
format:
	@echo "Cleaning and formatting Python scripts..."
	isort **/*/*.py
	ruff format **/*/*.py

# Convert Jupyter notebooks to Python scripts and vice versa
notebooks:
	@echo "Converting Jupyter notebooks..."
	jupyter nbconvert --to script *.ipynb
	jupyter nbconvert --to notebook *.

# Run tests with Pytest and Hypothesis
test:
	@echo "Running tests..."
	python3 -m pytest tests

# Clean up the environment
clean:
	@echo "Cleaning up..."
	find . -type f -name '*.pyc' | xargs rm -rf
	find . -type d -name '__pycache__' | xargs rm -rf
	find . -type d -name '.ruff_cache' | xargs rm -rf
