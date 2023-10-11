# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, String, Table
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
#sqlacodegen --tables books,authors,categories,bookauthors,bookcategories --outfile C:\SPTV21\hajusrakendus\ButorovSPTV21MVCBooks\Models\Models.py  --noindexes mysql+pymysql://root@localhost/books

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
