# LLM Classification Finetuning

Starter project for the Kaggle **LLM Classification Finetuning** competition.

This package trains a lightweight text baseline to predict:
- `winner_model_a`
- `winner_model_b`
- `winner_tie`

## Project structure

```text
kaggle-llm-classification-finetuning/
├── artifacts/
├── configs/
│   └── config.yaml
├── src/
│   ├── data/
│   │   ├── dataset.py
│   │   └── features.py
│   ├── models/
│   │   ├── baseline.py
│   │   └── predictor.py
│   ├── tests/
│   │   └── test_pipeline.py
│   ├── utils/
│   │   ├── io.py
│   │   ├── logger.py
│   │   └── seed.py
│   ├── __init__.py
│   ├── api.py
│   ├── train.py
│   └── predict.py
├── .gitignore
├── Dockerfile.serve
├── Dockerfile.train
├── Makefile
├── README.md
├── docker-compose.yml
├── dvc.yaml
├── pyproject.toml
├── requirements.txt
├── setup_env.ps1
└── submission.csv
```

## Expected data files
Place Kaggle data in `./data/raw/`:
- `train.csv`
- `test.csv`
- `sample_submission.csv`

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
make train
make predict
```

The trained model is saved in `artifacts/model.joblib` and predictions in `submission.csv`.

## Notes
This is a strong starter baseline, not a leaderboard-optimized solution. It uses TF-IDF features from prompt/response text and multinomial logistic regression.
