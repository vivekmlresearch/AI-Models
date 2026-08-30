from __future__ import annotations

from pathlib import Path
import pandas as pd

TARGET_COLUMNS = ["winner_model_a", "winner_model_b", "winner_tie"]
CLASS_NAMES = ["model_a", "model_b", "tie"]


def read_csv(path: str) -> pd.DataFrame:
    csv_path = Path(path)
    if not csv_path.exists():
        raise FileNotFoundError(f"Missing file: {csv_path}")
    return pd.read_csv(csv_path)


def get_targets(df: pd.DataFrame):
    if not set(TARGET_COLUMNS).issubset(df.columns):
        raise ValueError("Training data must contain winner target columns.")
    y = df[TARGET_COLUMNS].values.argmax(axis=1)
    return y
