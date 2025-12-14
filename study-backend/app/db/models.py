from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Boolean, Float
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
    is_locked = Column(Boolean, default=False, nullable = False)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, index= True, primary_key=True)
    username = Column(String(20), unique=True, nullable=False, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    mobile_no = Column(String(20), nullable=True)
    fullname = Column(String(255),nullable=False)
    hashed_pwd = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.now)

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable = False, unique = True)
    description = Column(String(255), nullable = True)
    price = Column(Float, nullable = False, default = 0.0)
    created_at = Column(DateTime, default = datetime.utcnow)
    subjects = relationship("Subject", back_populates="course", cascade="all, delete-orphan")


class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False, index=True)
    name = Column(String(255), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True, index=True)
    course = relationship("Course", back_populates="subjects")
    category = relationship("Category")

class Subscription(Base):
    __tablename__ = "subscriptions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False, index=True)
    active = Column(Boolean, default=True)
    starts_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    user = relationship("User")
    course = relationship("Course")

