from pydantic import BaseModel

class Book(BaseModel):
    title: str
    isbn: int
    pageCount: int
    thumbnailUrl: str
    shortDescription: str
    longDescription: str
    status: str
