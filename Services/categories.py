from  Models.Models import Category
from sqlalchemy.orm import Session
from dto import categories
from fastapi import HTTPException


def create_category(data: categories.Category, db: Session):
    category = Category(category_name = data.category_name)

    db.add(category)
    db.commit()
    db.refresh(category)

    return category


def get_category(category_id:int, db:Session):
    category = db.query(Category).filter(Category.category_id==category_id).first()

    return category


def update(category_id:int, data:categories.Category, db:Session):
    category = db.query(Category).filter(Category.category_id==category_id).first()
    category.category_name = data.category_name

    db.add(category)
    db.commit()
    db.refresh(category)

    return category


def remove(category_id:int, db:Session):
    try:
        category = db.query(Category).filter(Category.author_id==category_id).first()
        if category:
            db.delete(category)
            db.commit()
        return category
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))