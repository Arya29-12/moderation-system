from app.services.tfidf_service import tfidf_predict
from app.services.explain import ShapExplainer

explainer = None

def get_explainer():
    global explainer
    if explainer is None:
        explainer = ShapExplainer()
    return explainer


def analyse_text(text: str):
    text = text[:512]

    tfidf_result = tfidf_predict(text)
    result = tfidf_result  # default fallback

    if tfidf_result["confidence"] < 0.75:
        try:
            from app.services.transformer_service import transformer_predict
            result = transformer_predict(text)
        except Exception:
            result = tfidf_result

    final_label = result["label"]
    confidence = result["confidence"]

    if confidence < 0.6:
        final_label = "normal"

    explanation = None
    if confidence < 0.8:
        explanation = get_explainer().explain(text)

    toxicity_score = confidence if final_label == "toxic" else 0.0

    analysis = {
        "label": final_label,
        "confidence": confidence,
        "toxicity_score": toxicity_score,
        "explanation": explanation,
        "risk": get_risk_level(final_label, confidence)
    }

    return analysis


def get_risk_level(label: str, confidence: float):

    if label == "self-harm":
        return "critical" if confidence > 0.7 else "high"

    if label == "toxic":
        return "high" if confidence > 0.75 else "medium"

    if label == "sexual":
        return "medium" if confidence > 0.85 else "low"

    return "low"