from pymongo import MongoClient

MONGO_URL = "mongodb://localhost:27017"

client = MongoClient(MONGO_URL)

db = client["moderation_db"]

db["users"].create_index("email", unique=True) #unique email
db["content"].create_index("user_id") #indexing