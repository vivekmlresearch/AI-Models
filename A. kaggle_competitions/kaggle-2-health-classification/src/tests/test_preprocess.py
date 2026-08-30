"""
Unit tests for the preprocessing module.
"""

import pytest
import pandas as pd
import numpy as np
from src.data.preprocess import clean_data, split_features_target


@pytest.fixture
def sample_config():
    return {
        "data": {
            "target_column": "target",
            "test_size": 0.2,
            "random_state": 42,
        },
        "features": {
            "numerical": ["age", "trestbps", "chol", "thalach", "oldpeak"],
            "categorical": ["sex", "cp", "fbs", "restecg", "exang", "slope", "ca", "thal"],
        },
    }


@pytest.fixture
def sample_df():
    """Minimal synthetic heart disease dataframe."""
    np.random.seed(42)
    n = 50
    return pd.DataFrame({
        "age": np.random.randint(30, 75, n).astype(float),
        "sex": np.random.randint(0, 2, n),
        "cp": np.random.randint(0, 4, n),
        "trestbps": np.random.randint(90, 180, n).astype(float),
        "chol": np.random.randint(150, 350, n).astype(float),
        "fbs": np.random.randint(0, 2, n),
        "restecg": np.random.randint(0, 3, n),
        "thalach": np.random.randint(80, 200, n).astype(float),
        "exang": np.random.randint(0, 2, n),
        "oldpeak": np.random.uniform(0, 5, n),
        "slope": np.random.randint(0, 3, n),
        "ca": np.random.randint(0, 4, n),
        "thal": np.random.randint(0, 3, n),
        "target": np.random.randint(0, 5, n),  # UCI raw: 0-4
    })


def test_clean_data_no_nulls(sample_df, sample_config):
    cleaned = clean_data(sample_df, sample_config)
    assert cleaned.isnull().sum().sum() == 0, "No nulls should remain after cleaning"


def test_target_binarization(sample_df, sample_config):
    cleaned = clean_data(sample_df, sample_config)
    unique_targets = cleaned["target"].unique()
    assert set(unique_targets).issubset({0, 1}), "Target must be binarized to 0/1"


def test_no_duplicates(sample_df, sample_config):
    cleaned = clean_data(sample_df, sample_config)
    assert cleaned.duplicated().sum() == 0, "No duplicates should remain"


def test_split_features_target_shape(sample_df, sample_config):
    cleaned = clean_data(sample_df, sample_config)
    X, y = split_features_target(cleaned, sample_config)
    assert "target" not in X.columns, "Target column should not be in features"
    assert len(X) == len(y), "X and y must have the same number of rows"


def test_split_features_target_columns(sample_df, sample_config):
    cleaned = clean_data(sample_df, sample_config)
    X, y = split_features_target(cleaned, sample_config)
    expected_features = [c for c in cleaned.columns if c != "target"]
    assert list(X.columns) == expected_features
