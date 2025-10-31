from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    body: str | None = None
    userId: int | None = None


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
