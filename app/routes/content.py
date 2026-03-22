from fastapi import APIRouter
from fastapi import HTTPException

from datetime import datetime,timezone

from bson import ObjectId
from bson.errors import InvalidId

from app.models.content import Content
from app.models.analysis import AnalysisResult
from app.db.collections import content_collection, users_collection

from app.services.analysis import analyse_text

router = APIRouter()

@router.post("/content", response_model = AnalysisResult)
def submit_content(content: Content):

    try:
        obj_user_id = ObjectId(content.user_id)
    except Exception:
        raise HTTPException(status_code=400, detail = "Invalid user ID format")
    
    user = users_collection.find_one({"_id": obj_user_id})

    if not user:
        raise HTTPException (status_code=404, detail= "User not found")
    
    content_dict = content.model_dump()
    content_dict["user_id"] = obj_user_id
    content_dict["created_at"] = datetime.now(timezone.utc)
    content_collection.insert_one(content_dict)

    analysis = analyse_text(content.text)

    result = AnalysisResult(text=content.text,toxicity_score=analysis["confidence"],label=analysis["label"],risk=analysis["risk"])

    return result



@router.get("/content/{user_id}")
def get_user_content(user_id:str, limit: int = 10):

    try:
        obj_user_id = ObjectId(user_id)
    except Exception:
        raise HTTPException(status_code=400, detail = "Invalid user ID format")
    
    user = users_collection.find_one({"_id": obj_user_id})
    if not user:
        raise HTTPException (status_code=404, detail= "User not found")
    
    contents = list(content_collection.find({"user_id":obj_user_id},{"_id":0}).sort("created_at",-1).limit(limit))
    
    for content in contents:
        content["user_id"] = str(content["user_id"])

    return contents

@router.get("/content/{user_id}/stats")
def get_user_stats(user_id: str):

    try:
        obj_user_id = ObjectId(user_id)
    except (InvalidId, Exception):
        raise HTTPException(status_code=400, detail="Invalid user ID format")

    user = users_collection.find_one({"_id": obj_user_id})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    post_count = content_collection.count_documents({"user_id": obj_user_id})

    return {
        "user_id": user_id,
        "total_posts": post_count
    }