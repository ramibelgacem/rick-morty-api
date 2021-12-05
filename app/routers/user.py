from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import database, models
from app.schemas import user
from app.security import hash_password

router = APIRouter(
    prefix='/user',
    tags=['Users']
)


@router.get('/{user_id}', response_model=user.UserOut)
def read_user(user_id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User with id={user_id} not Found'
        )
    return user


@router.post('/', response_model=user.UserOut)
def create_user(user: user.UserCreate, db: Session = Depends(database.get_db)):
    new_user = models.User(
        email=user.email,
        hashed_password=hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.put('/{user_id}',
            status_code=status.HTTP_202_ACCEPTED,
            response_model=user.UserOut)
def update_user(
            user_id: int,
            new_values: user.UserUpdate,
            db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User with id={user_id} not Found'
        )
    new_values = new_values.dict()
    if new_values["password"]:
        user.hashed_password = hash_password(new_values["password"])
    if new_values["email"]:
        user.email = new_values["email"]
    db.commit()
    return user


@router.delete('/{user_id}')
def destory_user(user_id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == user_id)
    if user.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User with id={user_id} not Found'
        )
    user.delete()
    db.commit()
