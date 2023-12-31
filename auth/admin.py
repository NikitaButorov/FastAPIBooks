import contextlib

from fastapi_users.exceptions import UserAlreadyExists

from auth.manager import get_user_manager
from auth.schema import UserCreate
from database import get_async_session, get_user_db

get_async_session_context = contextlib.asynccontextmanager(get_async_session)
get_user_db_context = contextlib.asynccontextmanager(get_user_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)


async def create_user(email: str, password: str,username: str,role_id: int, is_superuser: bool = True,is_active:bool = True,is_verified: bool = True):
    try:
        async with get_async_session_context() as session:
            async with get_user_db_context(session) as user_db:
                async with get_user_manager_context(user_db) as user_manager:
                    user = await user_manager.create(
                        UserCreate(
                            email=email, password=password, is_superuser=is_superuser,is_active=is_active,is_verified=is_verified,username=username,role_id=role_id
                        )
                    )
                    print(f"User created {user}")
    except UserAlreadyExists:
        print(f"User {email} already exists")