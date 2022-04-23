from fastapi import FastAPI, Depends, Response, status
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get('/blog')
def getallblog(db: Session = Depends(get_db)):
    all_blogs = db.query(models.Blog).all()
    return all_blogs


@app.get('/blog{id}', status_code=200)
def showBlog(id, res: Response, db: Session = Depends(get_db)):
    showBlog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not showBlog:
        res.status_code = status.HTTP_200_OK
        return {'data': f"Blog with id {id} is not available"}
    return showBlog
