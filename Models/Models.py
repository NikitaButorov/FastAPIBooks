# coding: utf-8
from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, String, Table, Text, Integer, TIMESTAMP, Boolean, JSON
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Author(Base):
    __tablename__ = 'authors'

    author_id = Column(INTEGER(11), primary_key=True)
    author_name = Column(String(50))

    books = relationship('Book',cascade="all, delete",passive_deletes=True, secondary='bookauthors')


class Book(Base):
    __tablename__ = 'books'

    id = Column(INTEGER(11), primary_key=True)
    title = Column(String(50))
    isbn = Column(String(50))
    pageCount = Column(INTEGER(11))
    publishedDate = Column(DateTime)
    thumbnailUrl = Column(String(100))
    shortDescription = Column(String(500))
    longDescription = Column(String(1000))
    status = Column(String(50))

    categorys = relationship('Category',cascade="all, delete", passive_deletes=True, secondary='bookcategories')


class Category(Base):
    __tablename__ = 'categories'

    category_id = Column(INTEGER(11), primary_key=True)
    category_name = Column(String(50))


t_bookauthors = Table(
    'bookauthors', metadata,
    Column('book_id', ForeignKey('books.id', ondelete="CASCADE")),
    Column('author_id', ForeignKey('authors.author_id', ondelete="CASCADE"))
)


t_bookcategories = Table(
    'bookcategories', metadata,
    Column('book_id', ForeignKey('books.id', ondelete="CASCADE")),
    Column('category_id', ForeignKey('categories.category_id', ondelete="CASCADE"))
)



role = Table(
    "role",
    metadata,
    Column("role_id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)

user = Table(
    "user",
    metadata,
    Column("user_id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("role_id", Integer, ForeignKey(role.c.role_id)),
    Column("hashed_password", String, nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
)