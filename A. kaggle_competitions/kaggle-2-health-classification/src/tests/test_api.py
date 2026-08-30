"""
API endpoint tests using FastAPI TestClient.
"""

import pytest
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)

SAMPLE_PATIENT = {
    "age": 55, "sex": 1, "cp": 2, "trestbps": 130,
    "chol": 245, "fbs": 0, "restecg": 1, "thalach": 160,
    "exang": 0, "oldpeak": 1.2, "slope": 2, "ca": 0, "thal": 2,
}


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "status" in response.json()


@patch("src.api.predict_single")
def test_predict_endpoint(mock_predict):
    mock_predict.return_value = {
        "prediction": 1,
        "probability": 0.82,
        "label": "Heart Disease Detected",
    }
    response = client.post("/predict", json=SAMPLE_PATIENT)
    assert response.status_code == 200
    data = response.json()
    assert "prediction" in data
    assert "probability" in data
    assert "label" in data
    assert data["prediction"] in [0, 1]
    assert 0 <= data["probability"] <= 1


def test_predict_invalid_input():
    response = client.post("/predict", json={"age": "not_a_number"})
    assert response.status_code == 422  # Unprocessable entity
