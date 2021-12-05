from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base

DATABASE_USER = config('DATABASE_USER')
DATABASE_PASSWORD = config('DATABASE_PASSWORD')
DATABASE_HOST = config('DATABASE_HOST', default='localhost')
DATABASE_PORT = config('DATABASE_PORT', default='5432')
DATABASE_NAME = config('DATABASE_NAME')

SQLALCHEMY_DATABASE_URL =  \
    f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:\
    {DATABASE_PORT}/{DATABASE_NAME}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()
