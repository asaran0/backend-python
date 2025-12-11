from pydantic import BaseModel

class Question(BaseModel):
    id: int
    category_id: int
    question: str
    answer: str
    # dificulty: str
    # hint: str

