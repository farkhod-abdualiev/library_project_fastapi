from pydantic import BaseModel
from datetime import date
from typing import Optional
from uuid import UUID


class AuthorBase(BaseModel):
    full_name: str


class AuthorCreate(AuthorBase):
    pass


class AuthorUpdate(AuthorBase):
    pass


class Author(AuthorBase):
    id: int


    class Config:
        from_atributes = True


class BookBase(BaseModel):
    title: str
    author_id: int
    description: Optional[str]
    isbn: Optional[str]
    published_date: date
    count: Optional[int]
    price: Optional[float]


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    pass


class Book(BookBase):
    id: int
    is_available: bool
    author: Author


    class Config:
        from_atributes = True 
