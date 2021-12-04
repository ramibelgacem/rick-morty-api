import datetime

from app.schemas.base import CommentBase


class CommentOut(CommentBase):
    created_date: datetime.datetime

    class Config:
        orm_mode = True
