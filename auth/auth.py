from fastapi_users.authentication import CookieTransport, AuthenticationBackend
from fastapi_users.authentication import JWTStrategy
from fastapi_users.db import SQLAlchemyUserDatabase
from Models.Models import user

from auth.schema import UserDB
from database import get_db

cookie_transport = CookieTransport(cookie_name="books", cookie_max_age=3600)

SECRET = "SECRET"

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


users = user.__le__
user_db = SQLAlchemyUserDatabase(UserDB, get_db, users)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)