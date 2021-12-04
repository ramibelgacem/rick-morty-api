from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app import database
from app import models
from app.schemas import episode

router = APIRouter(
    prefix='/episode',
    tags=['Episode']
)


@router.get('/',
            response_model=List[episode.Episode],
            status_code=status.HTTP_200_OK)
def episodes(db: Session = Depends(database.get_db)):
    return db.query(models.Episode).all()
