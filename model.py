# train_model.py
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import pickle

BASE_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_DIR, "data", "dataset.csv")
MODEL_DIR = os.path.join(BASE_DIR, "models")
os.makedirs(MODEL_DIR, exist_ok=True)
MODEL_PATH = os.path.join(MODEL_DIR, "pipeline.pkl")

def load_data(path):
    df = pd.read_csv(path)
    # Expect columns: topic, symptom, label
    df = df.dropna(subset=["topic","symptom","label"])
    # combine topic+symptom into a single text
    df["text"] = df["topic"].astype(str) + " | " + df["symptom"].astype(str)
    return df

def train():
    df = load_data(DATA_PATH)
    X = df["text"]
    y = df["label"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    pipeline = Pipeline([
        ("vect", CountVectorizer(ngram_range=(1,2), max_features=5000)),
        ("tfidf", TfidfTransformer()),
        ("clf", LogisticRegression(max_iter=1000))
    ])
    pipeline.fit(X_train, y_train)
    preds = pipeline.predict(X_test)
    probs = pipeline.predict_proba(X_test) if hasattr(pipeline, "predict_proba") else None
    acc = accuracy_score(y_test, preds)
    print("Test accuracy:", acc)
    print(classification_report(y_test, preds))
    # save pipeline
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(pipeline, f)
    print("Saved model to", MODEL_PATH)

if __name__ == "__main__":
    train()
