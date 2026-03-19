from fastapi import FastAPI
from app.routes import user, content

app = FastAPI()

app.include_router(user.router)
app.include_router(content.router)

@app.get("/")
def home():
    return {"message":"API Running"}
