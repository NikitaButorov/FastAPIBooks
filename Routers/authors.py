from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from database import get_db
from dto import authors as AuthorDTO
from Controllers import authors as AuthorController


router = APIRouter()


@router.post('/authors', tags=["author"])
async def create(data:AuthorDTO.Author = None, db:Session = Depends(get_db)):
    result = await AuthorController.create(data,db)
    return result

@router.get('/authors/{id}', tags=["author"])
async def get(id:int = None, db: Session = Depends(get_db)):
    result = await AuthorController.get(id,db)
    return result

@router.put('/authors/{id}', tags=["author"])
async def update(id:int = None,data:AuthorDTO.Author = None, db: Session = Depends(get_db)):
    result = await AuthorController.update(id,data,db)
    return result

@router.delete('/authors/{id}', tags=["author"])
async def delete(id:int = None, db:Session = Depends(get_db)):
    result = await AuthorController.delete(id,db)
    return result