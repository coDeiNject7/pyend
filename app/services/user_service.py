from sqlalchemy.orm import Session
from app.models.user import User
from fastapi import HTTPException, status

def create_user(db : Session, name:str, email:str):

    user = db.query(User).filter(User.name==name).first()

    if user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= f"User Name {user.name} Already Exists")

    user = db.query(User).filter(User.email==email).first()

    if user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= f"Mail {user.email} Already Exists")

    user = User(
        name=name, 
        email=email
        )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def get_users(db:Session):
    return db.query(User).all()

def get_a_user(db:Session, user_id):
    user = db.query(User).filter(User.id==user_id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
    
    return user

def delete_user(db:Session, user_id):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found",)

    db.delete(user)
    db.commit()

    return {"message" : "User Deleted Successfully"}

def update_user(db:Session, name:str, email:str, user_id):
    user = db.query(User).filter(User.id==user_id).first()

    if not user:
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail="User not Found, nothing to update",)

    user.name=name
    user.email=email
    db.commit()
    db.refresh(user)

    return user

def update_user_partially(db:Session, user_id, request):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User Not Found")

    user_data = request.dict(exclude_unset=True)

    for field, value in user_data.items():
        setattr(user, field, value)

    db.commit()
    db.refresh(user)

    return user
