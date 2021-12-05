from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import database, models
from app.schemas import comment

router = APIRouter(
    prefix='/comment',
    tags=['Comment']
)


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
