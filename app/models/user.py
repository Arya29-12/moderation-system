from pydantic import BaseModel
from pydantic import Field

class User(BaseModel):
    name: str
    email:str
    avg_toxicity: float = 0.0
    total_posts: int = 0
    recent_scores: list[float] = Field(default_factory=list)
    recent_avg: float = 0.0

class UserCreate(BaseModel):
    name: str
    email: str