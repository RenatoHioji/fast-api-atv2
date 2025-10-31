from fastapi import FastAPI, HTTPException
from app import crud, schemas

app = FastAPI(title="AT2 - FastAPI + Pytest")

@app.get("/posts", response_model=list[schemas.Post])
def list_posts():
    try:
        return crud.get_all_posts()
    except Exception:
        raise HTTPException(status_code=500, detail="External API error")

@app.get("/posts/{post_id}", response_model=schemas.Post)
def get_post(post_id: int):
    post = crud.get_post_by_id(post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@app.post("/posts", response_model=schemas.Post, status_code=201)
def create_post(payload: schemas.PostCreate):
    created = crud.create_post(payload)
    if created is None:
        raise HTTPException(status_code=502, detail="External API error")
    return created
