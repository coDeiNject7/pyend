from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import create_user, get_users
from app.db.database import SessionLocal

router = APIRouter()

#DataBase Dependancy
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@router.post("/users", response_model = UserResponse)
def create_new_users(
    user : UserCreate,
    db : Session = Depends(get_db)
):
    return create_user(db, user.name, user.email)

@router.get("/users", response_model = list[UserResponse])
def get_all_users(
    db : Session = Depends(get_db)    
):
    return get_users(db)
