from fastapi import APIRouter, HTTPException

#from pymongo.errors import DuplicateKeyError

#from app.models.user import User,UserCreate
#from app.db import db

#from datetime import datetime,timezone

router = APIRouter()

@router.post("/users")
def get_users():
    return {"message" : "ok"}

'''
def create_user(user: UserCreate):

    user_dict = user.model_dump()
    user_dict["created_at"] = datetime.now(timezone.utc)
    user_dict.update({
    "avg_toxicity": 0.0,
    "total_posts": 0,
    "recent_scores": [],
    "recent_avg": 0.0,
    "last_spike": False
    })

    try:
        result = db.users_collection.insert_one(user_dict)
    except DuplicateKeyError:
        raise HTTPException(status_code=409, detail="Email already exists")
    return {
        "message":"User created", 
        "user_id": str(result.inserted_id)
        }
'''