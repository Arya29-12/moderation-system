from app.services.tfidf_service import tfidf_predict
from app.services.transformer_service import transformer_predict

def analyse_text(text: str):
    
    tfidf_result = tfidf_predict(text)

    if tfidf_result["confidence"] > 0.75:
        result = tfidf_result
    else:
        result = transformer_predict(text)

    # default label
    final_label = result["label"]

    # confidence threshold
    if result["confidence"] < 0.6:
        final_label = "normal"

    print(f"[ANALYSIS] text='{text[:50]}...' label={final_label} conf={result['confidence']:.3f}")

    analysis = {
        "label": final_label,
        "confidence": result["confidence"]
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