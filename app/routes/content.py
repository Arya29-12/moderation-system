from fastapi import APIRouter
from bson import ObjectId
from bson.errors import InvalidId

from app.models.content import Content
from app.models.analysis import AnalysisResult
from app.db.collections import content_collection, users_collection

router = APIRouter()

@router.post("/content", response_model = AnalysisResult)
def submit_content(content: Content):

    user = users_collection.find_one({"_id": ObjectId(content.user_id)})
    if not user:
        return {"error": "User not found"}
    
    content_dict = content.model_dump()
    content_collection.insert_one(content_dict)

    result = AnalysisResult(text = content.text, toxicity_score = 0.1, label = "Safe")
    return result

@router.get("/content/{user_id}")
def get_user_content(user_id:str):

    try:
        obj_id = ObjectId(user_id)
    except InvalidId:
        return {"error": "Invalid user ID format"}
    
    user = users_collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        return {"error": "User not found"}
    contents = list(content_collection.find({"user_id":user_id},{"_id":0}))
    return contents