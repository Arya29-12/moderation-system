from app.services.tfidf_service import pipeline
import shap

def predict_proba(texts):
    probs = pipeline.predict_proba(texts)
    classes = list(pipeline.classes_)

    if "toxic" in classes:
        toxic_index = classes.index("toxic")
    elif "hate/toxic" in classes:
     toxic_index = classes.index("hate/toxic")
    else:
        raise ValueError(f"No toxic class found in {classes}")
    return probs[:, toxic_index]

class ShapExplainer:
    def __init__(self):
        self.explainer = shap.Explainer(predict_proba, shap.maskers.Text())

    def explain(self, text: str):
        shap_values = self.explainer([text])

        values = shap_values.values[0]
        words = shap_values.data[0]

        explanation = []

        for word, val in zip(words, values):
            explanation.append({
                "word": word,
                "impact": float(val)
            })

        explanation = sorted(
            explanation,
            key=lambda x: abs(x["impact"]),
            reverse=True
        )

        return explanation[:2]