from fastapi import FastAPI
from app.routes import user, content
from app.db import db as db_module
from app.services.transformer_service import transformer_predict

app = FastAPI()

app.include_router(user.router)
app.include_router(content.router)

@app.get("/")
def home():
    return {"message": "API Running"}

@app.on_event("startup")
def startup_db():
    db_module.connect_to_mongo()
    print("Connected to Mongo:", db_module.db)

@app.on_event("startup")
def warmup():
    transformer_predict("test")