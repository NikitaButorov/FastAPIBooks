from Models.Models import Author
from sqlalchemy.orm import Session
from dto import authors
from fastapi import HTTPException


def create_author(data:authors.Author, db: Session):
    author = Author(author_name = data.author_name)

    db.add(author)
    db.commit()
    db.refresh(author)

    return author

def get_author(author_id:int, db: Session):
    return db.query(Author).filter(Author.author_id==author_id).first()

def update(data:authors.Author, db:Session, author_id:int):
    author = db.query(Author).filter(Author.author_id==author_id).first()
    author.author_name = data.author_name

    db.add(author)
    db.commit()
    db.refresh(author)

    return author


def remove (author_id: int, db:Session):
    try:
        author = db.query(Author).filter(Author.author_id==author_id).first()
        if author:
            db.delete(author)
            db.commit()
        return author
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
