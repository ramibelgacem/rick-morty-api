from fastapi import FastAPI

from app import models
from app import database
from app.routers import episode

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(episode.router)


@app.get("/")
def home():
    return {"Detail": "First Endpoint"}
