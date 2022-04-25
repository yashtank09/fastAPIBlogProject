from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException
from ..repository import users
from .. import schemas, database, models

router = APIRouter(
    tags=['Users']
)
get_db = database.get_db


@router.post('/user', response_model=schemas.showUser)
def create_users(req: schemas.User, db: Session = Depends(get_db)):
    return users.createUser(req, db)


@router.get('/user/{id}', response_model=schemas.showUser)
def showUser(id: int, db: Session = Depends(get_db)):
    return users.Show_User(id, db)


@router.get('/user', response_model=List[schemas.showUser])
def getallusers(db: Session = Depends(get_db)):
    return users.ShowAll_Users(db)