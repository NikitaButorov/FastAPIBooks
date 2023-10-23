import uuid
from typing import Optional

from fastapi_users import schemas
from fastapi_users import models
from pydantic import EmailStr




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


class UserCreate(UserRead,schemas.BaseUserCreate):
    username: str
    email: EmailStr
    password: str
    role_id: int
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False

class UserUpdate(UserRead,schemas.BaseUserUpdate):
    pass

class UserDB(UserRead,schemas.BaseUser):
    pass
