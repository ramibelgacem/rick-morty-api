from typing import List

from app.schemas.base import CharacterBase, EpisodeBase
from app.schemas.comment import CommentOut


class EpisodeOut(EpisodeBase):
    characters: List[CharacterBase] = []
    comments: List[CommentOut] = []
