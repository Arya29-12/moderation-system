import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "models", "pipeline.pkl")

import pickle

with open(model_path, "rb") as f:
    pipeline = pickle.load(f)

def tfidf_predict(text: str):
    probs = pipeline.predict_proba([text])[0]
    classes = pipeline.classes_

    idx = probs.argmax()
    label = classes[idx]
    confidence = float(probs[idx])

    return {
        "label": label,
        "confidence": confidence
    }