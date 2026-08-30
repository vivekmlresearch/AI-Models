"""
Unit tests for model training and evaluation.
"""

# import pytest
import numpy as np
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from src.models.evaluate import compute_metrics


@pytest.fixture
def binary_classification_data():
    X, y = make_classification(
        n_samples=200,
        n_features=13,
        n_informative=8,
        n_classes=2,
        random_state=42,
    )
    split = int(0.8 * len(X))
    return X[:split], X[split:], y[:split], y[split:]


@pytest.fixture
def trained_model(binary_classification_data):
    X_train, _, y_train, _ = binary_classification_data
    model = RandomForestClassifier(n_estimators=10, random_state=42)
    model.fit(X_train, y_train)
    return model


def test_metrics_keys(trained_model, binary_classification_data):
    _, X_test, _, y_test = binary_classification_data
    metrics = compute_metrics(trained_model, X_test, y_test)
    expected_keys = {"accuracy", "f1_score", "roc_auc", "precision", "recall"}
    assert expected_keys == set(metrics.keys()), "All expected metrics should be present"


def test_metrics_in_valid_range(trained_model, binary_classification_data):
    _, X_test, _, y_test = binary_classification_data
    metrics = compute_metrics(trained_model, X_test, y_test)
    for name, value in metrics.items():
        assert 0.0 <= value <= 1.0, f"Metric {name} = {value} is out of [0, 1] range"


def test_model_predictions_shape(trained_model, binary_classification_data):
    _, X_test, _, y_test = binary_classification_data
    preds = trained_model.predict(X_test)
    assert preds.shape == y_test.shape, "Predictions shape must match y_test"


def test_model_predictions_binary(trained_model, binary_classification_data):
    _, X_test, _, _ = binary_classification_data
    preds = trained_model.predict(X_test)
    assert set(preds).issubset({0, 1}), "Predictions must be binary (0 or 1)"


def test_model_predict_proba_range(trained_model, binary_classification_data):
    _, X_test, _, _ = binary_classification_data
    probas = trained_model.predict_proba(X_test)[:, 1]
    assert np.all(probas >= 0) and np.all(probas <= 1), "Probabilities must be in [0, 1]"
