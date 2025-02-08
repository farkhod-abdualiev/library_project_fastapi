from database import Base
from sqlalchemy import Column, String, Integer, Text, Date, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer,primary_key=True, index=True, autoincrement=True)
    full_name = Column(String, index=True)
    books = relationship("Book", back_populates="author")

    def __repr__(self):
        return f'<Author(full_name={self.full_name})>'


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship("Author", back_populates="books")
    description = Column(Text, nullable=True)
    isbn = Column(String, nullable=True, unique=True)
    published_date = Column(Date)
    count = Column(Integer, default=0)
    price = Column(Float, default=0.0)
    file_path = Column(String, nullable=True)
    is_available = Column(Boolean, default=True)

    def __repr__(self):
        return f'<Book(title={self.title}, author_id={self.author_id})>'

