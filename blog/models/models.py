import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Text, String
from blog.middleware.database import Base


class Blog(Base):
    __tablename__ = 'blogs'
    
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sa.text("uuid_generate_v4()"))
    title = Column(String, index=True)
    body = Column(Text)
