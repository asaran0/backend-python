from fastapi import FastAPI
from app.routers import categories
from app.routers import questions

app = FastAPI(
    title="Study App Backend",
    version="1.0.0"
)

app.include_router(categories.router, prefix="/api/v1/categories", tags=["Categories"])
app.include_router(questions.router, prefix="/api/v1/questions", tags=["Questions"])