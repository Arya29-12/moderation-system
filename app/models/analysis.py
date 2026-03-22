from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class AnalysisResult(BaseModel):
    text: str
    toxicity_score: float
    label: str
    risk: str
    explanation: Optional[List[Dict[str, Any]]] = []
  