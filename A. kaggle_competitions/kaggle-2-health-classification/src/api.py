"""
FastAPI application for serving heart disease predictions.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import yaml

from src.models.predict import predict_single, load_config
from src.utils.logger import get_logger

logger = get_logger(__name__)

app = FastAPI(
    title="Heart Disease Prediction API",
    description="MLOps pipeline serving XGBoost predictions for heart disease detection.",
    version="1.0.0",
)

# Load config at startup
config = load_config()


class PatientFeatures(BaseModel):
    age: float = Field(..., example=55, description="Age in years")
    sex: int = Field(..., example=1, description="Sex (1=male, 0=female)")
    cp: int = Field(..., example=2, description="Chest pain type (0-3)")
    trestbps: float = Field(..., example=130, description="Resting blood pressure (mmHg)")
    chol: float = Field(..., example=245, description="Serum cholesterol (mg/dl)")
    fbs: int = Field(..., example=0, description="Fasting blood sugar > 120 mg/dl (1=true)")
    restecg: int = Field(..., example=1, description="Resting ECG results (0-2)")
    thalach: float = Field(..., example=160, description="Max heart rate achieved")
    exang: int = Field(..., example=0, description="Exercise-induced angina (1=yes)")
    oldpeak: float = Field(..., example=1.2, description="ST depression induced by exercise")
    slope: int = Field(..., example=2, description="Slope of peak exercise ST segment")
    ca: int = Field(..., example=0, description="Number of major vessels (0-3)")
    thal: int = Field(..., example=2, description="Thalassemia type")


class PredictionResponse(BaseModel):
    prediction: int
    probability: float
    label: str


@app.get("/", summary="Health check")
def root():
    return {"status": "ok", "message": "Heart Disease Prediction API is running"}


@app.get("/health", summary="Health check")
def health():
    return {"status": "healthy"}


@app.post("/predict", response_model=PredictionResponse, summary="Predict heart disease")
def predict(patient: PatientFeatures):
    """
    Takes patient clinical features and returns a heart disease prediction.
    """
    try:
        features = patient.model_dump()
        result = predict_single(features, config)
        logger.info(f"Prediction: {result}")
        return result
    except FileNotFoundError as e:
        raise HTTPException(status_code=503, detail=str(e))
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        raise HTTPException(status_code=500, detail="Internal prediction error")
