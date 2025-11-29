def diagnose(topic, symptom):
    topic = topic.lower().strip()
    symptom = symptom.lower().strip()

    # SKIN CONDITIONS
    if topic == "skin" and symptom == "dry":
        return {
            "diagnosis": "Dry skin",
            "recommendations": [
                "Use a good moisturizer twice daily",
                "Drink 3–4 liters of water daily",
                "Avoid hot showers and harsh soaps"
            ],
            "explanation": "Skin dryness occurs when your skin loses moisture."
        }

    if topic == "skin" and symptom == "oily":
        return {
            "diagnosis": "Oily skin",
            "recommendations": [
                "Use oil-free moisturizer",
                "Wash face 2–3 times daily",
                "Avoid heavy makeup"
            ],
            "explanation": "Oily skin happens due to excess sebum production."
        }

    if topic == "skin" and symptom == "acne":
        return {
            "diagnosis": "Acne / Pimples",
            "recommendations": [
                "Use salicylic acid face wash",
                "Don’t touch or pop pimples",
                "Use non-comedogenic products"
            ],
            "explanation": "Acne is caused by clogged pores, bacteria, and oil."
        }

    # HAIR CONDITIONS
    if topic == "hair" and symptom == "dandruff":
        return {
            "diagnosis": "Dandruff",
            "recommendations": [
                "Use anti-dandruff shampoo 2 times a week",
                "Avoid oily hair products",
                "Keep scalp clean and dry"
            ],
            "explanation": "Dandruff happens due to fungus or dry scalp."
        }

    if topic == "hair" and symptom == "hairfall":
        return {
            "diagnosis": "Hair fall",
            "recommendations": [
                "Oil scalp 2 times a week",
                "Use sulfate-free shampoo",
                "Reduce heat styling"
            ],
            "explanation": "Hair fall is due to stress, dryness, or weak roots."
        }

    # UNKNOWN CASE
    return {
        "diagnosis": "Symptom not recognized",
        "recommendations": [
            "Try another symptom",
            "Or consult a dermatologist/hair specialist"
        ],
        "explanation": ""
    }
if __name__ == '__main__': app.run(debug=True,port=8000)