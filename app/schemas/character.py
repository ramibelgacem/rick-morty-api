from typing import List

from app.schemas.base import CharacterBase, EpisodeBase
from app.schemas.comment import CommentOut


class CharacterOut(CharacterBase):
    episodes: List[EpisodeBase] = []
    comments: List[CommentOut] = []
