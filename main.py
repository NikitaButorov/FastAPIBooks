import token
from typing import Optional, Dict, Any, List
import asyncio

import uvicorn
from fastapi import FastAPI, Depends, Query
from fastapi_users import fastapi_users, FastAPIUsers

import database
from Routers import books as BookRouter
from Routers import authors as AuthorRouter
from Routers import categories as CategoryRouter
from auth.admin import create_user
from auth.manager import get_user_manager, current_active_user, auth_backend
from auth.schema import UserRead, UserCreate, UserUpdate, UserResponse
from fastapi import Request
from database import User, Session, get_db
from auth.manager import fastapi_users


app = FastAPI()

def after_verification_request(user: UserRead, token: str, request: Optional[Request] = None):
    print(f"Verification requested for user {user.user_id}. Verification token: {token}")

app.include_router(BookRouter.router, prefix="/book")
app.include_router(AuthorRouter.router, prefix="/author")
app.include_router(CategoryRouter.router, prefix="/category")
app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)


@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}



@app.get("/users")
async def list_users(
    is_active: bool = Query(None),  # Опциональный параметр запроса "is_active"
    db: Session = Depends(get_db),  # Получаем экземпляр сессии SQLAlchemy
):
    query = db.query(User.username, User.email)  # Выбираем только username и email

    # Применяем фильтр is_active, если он указан в запросе
    if is_active is not None:
        query = query.filter(User.is_active == is_active)

    # Выполняем SQL-запрос и получаем результат
    results = query.all()

    # Преобразуем результат в список объектов UserResponse
    user_responses = [UserResponse(username=username, email=email) for username, email in results]

    return user_responses

    return results






if __name__ == "__main__":
    asyncio.run(create_user("admin@admin.com", "admin","admin",2))
    uvicorn.run("main:app", host='localhost', port=3000, reload=True,workers=3)

