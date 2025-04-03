from sqlalchemy.orm import Session
from sqlalchemy.future import select
from blog.models.models import Blog
from blog.models.schemas import BlogCreate
import uuid

def get_blogs(db: Session):
    result = db.execute(select(Blog))
    return result.scalars().all()

def get_blog(db: Session, blog_id: uuid.UUID):
    result = db.execute(select(Blog).filter(Blog.id == blog_id))
    return result.scalars().first()

def create_blog(db: Session, blog: BlogCreate):
    new_blog = Blog(title=blog.title, body=blog.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete_blog(db: Session, blog_id: uuid.UUID):
    result = db.execute(select(Blog).filter(Blog.id == blog_id))
    if blog := result.scalars().first():
        db.delete(blog)
        db.commit()
        return True
    return False

def update_blog(db: Session, blog_id: uuid.UUID, blog_data: BlogCreate):
    result = db.execute(select(Blog).filter(Blog.id == blog_id))
    if blog := result.scalars().first():
        blog.title = blog_data.title
        blog.body = blog_data.body
        db.commit()
        db.refresh(blog)
        return blog
    return None