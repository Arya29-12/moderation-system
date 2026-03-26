from app.services.tfidf_service import tfidf_predict
#from app.services.transformer_service import transformer_predict
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

    explanation = None

    if result["confidence"] < 0.8:
        explanation = get_explainer().explain(text)
    
    conf = tfidf_result["confidence"]

    if conf >= 0.75 or conf <= 0.4:
        result = tfidf_result
    else:
        try:
            result = transformer_predict(text)
        except Exception:
            result = tfidf_result

    final_label = result["label"]

    if result["confidence"] < 0.6:
        final_label = "normal"

    toxicity_score = result["confidence"] if final_label == "toxic" else 0.0
    analysis = { 
    "label": final_label,
    "confidence": result["confidence"],
    "toxicity_score": toxicity_score,
    "explanation": explanation
    }

    risk = get_risk_level(final_label, result["confidence"])
    analysis["risk"] = risk

    return analysis


def get_risk_level(label: str, confidence: float):

    if label == "self-harm":
        if confidence > 0.7:
            return "critical"
        return "high"

    if label == "toxic":
        if confidence > 0.75:
            return "high"
        return "medium"

    if label == "sexual":
        if confidence > 0.85:
            return "medium"
        return "low"

    return "low"