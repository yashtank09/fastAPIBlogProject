from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, Response, HTTPException
from ..hashing import Hash
from ..repository import blogs

from .. import schemas, database, models

# Path Operation
router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)

# Database Object
get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowBlog])
def getallblog(db: Session = Depends(get_db)):
    return blogs.getBlogs(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    return blogs.create(request, db)


@router.delete('/{id}')
def deleteBlog(id, db: Session = Depends(get_db)):
    return blogs.deleteBlog(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, req: schemas.Blog, db: Session = Depends(get_db)):
    return blogs.updateBlog(id, req, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def showBlog(id, db: Session = Depends(get_db)):
    return blogs.showBlogs(id, db)
