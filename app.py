from fastapi import FastAPI
from pydantic import BaseModel
from skin_hair_agent import diagnose

app = FastAPI(
    title="Skin & Hair Diagnosis AI",
    description="Simple AI-based API to analyze skin and hair problems",
    version="1.0"
)

class RequestIn(BaseModel):
    topic: str
    symptom: str

@app.get("/")
def home():
    return {"message": "API is Running Successfully!"}

@app.post("/analyze")
def analyze(req: RequestIn):
    print(">> /analyze called with:", req.dict())
    result = diagnose(req.topic, req.symptom)
    print(">> result:", result)
    return result

