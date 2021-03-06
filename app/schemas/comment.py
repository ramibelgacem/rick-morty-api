import datetime

from app.schemas.base import CommentBase


class CommentOut(CommentBase):
    id: int
    created_date: datetime.datetime

    class Config:
        orm_mode = True
