from fastapi import FastAPI

from app import database, models
from app.routers import character, episode

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(episode.router)
app.include_router(character.router)


@app.get("/")
def home():
    return {"Detail": "First Endpoint"}
