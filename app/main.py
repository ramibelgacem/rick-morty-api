from fastapi import FastAPI

from models import Base
from database import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {"Detail": "First Endpoint"}
