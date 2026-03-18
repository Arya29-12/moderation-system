from fastapi import APIRouter
from app.models.user import User

router = APIRouter()

@router.post("/Users")
def create_user(user: User):
    return {"Message":"User created", "data":user}