from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app import database, models
from app.schemas import character

router = APIRouter(
    prefix='/character',
    tags=['Character']
)


@router.get('/',
            response_model=List[character.CharacterOut],
            status_code=status.HTTP_200_OK)
def characters(db: Session = Depends(database.get_db)):
    return db.query(models.Character).all()
