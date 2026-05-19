from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserResponse, UserDelete, UserUpdate
from app.services.user_service import create_user, get_users, delete_user, update_user
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

@router.delete("/users/{user_id}", response_model = UserDelete)
def delete_a_user(
    user_id:int,
    db:Session = Depends(get_db)
):
    return  delete_user(db, user_id)

@router.put("/users/{user_id}", response_model = UserResponse)
def update_a_user(
    user_id:int,
    user:UserUpdate,
    db:Session = Depends(get_db)
):
    return update_user(db, user.name, user.email, user_id)