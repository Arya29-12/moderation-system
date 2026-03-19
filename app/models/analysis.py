from pydantic import BaseModel

class AnalysisResult(BaseModel):
    text: str
    toxicity_score: float
    label: str