from fastapi import APIRouter, Depends, HTTPException
from app.schemas.category_schema import Category
from sqlalchemy.orm import Session
from app.db.database import get_db
from app import curd

router = APIRouter()

# TEMP DATA — You can replace later with database


@router.get("/", response_model=list[Category])
def get_categories(db: Session = Depends(get_db)):
    return curd.get_categories(db)

@router.post("/", response_model=Category)
def add_category(category: Category, db: Session = Depends(get_db)):
    existing = db.query(__import__("app.db.models", fromlist=["models"]).models.Category).filter_by(name = category.name).first()
    if existing:
        raise HTTPException(status_code = 400, detail="Category with name {category.name} already exists.")
    return curd.create_category(db, category)