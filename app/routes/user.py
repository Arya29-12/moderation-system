from fastapi import APIRouter, HTTPException

from pymongo.errors import DuplicateKeyError

from app.models.user import User
from app.db.collections import users_collection

from datetime import datetime,timezone

router = APIRouter()

@router.post("/users")
def create_user(user: User):

    user_dict = user.model_dump()
    user_dict["created_at"] = datetime.now(timezone.utc)

    try:
        result = users_collection.insert_one(user_dict)
    except DuplicateKeyError:
        raise HTTPException(status_code=409, detail="Email already exists")
    return {
        "message":"User created", 
        "user_id": str(result.inserted_id)
        }