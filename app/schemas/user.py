from typing import List, Optional

from app.schemas.base import UserBase
from app.schemas.comment import CommentOut


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    password: Optional[str] = None


class UserOut(UserBase):
    id: int
    is_active: bool
    comments: List[CommentOut] = []

    class Config:
        orm_mode = True
