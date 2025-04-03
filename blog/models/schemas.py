from pydantic import BaseModel
import uuid
class Blog(BaseModel):
    title: str
    body: str

class BlogCreate(Blog):
    pass

class BlogResponse(Blog):
    id: uuid.UUID
    
    class Config:
        from_attributes = True