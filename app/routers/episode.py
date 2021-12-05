from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import database, models
from app.schemas import base, comment, episode

router = APIRouter(
    prefix='/episode',
    tags=['Episode']
)


@router.get('/',
            response_model=List[episode.EpisodeOut],
            status_code=status.HTTP_200_OK)
def episodes(db: Session = Depends(database.get_db)):
    return db.query(models.Episode).all()


@router.post(
    '/{episode_id}/comment',
    status_code=status.HTTP_201_CREATED,
    response_model=comment.CommentOut)
def create_comment_for_user(
            episode_id: int,
            comment: base.CommentBase,
            db: Session = Depends(database.get_db)):
    episode = db.query(models.Episode).filter(
        models.Episode.id == episode_id)
    if episode.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Episode with id={episode_id} not Found'
        )
    new_comment = models.Comment(
        message=comment.message,
        episode_id=episode_id)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment
