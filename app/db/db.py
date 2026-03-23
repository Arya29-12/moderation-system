from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["moderation_db"]

users_collection = db["users"]
content_collection = db["content"]

users_collection.create_index("email", unique=True)
content_collection.create_index("user_id")