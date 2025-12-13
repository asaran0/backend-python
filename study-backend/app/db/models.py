from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

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