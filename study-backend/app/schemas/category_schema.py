from pydantic import BaseModel
from typing import Optional
class Category(BaseModel):
    id: Optional[int]
    name: str
    class Config:
        orm_mode = True