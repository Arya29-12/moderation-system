from app.services.tfidf_service import tfidf_predict
from app.services.transformer_service import transformer_predict

def analyse_text(text: str):
    
    tfidf_result = tfidf_predict(text)

    if tfidf_result["confidence"] > 0.75:
        result = tfidf_result
    else:
        result = transformer_predict(text)

    if result["confidence"] < 0.6:
        final_label = "normal"

    print(f"[ANALYSIS] text='{text[:50]}...' label={result['label']} conf={result['confidence']:.3f}")
    
    return result