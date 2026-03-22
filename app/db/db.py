from pymongo import MongoClient

MONGO_URL = "mongodb://localhost:27017"

client = MongoClient(MONGO_URL)
db = client["moderation_db"]

users_collection = db["users"]
content_collection = db["content"]

users_collection.create_index("email", unique=True)
content_collection.create_index("user_id")