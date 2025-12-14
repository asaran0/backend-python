from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime
class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)
    questions = relationship("Question", back_populates="category", cascade="all, delete-orphan")

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index= True)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False, index=True)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable= True)
    category = relationship("Category", back_populates="questions")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, index= True, primary_key=True)
    username = Column(String(20), unique=True, nullable=False, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    mobile_no = Column(String(20), nullable=True)
    fullname = Column(String(255),nullable=False)
    hashed_pwd = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.now)

