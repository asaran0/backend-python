from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserSignup(BaseModel):
    username: str
    email: str
    fullname: str
    passowrd: str
    mobile_no: Optional[str] = None

class UserLogin(BaseModel):
    username: str # This can be username or email.
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    fullname: str
    mobile_no: Optional[str] = None
    created_at: datetime

    class Config:
        orm_mode = True

class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    user: UserResponse
