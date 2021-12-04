from fastapi import FastAPI

from app import models
from app import database
from app.routers import episode, character

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(episode.router)
app.include_router(character.router)


@app.get("/")
def home():
    return {"Detail": "First Endpoint"}
