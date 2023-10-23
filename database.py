from typing import Generator, AsyncGenerator
import aiomysql
import pymysql
from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import Column, String, ForeignKey, Boolean, create_engine
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from Models.Models import Base, role

SQLALCHEMY_URL = 'mysql+aiomysql://root@localhost/books'
SQLALCHEMY_URL2 = 'mysql+pymysql://root@localhost/books'


engine = create_engine(SQLALCHEMY_URL2)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

engine_async = create_async_engine(SQLALCHEMY_URL)
Session_async = sessionmaker(engine_async, class_=AsyncSession, expire_on_commit=False)

class User(SQLAlchemyBaseUserTable[int], Base):
    __table_args__ = {'extend_existing': True}
    user_id = Column(INTEGER(11), primary_key=True)
    email = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False)
    role_id = Column(ForeignKey(role.c.role_id), index=True)
    hashed_password = Column(String(150), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with Session_async() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
