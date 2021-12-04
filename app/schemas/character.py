from typing import List

from app.schemas.base import CharacterBase, EpisodeBase


class CharacterOut(CharacterBase):
    episodes: List[EpisodeBase] = []
