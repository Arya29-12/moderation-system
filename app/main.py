print("APP STARTING...")
from fastapi import FastAPI
from app.routes import user, content
from app.db.db import connect_to_mongo

app = FastAPI()

@app.on_event("startup")
def startup_event():
    connect_to_mongo()

app.include_router(user.router)
app.include_router(content.router)

@app.get("/")
def home():
    return {"message": "API Running"}