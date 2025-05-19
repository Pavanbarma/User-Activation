from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text, JSON
import uuid4

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer,primary_key=True,nullable=False, default=uuid4.uuid())
    user_name = Column(String,nullable=False)
    event = Column(JSON,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

