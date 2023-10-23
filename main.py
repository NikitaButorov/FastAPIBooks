import token
from typing import Optional

import uvicorn
from fastapi import FastAPI
from fastapi_users import fastapi_users, FastAPIUsers
from Routers import books as BookRouter
from Routers import authors as AuthorRouter
from Routers import categories as CategoryRouter
from auth.manager import get_user_manager
from auth.schema import UserRead,UserCreate
from auth.auth import auth_backend
from fastapi import Request
from database import User, get_db


app = FastAPI()

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
def after_verification_request(user: UserRead, token: str, request: Optional[Request] = None):
    print(f"Verification requested for user {user.user_id}. Verification token: {token}")

app.include_router(BookRouter.router, prefix="/book")
app.include_router(AuthorRouter.router, prefix="/author")
app.include_router(CategoryRouter.router, prefix="/category")
app.include_router(fastapi_users.get_auth_router(auth_backend),prefix="/auth/jwt",tags=["auth"],)
app.include_router(fastapi_users.get_register_router(UserRead, UserCreate),prefix="/auth",tags=["auth"],)
app.include_router(fastapi_users.get_verify_router(after_verification_request(user=User,token=token,request=Request)),prefix="/auth",tags=["auth"],)

if __name__ == "__main__":
    uvicorn.run("main:app", host='localhost', port=3000, reload=True,workers=3)

