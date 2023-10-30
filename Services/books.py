from sqlalchemy.ext.asyncio import AsyncSession
from streamlit import status

from Models.Models import Book,Author,Category
from sqlalchemy.orm import Session

from database import User, get_db
from dto import books,authors,categories
from sqlalchemy import func, select
from fastapi import HTTPException, Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from auth.manager import current_superuser


def superuser_required(function):
    async def wrapper(id: int = None, db: Session = Depends(get_db), user=Depends(current_superuser), *args, **kwargs):
        if user is None or not user.is_superuser:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Permission denied")
        return function(id, db, user, *args, **kwargs)
    return wrapper

def create_books(book_data_list, author_data_list, category_data_list, db: Session):
    try:
        books_to_add = []
        authors_to_add = []
        categories_to_add = []

        for category_data in category_data_list:
            existing_category = db.query(Category).filter_by(category_name=category_data.category_name).first()
            if not existing_category:
                category = Category(category_name=category_data.category_name)
                db.add(category)
                categories_to_add.append(category)
            else:
                categories_to_add.append(existing_category)

        for author_data in author_data_list:
            existing_author = db.query(Author).filter_by(author_name=author_data.author_name).first()
            if not existing_author:
                author = Author(author_name=author_data.author_name)
                db.add(author)
                authors_to_add.append(author)
            else:
                authors_to_add.append(existing_author)

        for book_data in book_data_list:

            book = Book(
                title=book_data.title,
                isbn=book_data.isbn,
                pageCount=book_data.pageCount,
                thumbnailUrl=book_data.thumbnailUrl,
                shortDescription=book_data.shortDescription,
                longDescription=book_data.longDescription,
                status=book_data.status
            )
            db.add(book)
            books_to_add.append(book)

        db.commit()

        return books_to_add, authors_to_add, categories_to_add

    except IntegrityError as e:
        db.rollback()
        print(f"Произошла ошибка IntegrityError: {e}")

    except Exception as e:
        db.rollback()
        print(f"Произошла ошибка: {e}")

    finally:
        db.close()


def get_book(id: int, db,user:User):
    book = db.query(Book).filter(Book.id == id).first()
    if book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return book

def update(data: books.Book, db:Session, id:int ):
    book = db.query(Book).filter(Book.id==id).first()
    book.title = data.title
    book.isbn = data.isbn
    book.pageCount = data.pageCount
    book.thumbnailUrl = data.thumbnailUrl
    book.shortDescription = data.shortDescription
    book.longDescription = data.longDescription
    book.status = data.status
    db.add(book)
    db.commit()
    db.refresh(book)

    return book

def remove(id: int, db:Session):
    try:
        book = db.query(Book).filter(Book.id==id).first()
        if book:
            db.delete(book)
            db.commit()
        return book
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def allbooks(db:Session):
    books = db.query(Book).all()
    db.close()
    return books


def book_by_name(title: str, db:Session()):
    books = db.query(Book).filter(Book.title.ilike(f'%{title}%')).all()
    db.close()
    return books

def book_by_author(author_id: int, db:Session()):
    books = db.query(Book).join(Author.books).filter(Author.author_id == author_id).all()
    return books


def books_by_category(category_name: str, db:Session()):
    books = db.query(Book).join(Book.categorys).filter(Category.category_name == category_name).all()
    return books

def count_of_category(db:Session):
    category_counts = db.query(Category.category_name, func.count(Book.id).label('book_count')) \
        .join(Book.categorys) \
        .group_by(Category.category_name) \
        .all()
    return category_counts

