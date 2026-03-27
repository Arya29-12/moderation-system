classifier = None

label_map = {"TOXIC": "toxic","INSULT": "toxic","OBSCENE": "sexual","THREAT": "self-harm","IDENTITY_HATE": "toxic"}

def get_classifier():
    global classifier
    if classifier is None:
        from transformers import pipeline
        classifier = pipeline(
            "text-classification",
            model="unitary/toxic-bert",
            truncation=True
        )
    return classifier

def transformer_predict(text: str):

    result = classifier(text)[0]
    raw_label = result["label"]
    confidence = float(result["score"])

    return {
        "label": label_map.get(raw_label, "normal"),
        "confidence": confidence
    }