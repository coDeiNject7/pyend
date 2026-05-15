from fastapi import FastAPI
from app.db.database import engine, Base
from app.api.routes.auth import router as auth_router
from app.api.routes import users_router

app = FastAPI()

#Create Tables
#Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"Message" : "Back-End is Running successfully !"}


app.include_router(auth_router)

#GET & POST API for Users
app.include_router(users_router)