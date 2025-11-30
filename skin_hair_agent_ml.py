# skin_hair_agent_ml.py
import pickle
import os

MODEL_DIR = "models"

model = pickle.load(open(os.path.join(MODEL_DIR, "model.pkl"), "rb"))
le_topic = pickle.load(open(os.path.join(MODEL_DIR, "topic_encoder.pkl"), "rb"))
le_symptom = pickle.load(open(os.path.join(MODEL_DIR, "symptom_encoder.pkl"), "rb"))
le_condition = pickle.load(open(os.path.join(MODEL_DIR, "condition_encoder.pkl"), "rb"))

RECOMMENDATIONS = {
    "Dry Skin": "Apply moisturizer twice a day and drink more water",
    "Acne": "Use salicylic acid cleanser and consult dermatologist if severe",
    "Oily Skin": "Use oil-free, gel based moisturizers; wash face twice a day",
    "Contact Dermatitis": "Avoid triggers and see a doctor for topical steroid",
    "Rosacea": "Use gentle skincare and consult dermatologist",
    "Dandruff": "Use anti-dandruff shampoo (e.g., ketoconazole)",
    "Hair Fall": "Avoid harsh treatments; consult dermatologist for tests",
    "Dry Scalp": "Oil massage weekly and use moisturizing shampoos",
    "Scalp Allergy": "Use mild herbal shampoo and avoid irritants"
}

def diagnose(topic: str, symptom: str):
    topic = (topic or "").strip().lower()
    symptom = (symptom or "").strip().lower()
    try:
        t = le_topic.transform([topic])[0]
        s = le_symptom.transform([symptom])[0]
    except Exception:
        return {"error": "Unknown topic or symptom. Please use valid values."}

    pred = model.predict([[t, s]])[0]
    condition = le_condition.inverse_transform([pred])[0]
    recommendation = RECOMMENDATIONS.get(condition, "No recommendation available")

    return {
        "condition": condition,
        "recommendation": recommendation
    }
