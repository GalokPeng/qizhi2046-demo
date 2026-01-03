from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal, engine
import models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="社区API")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/posts", response_model=schemas.PostOut)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    obj = models.Post(**post.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@app.get("/posts", response_model=List[schemas.PostOut])
def list_posts(db: Session = Depends(get_db)):
    return db.query(models.Post).all()

@app.delete("/posts/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    post = db.get(models.Post, post_id)
    if not post:
        raise HTTPException(404, "Post not found")
    db.delete(post)
    db.commit()
    return {"message": "deleted"}

@app.post("/posts/{post_id}/comments")
def create_comment(
    post_id: int,
    comment: schemas.CommentCreate,
    db: Session = Depends(get_db)
):
    obj = models.Comment(
        post_id=post_id,
        content=comment.content,
        parent_id=comment.parent_id
    )
    db.add(obj)
    db.commit()
    return {"message": "ok"}

@app.delete("/comments/{comment_id}")
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    c = db.get(models.Comment, comment_id)
    if not c:
        raise HTTPException(404, "Comment not found")
    db.delete(c)
    db.commit()
    return {"message": "deleted"}

@app.get("/posts/{post_id}/comments", response_model=List[schemas.CommentOut])
def get_comments(
    post_id: int,
    page: int = 1, 
    size: int = 10, #给予个默认值
    db: Session = Depends(get_db)
):

    all_comments = (
        db.query(models.Comment)
        .filter(models.Comment.post_id == post_id)
        .order_by(models.Comment.created_at)
        .all()
    )

    comment_map = {}
    roots = []


    for c in all_comments:
        comment_map[c.id] = schemas.CommentOut(
            id=c.id,
            content=c.content,
            created_at=c.created_at,
            replies=[]
        )

    # 梳理子评论
    for c in all_comments:
        if c.parent_id:
            parent = comment_map.get(c.parent_id)
            if parent:
                parent.replies.append(comment_map[c.id])
        else:
            roots.append(comment_map[c.id])


    offset = (page - 1) * size
    end = offset + size
    paginated_roots = roots[offset:end]

    return paginated_roots

