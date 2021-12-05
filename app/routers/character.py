from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import database, models
from app.schemas import base, character, comment

router = APIRouter(
    prefix='/character',
    tags=['Character']
)


@router.get('/',
            response_model=List[character.CharacterOut],
            status_code=status.HTTP_200_OK)
def characters(db: Session = Depends(database.get_db)):
    return db.query(models.Character).all()


@router.post(
    '/{character_id}/comment',
    status_code=status.HTTP_201_CREATED,
    response_model=comment.CommentOut)
def create_comment_for_user(
            character_id: int,
            comment: base.CommentBase,
            db: Session = Depends(database.get_db)):
    character = db.query(models.Character).filter(
        models.Character.id == character_id)
    if character.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Character with id={character_id} not Found'
        )
    new_comment = models.Comment(
        message=comment.message,
        character_id=character_id)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment
