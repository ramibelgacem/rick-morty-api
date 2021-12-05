from fastapi import FastAPI

from app import database, models
from app.routers import character, comment, episode, user

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(episode.router)
app.include_router(character.router)
app.include_router(comment.router)
app.include_router(user.router)
