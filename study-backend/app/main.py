from fastapi import FastAPI
from app.routers import categories, questions, questions_list
from app.db.database import engine, Base


app = FastAPI(
    title="Study App Backend",
    version="1.0.0"
)

app.include_router(categories.router, prefix="/api/v1/categories", tags=["Categories"])
app.include_router(questions_list.router, prefix="/api/v1/questions1", tags=["Questions1"])
app.include_router(questions.router, prefix="/api/v1/questions", tags=["Questions"])