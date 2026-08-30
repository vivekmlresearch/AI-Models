from __future__ import annotations

import pandas as pd

from src.data.features import build_text
from src.utils.io import load_joblib


class Predictor:
    def __init__(self, model_path: str):
        self.model = load_joblib(model_path)

    def predict_proba(self, df: pd.DataFrame):
        text = build_text(df)
        return self.model.predict_proba(text)
