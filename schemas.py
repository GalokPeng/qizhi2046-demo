from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class PostCreate(BaseModel):
    title: str
    content: str


class PostOut(PostCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class CommentCreate(BaseModel):
    content: str
    parent_id: Optional[int] = None


class CommentOut(BaseModel):
    id: int
    content: str
    created_at: datetime
    replies: List["CommentOut"] = []

    class Config:
        orm_mode = True
