from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Path
from database import get_db
from Services import categories as CategoryService
from dto import books as BookDTO
from dto import authors as AuthorDTO
from dto import categories as CategoryDTO
from typing import List


async def create(data:CategoryDTO.Category = None, db:Session = Depends(get_db)):
    return CategoryService.Category(data,db)

async def get(id: int = None, db:Session = Depends(get_db)):
    return CategoryService.Category(id,db)

async def update(id:int = None,data:CategoryDTO.Category = None, db:Session = Depends(get_db)):
    return CategoryService.Category(id,data,db)

async def remove(id:int = None, db:Session = Depends(get_db)):
    return  CategoryService.Category(id, db)