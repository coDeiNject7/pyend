
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#DATABASE_URL = "sqlite:///./test.db"
DATABASE_URL = "postgresql://pav:password123@localhost/fastapi_db"

engine = create_engine(
    DATABASE_URL,
    #connect_args = {"check_same_thread" : False} Since we are using pgadmin4. we dont need this.
)

SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine
)

Base = declarative_base()