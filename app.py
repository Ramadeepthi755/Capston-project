# app.py
import os
from pathlib import Path
import pickle
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

BASE = Path(__file__).resolve().parent
MODEL_PATH = BASE / "models" / "pipeline.pkl"

app = FastAPI(title="Skin & Hair Diagnosis API")

class DiagnoseRequest(BaseModel):
    topic: str
    symptom: str

class Prediction(BaseModel):
    label: str
    score: float

class DiagnoseResponse(BaseModel):
    topic: str
    symptom: str
    predictions: List[Prediction]

# load model at startup
if not MODEL_PATH.exists():
    raise RuntimeError(f"Model not found at {MODEL_PATH}. Run train_model.py first.")

with open(MODEL_PATH, "rb") as f:
    pipeline = pickle.load(f)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/diagnose", response_model=DiagnoseResponse)
def diagnose(req: DiagnoseRequest):
    text = f"{req.topic} | {req.symptom}"
    try:
        probs = pipeline.predict_proba([text])[0]  # shape (n_classes,)
        classes = pipeline.classes_
        # top 3
        top_idx = probs.argsort()[::-1][:3]
        preds = [{"label": classes[i], "score": float(probs[i])} for i in top_idx]
        return {"topic": req.topic, "symptom": req.symptom, "predictions": preds}
    except AttributeError:
        # If model does not support predict_proba, return single prediction
        pred = pipeline.predict([text])[0]
        return {"topic": req.topic, "symptom": req.symptom, "predictions": [{"label": pred, "score": 1.0}]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
