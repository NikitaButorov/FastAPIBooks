from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from database import get_db
from Services import categories as CategoryService
from dto import categories as CategoryDTO
from Controllers import categories as CategoryController

router = APIRouter()

@router.post("/categories",tags = ["category"])
async def create(data:CategoryDTO.Category = None, db:Session = Depends(get_db)):
    result = await CategoryController.create(data,db)
    return result

@router.get("/categories/{id}", tags=["category"])
async def get(id: int = None, db:Session = Depends(get_db)):
    result = await CategoryController.get(id, db)
    return result

@router.put("/categories/{id}", tags=["category"])
async def update(id:int = None,data:CategoryDTO.Category = None, db:Session = Depends(get_db)):
    result = await CategoryController.update(id,data, db)
    return result

@router.delete("/categories/{id}", tags=["category"])
async def remove(id:int = None, db:Session = Depends(get_db)):
    result = await CategoryController.remove(id,db)
    return result
