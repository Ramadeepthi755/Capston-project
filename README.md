# Capstone: Skin & Hair Diagnosis AI (Local)

## Description
Simple FastAPI app that analyses skin/hair symptoms and returns recommendations.

## How to run (local)
1. python -m venv venv  
2. Activate venv  
3. pip install -r requirements.txt  
4. uvicorn app:app --reload --port 8000  
5. Open http://127.0.0.1:8000/docs

## Endpoints
- POST /analyze  
  Input: { "topic": "skin", "symptom": "dry" }  
  Output: { "diagnosis": "...", "recommendations": ["..."], "explanation": "..." }

## 🧠 Features  
- Skin problem detection  
- Hair problem detection  
- Rule-based AI  
- Clear recommendations  

## 🔗 Notebook  
https://www.kaggle.com/code/ramadeepthibadireddy/skin-hair-diagnosis-ai

## Notes
This project uses local rule-based agent. For production, replace with Google Gemini / Vertex integration.
