from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Path

from auth.manager import current_superuser
from database import get_db, User
from Services import books as BookService
from dto import books as BookDTO
from dto import authors as AuthorDTO
from dto import categories as CategoryDTO
from typing import List


async def create(book_data_list: List[BookDTO.Book],  author_data_list: List[AuthorDTO.Author], category_data_list: List[CategoryDTO.Category],db: Session = Depends(get_db)):
    return BookService.create_books(book_data_list, author_data_list,  category_data_list, db)

async def get(id:int = None, db: Session = Depends(get_db),user: Session=Depends(current_superuser)):
    return BookService.get_book(id,db,user)

async def update(id: int = None, data: BookDTO.Book = None, db: Session = Depends(get_db), user: User = Depends(current_superuser)):
    return BookService.update(data, db, id)


async def delete(id:int = None, db: Session = Depends(get_db)):
    return BookService.remove(id, db)

async def allboks(db: Session = Depends(get_db)):
    return BookService.allbooks(db)

async def search(title: str = Path(..., description="Title of the book"),db:Session = Depends(get_db)):
    return BookService.book_by_name(title, db)


async def book_by_author(id:int = None, db:Session = Depends(get_db)):
    return  BookService.book_by_author(id,db)


async def book_by_category(category_name: str = None, db: Session = Depends(get_db)):
    return BookService.books_by_category(category_name,db)

async def count(db: Session = Depends(get_db)):
    return BookService.count_of_category(db)