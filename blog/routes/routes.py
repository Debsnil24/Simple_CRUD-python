from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from blog.middleware.database import get_db
from blog.models.schemas import BlogCreate, BlogResponse
from blog.middleware.crud import get_blog, get_blogs, create_blog, delete_blog, update_blog
import uuid

router = APIRouter(prefix="/blogs", tags=['blogs'])

@router.get("/", response_model=list[BlogResponse])
def read_blogs(db: Session = Depends(get_db)):
    return get_blogs(db)

@router.get("/{blog_id}", response_model=BlogResponse, status_code=status.HTTP_302_FOUND)
def read_blog(blog_id: uuid.UUID, db: Session = Depends(get_db)):
    if blog := get_blog(db, blog_id):
        return blog
    else:
        raise HTTPException(status_code=404, detail="Blog not Found")

@router.post("/", response_model=BlogResponse, status_code=status.HTTP_201_CREATED)
def create_blog_handler(blog: BlogCreate, db: Session = Depends(get_db)):
    return create_blog(db, blog)

@router.delete("/{blog_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_blog(blog_id: uuid.UUID, db: Session = Depends(get_db)):
    if not delete_blog(db, blog_id):
        raise HTTPException(status_code=404, detail="Blog not Found")
    return {"message":"Blog Deleted"}

@router.put("/{blog_id}", response_model=BlogResponse, status_code=status.HTTP_202_ACCEPTED)
def modify_blog(blog_id: uuid.UUID, blog_data: BlogCreate, db: Session = Depends(get_db)):
    if updated_blog := update_blog(db, blog_id, blog_data):
        return updated_blog
    raise HTTPException(status_code=404, detail="Blog not Found")