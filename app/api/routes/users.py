from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user import (
    UserCreate, 
    UserResponse, 
    UserDelete, 
    UserUpdate, 
    UserUpdatePartially)
from app.services.user_service import (
    create_user, 
    get_users, 
    delete_user, 
    update_user, 
    get_a_user, 
    update_user_partially)
from app.db.database import SessionLocal

router = APIRouter()

#DataBase Dependancy
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@router.get("/get-a-user", response_model=UserResponse)
def get_single_user(
    user_id:int,
    db : Session = Depends(get_db)
):
    return get_a_user(db, user_id)

@router.get("/get-all-users", response_model = list[UserResponse])
def get_all_users(
    db : Session = Depends(get_db)    
):
    return get_users(db)

@router.post("/create-user", response_model = UserResponse)
def create_new_users(
    user : UserCreate,
    db : Session = Depends(get_db)
):
    return create_user(db, user.name, user.email)

@router.delete("/delete-a-user/{user_id}", response_model = UserDelete)
def delete_a_user(
    user_id:int,
    db:Session = Depends(get_db)
):
    return  delete_user(db, user_id)

@router.put("/update-a-user/{user_id}", response_model = UserResponse)
def update_a_user(
    user_id:int,
    user:UserUpdate,
    db:Session = Depends(get_db)
):
    return update_user(db, user.name, user.email, user_id)

@router.patch("/update-partially/{user_id}", response_model=UserResponse)
def update_partially(
    user_id:int,
    request:UserUpdatePartially,
    db:Session=Depends(get_db)
):
    return update_user_partially(db, user_id, request)
