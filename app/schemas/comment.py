import datetime
from typing import Optional

from app.schemas.base import CommentBase


class CommentOut(CommentBase):
    id: int
    created_date: datetime.datetime
    user_id: Optional[int]

    class Config:
        orm_mode = True
