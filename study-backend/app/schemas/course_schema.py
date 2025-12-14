from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class SubjectBase(BaseModel):
    id: Optional[int]
    name: str
    category_id: Optional[int] = None

    class Config:
        orm_mode = True

class CourseBase(BaseModel):
    id: Optional[int]
    name: str
    description: Optional[str] = None
    price: float
    subjects: Optional[List[SubjectBase]] = []

    class Config:
        orm_mode = True

class SubscriptionCreate(BaseModel):
    course_id: int
    payment_token: Optional[str] = None

class SubscriptionResponse(BaseModel):
    id: int
    user_id: int
    course_id: int
    active: bool
    starts_at: datetime
    expires_at: Optional[datetime]

    class Config:
        orm_mode = True