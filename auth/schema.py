import uuid
from typing import Optional

from fastapi_users import schemas
from fastapi_users import models
from pydantic import EmailStr, BaseModel


class UserRead(schemas.BaseUser[int]):
    user_id: int
    email: str
    username: str
    role_id: int
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        from_attributes = True


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: EmailStr
    password: str
    role_id: int
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False

class UserUpdate(schemas.BaseUserUpdate):
    pass

class UserResponse(BaseModel):
    username: str
    email: str

