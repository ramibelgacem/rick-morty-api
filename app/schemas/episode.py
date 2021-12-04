from typing import List

from app.schemas.base import CharacterBase, EpisodeBase


class EpisodeOut(EpisodeBase):
    characters: List[CharacterBase] = []
