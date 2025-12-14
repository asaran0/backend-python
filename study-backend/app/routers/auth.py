from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta

from app.db.database import get_db
from app.db.models import User
from app.schemas.user_schma import UserLogin, UserResponse, UserSignup, LoginResponse
from app.utils.jwt_handler import create_access_token, verify_password
from app import curd
from app.config import ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter()

@router.post("/signup", response_model=UserResponse, status_code=201)
def signup(user: UserSignup, db: Session = Depends(get_db)):
    existing_user = curd.get_user_by_username(db, user.username)
    if existing_user:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
                            detail="UserName already exists, Please use other username."
                            )
    existing_email = curd.get_user_by_email(db, user.email)
    if existing_email:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
                            detail="Email already resistered please use other email or go to login.")
    
    #create the user.
    new_user = curd.create_user(db, user)
    return new_user

@router.post("/login", response_model=LoginResponse, status_code=200)
def login(credentials: UserLogin, db: Session = Depends(get_db)):
    user = curd.get_user_by_email_or_username(db, credentials.username)
    if not user:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid username/email.")
    
    # Verify password:
    if not verify_password(credentials.password, user.hashed_pwd):
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,
                            detail = "Please enter the correct password.")
    
    # Create access token (JWT token)
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data = {"sub": str(user.id), "username": user.username},
        expires_delta = access_token_expires
    )
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": user
    }

@router.get("/users", response_model=list[UserResponse])
def getUsers(db: Session = Depends(get_db)):
    return curd.get_all_users(db)