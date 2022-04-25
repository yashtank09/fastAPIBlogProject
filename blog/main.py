from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blog, users, authentication

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(users.router)
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @app.post('/blog', status_code=status.HTTP_201_CREATED, tags=['blogs'])
# def create(request: schemas.Blog, db: Session = Depends(get_db)):
#     new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog


# @app.get('/blog', response_model=List[schemas.ShowBlog], tags=['blogs'])
# def getallblog(db: Session = Depends(get_db)):
#     all_blogs = db.query(models.Blog).all()
#     return all_blogs


# @app.delete('/blog/{id}', tags=['blogs'])
# def deleteBlog(id, db: Session = Depends(get_db)):
#     db.query(models.Blog).filter(models.Blog.id == id)
#
#     if not deleteBlog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail={'data': f"Blog with id {id} is not available"})
#
#     deleteBlog.delete(synchronize_session=False)
#     db.commit()
#     return 'done'


# @app.put('/bog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
# def update(id, req: schemas.Blog, db: Session = Depends(get_db)):
#     updateBlog = db.query(models.Blog).filter(models.Blog.id == id)
#
#     if not updateBlog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail={'data': f"Blog with id {id} is not available"})
#
#     updateBlog.update(req.dict())  # Ned convert Blog schema object to dictionary
#     db.commit()
#     return 'Updated'


# @app.get('/blog{id}', status_code=200, response_model=schemas.ShowBlog, tags=['blogs'])
# def showBlog(id, res: Response, db: Session = Depends(get_db)):
#     showBlog = db.query(models.Blog).filter(models.Blog.id == id).first()
#
#     if not showBlog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail={'data': f"Blog with id {id} is not available"})
#         # res.status_code = status.HTTP_200_OK
#         # return {'data': f"Blog with id {id} is not available"}
#     return showBlog


# @app.post('/user', response_model=schemas.showUser, tags=['users'])
# def create_users(req: schemas.User, db: Session = Depends(get_db)):
#     newUser = models.User(name=req.name, email=req.email, password=Hash.bcrypt(req.password))
#     db.add(newUser)
#     db.commit()
#     db.refresh(newUser)
#     return newUser


# @app.get('/user/{id}', response_model=schemas.showUser, tags=['users'])
# def showUser(id: int, db: Session = Depends(get_db)):
#     showUser = db.query(models.User).filter(models.User.id == id).first()
#
#     if not showUser:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'data': f"User with id {id} not found"})
#     return showUser


# @app.get('/user', response_model=List[schemas.showUser], tags=['users'])
# def getallusers(db: Session = Depends(get_db)):
#     all_Users = db.query(models.User).all()
#     return all_Users
