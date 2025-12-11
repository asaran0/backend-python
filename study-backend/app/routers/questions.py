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
@router.get("/all", response_model=list[Question])
def get_questions():
    return questions_data

@router.get("/id/{question_id}", response_model=Question)
def get_question_by_id(id: int):
    return questions_data["id":id]

@router.get("/{category_id}", response_model=list[Question])
def get_questions_by_category(category_id: int):
    result = [q for q in questions_data if q["category_id"] == category_id]
    
    if not result:
        raise HTTPException(status_code=404, detail="No questions found for this category")
    
    return result


