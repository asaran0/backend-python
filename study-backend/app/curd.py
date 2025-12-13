from sqlalchemy.orm import Session
from app.db import models
from app.schemas.question_schema import Question as QuestionSchema
from app.schemas.category_schema import Category as CategorySchema

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