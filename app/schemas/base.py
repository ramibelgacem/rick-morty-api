from typing import Optional

from pydantic import BaseModel


class EpisodeBase(BaseModel):
    name: str
    air_date: str
    reference: str

    class Config:
        orm_mode = True


class CharacterBase(BaseModel):
    name: str
    status: str
    species: str
    type: str
    gender: str

    class Config:
        orm_mode = True


class CommentBase(BaseModel):
    message: str


class UserBase(BaseModel):
    email: Optional[str] = None
