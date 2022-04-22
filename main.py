from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


# This is the base path
@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blog from the db'}
    else:
        return {'data': f'{limit} blog from the db'}


# This is the blog path
@app.get('/about')
def blog():
    return {"data": 'about page'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'Unpublished Blog'}


@app.get('/blog/{id}')
def show(id: int):
    return {"data": {id}}


@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    # fetch comments of blog with id = id
    return {'data': {'1', '2'}}


class Blog(BaseModel):
    # pass
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(request: Blog):
    return {'data': "Blog is created"}
