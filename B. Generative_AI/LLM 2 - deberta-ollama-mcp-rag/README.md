# LLM Classification Finetuning - DeBERTa v3 Base

This project trains a `microsoft/deberta-v3-base` sequence-classification model for the Kaggle competition.

And then can be fed into LLM, MCP and RAG.

## Windows PowerShell setup

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Train

```powershell
python -m src.train --config configs/config.yaml
```

## Predict:-

```powershell
python -m src.predict --config configs/config.yaml
```

## Outputs:-

- Fine-tuned model: `artifacts/deberta_v3_base/`
- Metrics: `artifacts/metrics.yaml`

## Notes

- `max_length: 1024` is memory-heavy. If your GPU/CPU RAM is limited, reduce it to `512` in `configs/config.yaml`.
- The default config uses `train_batch_size: 2` and gradient accumulation to fit more easily on smaller GPUs.
