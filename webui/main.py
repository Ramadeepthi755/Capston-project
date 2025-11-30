# webui/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
import os, sys

# allow parent folder imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

try:
    from skin_hair_agent import diagnose    # your function
except Exception as e:
    # fallback stub if import fails
    def diagnose(topic, symptom):
        return {"error": "import failed", "detail": str(e)}

class Input(BaseModel):
    topic: str
    symptom: str

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def root():
    p = os.path.join(os.path.dirname(__file__), "static", "index.html")
    if os.path.exists(p):
        return open(p, "r", encoding="utf-8").read()
    return "<h1>Index not found</h1>"

@app.post("/api/diagnose")
def api_diagnose(data: Input):
    try:
        out = diagnose(data.topic, data.symptom)
        return {"result": out}
    except Exception as e:
        return {"error": str(e)}
