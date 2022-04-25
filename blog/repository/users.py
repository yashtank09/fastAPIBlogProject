from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException
from ..hashing import Hash
from .. import schemas, database, models


def createUser(req: schemas.User, db: Session):
    newUser = models.User(name=req.name, email=req.email, password=Hash.bcrypt(req.password))
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser


def Show_User(id: int, db: Session):
    showUser = db.query(models.User).filter(models.User.id == id).first()

    if not showUser:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'data': f"User with id {id} not found"})
    return showUser


def ShowAll_Users(db: Session):
    all_Users = db.query(models.User).all()
    return all_Users
