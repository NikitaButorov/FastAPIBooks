from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
from database import get_db
from Services import books as BookService
from dto import books as BookDTO
from dto import authors as AuthorDTO
from dto import categories as CategoryDTO
from typing import List
from Controllers import books as BookController


router = APIRouter()

@router.post('/books', tags=["book"], operation_id="create")
async def create(
    book_data_list: List[BookDTO.Book],
    author_data_list: List[AuthorDTO.Author],
    category_data_list: List[CategoryDTO.Category],
    db: Session = Depends(get_db)
):
    result = await BookController.create(book_data_list, author_data_list, category_data_list, db)
    return result

@router.get('/books/id/{id}', tags=["book"])
async def get(id:int = None, db: Session = Depends(get_db)):
    result = await BookController.get(id,db)
    return result

@router.put('/books/{id}', tags=["book"])
async def update(id:int = None,data:BookDTO.Book = None, db: Session = Depends(get_db)):
    result = await BookController.update(id,data,db)
    return result

@router.delete('/books/{id}', tags=["book"])
async def delete(id:int = None, db: Session = Depends(get_db)):
    result = await BookController.delete(id,db)
    return result

@router.get('/books', tags=["book"])
async def allboks(db: Session = Depends(get_db)):
   result = await BookController.allboks(db)
   return result

@router.get('/books/title/{title}', tags=["book"])
async def search(title: str = Path(..., description="Title of the book"),db:Session = Depends(get_db)):
    result = await BookController.search(title,db)
    return result

@router.get('/books/author/{id}', tags=["book"])
async def book_by_author(id:int = None, db:Session = Depends(get_db)):
    result = await BookController.book_by_author(id,db)
    return result

@router.get('/books/category/{category_name}', tags=["book"])
async def book_by_category(category_name: str = None, db: Session = Depends(get_db)):
    result = await BookController.book_by_category(category_name,db)
    return result

@router.get('/books/count', tags=["book"])
async def count(db: Session = Depends(get_db)):
    result = await BookController.count(db)
    return result