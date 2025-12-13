from fastapi import APIRouter, HTTPException
from app.schemas.question_schema import Question

# Dummy questions dataset
questions_data = [
    {"id": 1, "category_id": 1, "question": "What is Python?", "answer": "Python is a high-level programming language."},
    {"id": 2, "category_id": 1, "question": "What is a list?", "answer": "A list is a mutable collection in Python."},
    {"id": 3, "category_id": 2, "question": "What is Java?", "answer": "Java is an object-oriented programming language."},
    {"id": 4, "category_id": 2, "question": "What is JVM?", "answer": "JVM stands for Java Virtual Machine."},
]
router = APIRouter()

# 2️⃣ GET all questions
@router.get("/", response_model=list[Question])
def get_questions():
    return questions_data

@router.get("/{question_id}", response_model=Question)
def get_question_by_id(question_id: int):
    for q in questions_data:
        if q["id"] == question_id:
            return q
        raise HTTPException(status_code=404,detail=" Question not found for the question id: {question_id}")

@router.get("/cat/{category_id}", response_model=list[Question])
def get_questions_by_category(category_id: int):
    result = [q for q in questions_data if q["category_id"] == category_id]
    
    if not result:
        raise HTTPException(status_code=404, detail="No questions found for this category")
    
    return result

@router.post("/", response_model=Question, status_code=201)
def add_question(question: Question):
    # generate a new id (incremental)
    new_id = max((q["id"] for q in questions_data), default=0) +1
    new_q = {
        "id": new_id,
        "category_id": question.category_id,
        "question": question.question,
        "answer": question.answer,
    }
    questions_data.append(new_q)
    return new_q

