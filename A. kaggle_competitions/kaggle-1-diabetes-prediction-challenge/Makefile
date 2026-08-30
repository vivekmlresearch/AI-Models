.PHONY: all install preprocess train evaluate test lint serve docker-build docker-up clean

## Install all dependencies
install:
	pip install -r requirements.txt

## Run full pipeline: preprocess → train → evaluate
all: preprocess train evaluate

## Preprocess data
preprocess:
	python -m src.data.preprocess

## Train model with MLflow tracking
train:
	python -m src.models.train

## Evaluate and generate reports
evaluate:
	python -m src.models.evaluate

## Launch FastAPI server (development)
serve:
	uvicorn src.api:app --host 0.0.0.0 --port 8000 --reload

## Run all tests
test:
	pytest tests/ -v --tb=short

## Lint code
lint:
	ruff check src/ tests/

## Format code
format:
	ruff format src/ tests/

## Open MLflow UI
mlflow-ui:
	mlflow ui --backend-store-uri mlruns

## Build Docker image
docker-build:
	docker build -t heart-disease-mlops:latest .

## Start all services with Docker Compose
docker-up:
	docker compose up --build

## Stop Docker services
docker-down:
	docker compose down

## Clean generated artifacts
clean:
	rm -rf models/ data/processed/ reports/ mlruns/ __pycache__ .pytest_cache
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -type d -exec rm -rf {} +

## DVC: run full tracked pipeline
dvc-run:
	dvc repro

## Help
help:
	@grep -E '^## ' Makefile | sed 's/## //'
