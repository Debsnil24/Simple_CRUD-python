from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from blog.config import DB_URL

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(bind=engine, expire_on_commit=False, autoflush=False, class_=Session)

Base = declarative_base()

def get_db():
    with SessionLocal() as session:
        yield session
        