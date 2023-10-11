from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Path
from database import get_db
from Services import authors as AuthorService
from dto import books as BookDTO
from dto import authors as AuthorDTO
from dto import categories as CategoryDTO
from typing import List


async def create(data:AuthorDTO.Author = None, db:Session = Depends(get_db)):
    return AuthorService.create_author(data,db)

async def get(id:int = None, db: Session = Depends(get_db)):
    return AuthorService.get_author(id, db)

async def update(id:int = None,data:AuthorDTO.Author = None, db: Session = Depends(get_db)):
    return AuthorService.update(data, db, id)

async def delete(id:int = None, db:Session = Depends(get_db)):
    return AuthorService.remove(id, db)