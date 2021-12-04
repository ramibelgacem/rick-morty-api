from typing import List

from pydantic import BaseModel


class EpisodeBase(BaseModel):
    name: str
    air_date: str
    reference: str


class CharacterBase(BaseModel):
    name: str
    status: str
    species: str
    type: str
    gender: str


class Character(CharacterBase):
    class Config:
        orm_mode = True


class Episode(EpisodeBase):
    characters: List[Character] = []

    class Config:
        orm_mode = True
