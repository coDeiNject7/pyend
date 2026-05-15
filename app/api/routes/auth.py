from fastapi import APIRouter

router = APIRouter()

@router.get("/login")
def login():
    return {"Message" : "Login API !"}