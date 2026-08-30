from __future__ import annotations

from typing import List

import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

from src.models.predictor import Predictor

MODEL_PATH = "artifacts/model.joblib"
app = FastAPI(title="LLM Preference Predictor")


class RequestRow(BaseModel):
    id: int
    prompt: str
    response_a: str
    response_b: str


class PredictRequest(BaseModel):
    rows: List[RequestRow]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(request: PredictRequest):
    predictor = Predictor(MODEL_PATH)
    df = pd.DataFrame([row.model_dump() for row in request.rows])
    probs = predictor.predict_proba(df)

    results = []
    for row_id, prob in zip(df["id"].tolist(), probs):
        results.append(
            {
                "id": row_id,
                "winner_model_a": float(prob[0]),
                "winner_model_b": float(prob[1]),
                "winner_tie": float(prob[2]),
            }
        )
    return {"predictions": results}
