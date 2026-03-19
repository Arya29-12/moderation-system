from fastapi import APIRouter
from app.models.user import User
from app.db.collections import users_collection

router = APIRouter()

@router.post("/users")
def create_user(user: User):
    user_dict = user.model_dump()
    result = users_collection.insert_one(user_dict)
    return {
        "message":"User created", 
        "user_id": str(result.inserted_id)
        }