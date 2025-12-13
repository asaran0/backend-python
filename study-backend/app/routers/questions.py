from fastapi import APIRouter, HTTPException, Depends
from app.schemas.question_schema import Question
from sqlalchemy.orm import Session
from app.schemas.question_schema import Question
from app.db.database import get_db
from app import curd


# Dummy questions dataset

router = APIRouter()

# 2️⃣ GET all questions
@router.get("/", response_model=list[Question])
def get_questions(db: Session = Depends(get_db)):
    return curd.get_questions(db)

@router.get("/{question_id}", response_model=Question)
def get_question_by_id(question_id: int, db: Session = Depends(get_db)):
    ques = curd.get_question_by_id(db, question_id)
    if ques:
        return ques
    raise HTTPException(status_code=404,detail=" Question not found for the question id: {question_id}")

@router.get("/cat/{category_id}", response_model=list[Question])
def get_questions_by_category(category_id: int, db: Session = Depends(get_db)):
    quesList = curd.get_question_by_category_id(db, category_id)
    if not quesList:
        raise HTTPException(status_code=404, detail="No questions found for this category")
    
    return quesList

@router.post("/", response_model=Question, status_code=201)
def add_question(question: Question, db: Session = Depends(get_db)):
    # generate a new id (incremental)
    #check if category already exists if not we will not save the question.
    new_q = curd.get_question_by_id(question.id)
    if not new_q:
        raise HTTPException(status_code = 400, detail= " Question already found.")
    return curd.create_category(db, question)

