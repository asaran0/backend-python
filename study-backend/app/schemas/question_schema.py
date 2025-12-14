from pydantic import BaseModel
from typing import Optional

class Question(BaseModel):
    id: Optional[int]
    category_id: int
    question: str
    answer: Optional[str] = None
    is_locked: Optional[bool] = False
    class Config:
        orm_mode = True
    # dificulty: str
    # hint: str

