from fastapi import FastAPI

from models import Base
from database import engine
from routers import episode

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(episode.router)


@app.get("/")
def home():
    return {"Detail": "First Endpoint"}
