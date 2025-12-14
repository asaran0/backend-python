from sqlalchemy.orm import Session
from app.db import models
from app.schemas.question_schema import Question as QuestionSchema
from app.schemas.category_schema import Category as CategorySchema
from app.schemas.user_schma import UserSignup, UserResponse, UserLogin
from app.utils.jwt_handler import hash_password, verify_password

#Category
def get_categories(db: Session):
    return db.query(models.Category).all()

def create_category(db: Session, category: CategorySchema):
    db_cat = models.Category(name=category.name)
    db.add(db_cat)
    db.commit()
    db.refresh(db_cat)
    return db_cat


#quesions
def get_questions(db: Session):
    return db.query(models.Question).all()

def get_question_by_id(db: Session, id: int):
    return db.query(models.Question).filter(models.Question.id == id).first()

def get_question_by_category_id(db: Session, category_id: int):
    return db.query(models.Question).filter(models.Question.category_id == category_id).all()

def create_question(db: Session, question: QuestionSchema):
    db_q = models.Question(
        category_id = question.category_id,
        question = question.question,
        answer = question.answer,
    )
    db.add(db_q)
    db.commit()
    db.refresh(db_q)
    return db_q


# User signin signup

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_all_users(db: Session):
    return db.query(models.User).all()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_by_email_or_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.email == username or models.User.username == username).first()
def create_user(db: Session, user: UserSignup):
    hashed_pwd = hash_password(user.passowrd)
    db_user = models.User(
        username = user.username,
        email = user.email,
        fullname = user.fullname,
        mobile_no = user.mobile_no,
        hashed_pwd = hashed_pwd,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user