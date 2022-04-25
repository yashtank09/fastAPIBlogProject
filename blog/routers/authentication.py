from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from .. import schemas, database, models, token
from ..hashing import Hash
from sqlalchemy.orm import Session

router = APIRouter(
    tags=['Authentication']
)


@router.post('/login')
def login(req: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    userauth = db.query(models.User).filter(models.User.email == req.username).first()
    if not userauth:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'data': "You had entered Invalid Authentication "})

    if not Hash.Verify(userauth.password, req.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'data': "You had entered Invalid Password "})

    access_token = token.create_access_token(data={"sub": userauth.email})
    return {"access_token": access_token, "token_type": "bearer"}
