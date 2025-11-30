# evaluate.py
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report
import pickle

df = pd.read_csv("dataset.csv")
df['topic'] = df['topic'].str.strip().str.lower()
df['symptom'] = df['symptom'].str.strip().str.lower()

le_topic = pickle.load(open("models/topic_encoder.pkl","rb"))
le_symptom = pickle.load(open("models/symptom_encoder.pkl","rb"))
le_condition = pickle.load(open("models/condition_encoder.pkl","rb"))
model = pickle.load(open("models/model.pkl","rb"))

X = df[['topic','symptom']]
X_enc = pd.DataFrame({
    "topic_enc": le_topic.transform(df['topic']),
    "symptom_enc": le_symptom.transform(df['symptom'])
})

pred = model.predict(X_enc)
y_true = le_condition.transform(df['condition'])

print(classification_report(y_true, pred, target_names=le_condition.classes_))
