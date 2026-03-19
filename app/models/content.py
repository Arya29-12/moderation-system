from pydantic import BaseModel

class Content(BaseModel):
    user_id:str
    text:str