from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import database, models
from app.schemas import base, comment
from app.routers.utils import build_filters

router = APIRouter(
    prefix='/comment',
    tags=['Comment']
)


@router.get('/',
            response_model=List[comment.CommentOut],
            status_code=status.HTTP_200_OK)
def comments(
        offset: int = 0,
        limit: int = 5,
        message: Optional[str] = None,
        db: Session = Depends(database.get_db)):
    return db.query(models.Comment).filter(
        *build_filters(models.Comment, {
            'message': message,
        })).offset(offset).limit(limit).all()


@router.get('/{comment_id}',
            status_code=status.HTTP_200_OK,
            response_model=comment.CommentOut)
def read_comment(
        comment_id: int,
        db: Session = Depends(database.get_db)):
    comment = db.query(models.Comment).filter(
        models.Comment.id == comment_id)
    if comment.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Comment with id={comment_id} not Found'
        )
    return comment.first()


@router.put('/{comment_id}',
            status_code=status.HTTP_202_ACCEPTED,
            response_model=comment.CommentOut)
def update_comment(
            comment_id: int,
            new_comment: base.CommentBase,
            db: Session = Depends(database.get_db)):
    comment = db.query(models.Comment).filter(models.Comment.id == comment_id)
    if comment.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Comment with id={comment_id} not Found'
        )

    comment.update(new_comment.dict())
    db.commit()
    return comment.first()


@router.delete('/{comment_id}')
def destory_comment(comment_id: int, db: Session = Depends(database.get_db)):
    comment = db.query(models.Comment).filter(models.Comment.id == comment_id)
    if comment.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Comment with id={comment_id} not Found'
        )

    comment.delete()
    db.commit()
