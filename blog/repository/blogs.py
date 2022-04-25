from .. import models, schemas
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from fastapi import requests


def getBlogs(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def deleteBlog(id, db: Session):
    deleteBlog = db.query(models.Blog).filter(models.Blog.id == id)

    if not deleteBlog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail={'data': f"Blog with id {id} is not available"})

    deleteBlog.delete(synchronize_session=False)
    db.commit()
    return 'done'


def updateBlog(id, req, db: Session):
    updateBlog = db.query(models.Blog).filter(models.Blog.id == id)

    if not updateBlog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail={'data': f"Blog with id {id} is not available"})

    updateBlog.update(req.dict())  # Ned convert Blog schema object to dictionary
    db.commit()
    return 'Updated'


def showBlogs(id, db: Session):
    showBlog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not showBlog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail={'data': f"Blog with id {id} is not available"})

        # res.status_code = status.HTTP_200_OK
        # return {'data': f"Blog with id {id} is not available"}
    return showBlog