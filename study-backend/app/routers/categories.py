from fastapi import APIRouter
from app.schemas.category_schema import Category

router = APIRouter()

# TEMP DATA — You can replace later with database
categories_list = [
    {"id": 1, "name": "Python"},
    {"id": 2, "name": "Java"},
    {"id": 3, "name": "Data Structures"},
    {"id": 4, "name": "Operating Systems"},
    {"id": 5, "name": "Computer Networks"},
]

@router.get("/", response_model=list[Category])
def get_categories():
    return categories_list
