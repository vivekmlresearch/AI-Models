# Health Classification MLOps Pipeline

![CI](https://github.com/YOUR_USERNAME/heart-disease-mlops/actions/workflows/ci.yaml/badge.svg)
![Python](https://img.shields.io/badge/python-3.11-blue)
![MLflow](https://img.shields.io/badge/tracking-MLflow-orange)
![DVC](https://img.shields.io/badge/data-DVC-purple)
![Docker](https://img.shields.io/badge/deploy-Docker-2496ED)

> End-to-end MLOps pipeline for predicting heart disease using the UCI Heart Disease dataset — featuring experiment tracking, data versioning, CI/CD, and REST API serving.

---

## Architecture

```
Raw Data (DVC) → Preprocessing → Model Training (MLflow) → Registry → FastAPI → Docker
                                        ↑
                               GitHub Actions CI/CD
```

---

## Project Structure

```
heart-disease-mlops/
├── data/
│   ├── raw/                  # Original CSV (versioned via DVC)
│   └── processed/            # Cleaned/transformed data
├── notebooks/
│   └── 01_EDA.ipynb          # Exploratory analysis
├── src/
│   ├── data/
│   │   ├── ingest.py         # Data loading
│   │   └── preprocess.py     # Feature engineering & scaling
│   ├── models/
│   │   ├── train.py          # Training with MLflow logging
│   │   ├── evaluate.py       # Metrics computation
│   │   └── predict.py        # Inference
│   └── utils/
│       └── logger.py         # Centralized logging
├── tests/                    # pytest unit tests
├── configs/
│   └── config.yaml           # All hyperparams & paths
├── .github/workflows/
│   └── ci.yaml               # GitHub Actions CI/CD
├── Dockerfile
├── docker-compose.yml
├── dvc.yaml                  # DVC pipeline
├── Makefile
└── requirements.txt
```

---

## Quick Start

### 1. Clone & Install
```bash
git clone https://github.com/YOUR_USERNAME/heart-disease-mlops.git
cd heart-disease-mlops
pip install -r requirements.txt
```

### 2. Pull Data (DVC)
```bash
dvc pull
```

### 3. Run Full Pipeline
```bash
make all
# or step by step:
make preprocess
make train
make evaluate
```

### 4. Launch MLflow UI
```bash
mlflow ui
# Open http://localhost:5000
```

### 5. Serve Predictions (FastAPI)
```bash
make serve
# Open http://localhost:8000/docs
```

### 6. Run with Docker
```bash
docker compose up
```

---

## Results


<img width="1435" height="111" alt="image" src="https://github.com/user-attachments/assets/53be7380-3ec7-4b5e-96cb-6cfc04c6f002" />


## For Multi-Model Comparisions:- 


| Model | ROC-AUC | F1 Score | Accuracy |
|---|---|---|---|
| LightGBM | 0.6966 | tba | tba |
| Logistic Regression | tba | tba | tba |
| Random Forest | tba | tba | tba |

---

## 🛠️ MLOps Components

| Component | Tool | Purpose |
|---|---|---|
| Data Versioning | DVC | Reproducible datasets |
| Experiment Tracking | MLflow | Log params, metrics, artifacts |
| Config Management | YAML + Hydra-style | No hardcoded values |
| Testing | pytest | Schema, preprocessing, model tests |
| CI/CD | GitHub Actions | Lint + test on every push |
| Serving | FastAPI | REST API for predictions |
| Containerization | Docker | Portable deployment |

---

## API Usage

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "age": 55, "sex": 1, "cp": 2, "trestbps": 130,
    "chol": 245, "fbs": 0, "restecg": 1, "thalach": 160,
    "exang": 0, "oldpeak": 1.2, "slope": 2, "ca": 0, "thal": 2
  }'
```

Response:
```json
{"prediction": 1, "probability": 0.82, "label": "Heart Disease Detected"}
```

---

## Running Tests
```bash
make test
```

---

## Data Source
Kaggle - 14 clinical features across 920 ids from 4 institutions.

## License

This project is released under the MIT License. The competition dataset is provided by Kaggle under: Attribution 4.0 International (CC BY 4.0)

---

