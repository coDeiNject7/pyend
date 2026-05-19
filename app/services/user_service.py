from sqlalchemy.orm import Session
from app.models.user import User

def create_user(db : Session, name:str, email:str):
    user = User(name=name, email=email)

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def get_users(db:Session):
    return db.query(User).all()

def delete_user(db:Session, user_id):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return {"message" : "User not Found"}

    db.delete(user)
    db.commit()

    return {"message" : "User Deleted Successfully"}

def update_user(db:Session, name:str, email:str, user_id):
    user = db.query(User).filter(User.id==user_id).first()

    if not user:
        return {"message" : "User not Found, nothing to update"}

    user.name=name
    user.email=email
    db.commit()
    db.refresh(user)

    return user