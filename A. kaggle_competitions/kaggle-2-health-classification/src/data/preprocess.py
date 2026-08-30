"""
Preprocessing module: handles cleaning, feature engineering, and train/test splitting.
"""

import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
import yaml

from src.utils.logger import get_logger

logger = get_logger(__name__)


def load_config(config_path: str = "configs/config.yaml") -> dict:
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


def clean_data(df: pd.DataFrame, config: dict) -> pd.DataFrame:
    """
    Clean raw dataframe:
    - Drop duplicates
    - Handle missing values
    - Binarize target column
    """
    logger.info(f"Shape before cleaning: {df.shape}")
    df = df.drop_duplicates()

    target_col = config["data"]["target_column"]

    # UCI target: 0 = no disease, 1-4 = disease → binarize to 0/1
    if df[target_col].max() > 1:
        logger.info("Binarizing target column (0 = healthy, 1 = disease)")
        df[target_col] = (df[target_col] > 0).astype(int)

    # Drop rows with too many nulls (>50% missing)
    threshold = len(df.columns) * 0.5
    df = df.dropna(thresh=threshold)

    # Fill remaining nulls with median for numeric
    num_cols = df.select_dtypes(include=[np.number]).columns
    df[num_cols] = df[num_cols].fillna(df[num_cols].median())

    logger.info(f"Shape after cleaning: {df.shape}")
    return df


def split_features_target(df: pd.DataFrame, config: dict):
    target_col = config["data"]["target_column"]
    X = df.drop(columns=[target_col])
    y = df[target_col]
    return X, y


def scale_features(X_train: pd.DataFrame, X_test: pd.DataFrame, config: dict):
    """
    Fit scaler on training data, transform both splits.
    Saves scaler artifact for use in serving.
    """
    numerical_cols = config["features"]["numerical"]
    scaler = StandardScaler()

    X_train = X_train.copy()
    X_test = X_test.copy()

    X_train[numerical_cols] = scaler.fit_transform(X_train[numerical_cols])
    X_test[numerical_cols] = scaler.transform(X_test[numerical_cols])

    # Persist scaler
    scaler_path = Path("models/scaler.pkl")
    scaler_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(scaler, scaler_path)
    logger.info(f"Scaler saved to {scaler_path}")

    return X_train, X_test, scaler


def run_preprocessing(config: dict):
    """Full preprocessing pipeline."""
    from src.data.ingest import load_raw_data

    df = load_raw_data(config)
    df = clean_data(df, config)

    X, y = split_features_target(df, config)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=config["data"]["test_size"],
        random_state=config["data"]["random_state"],
        stratify=y,
    )

    X_train, X_test, _ = scale_features(X_train, X_test, config)

    # Save processed data
    processed_path = Path(config["data"]["processed_path"])
    processed_path.parent.mkdir(parents=True, exist_ok=True)
    processed = pd.concat([X_train, y_train], axis=1)
    processed.to_csv(processed_path, index=False)
    logger.info(f"Processed data saved to {processed_path}")

    logger.info(f"Train size: {X_train.shape}, Test size: {X_test.shape}")
    return X_train, X_test, y_train, y_test


if __name__ == "__main__":
    config = load_config()
    run_preprocessing(config)
