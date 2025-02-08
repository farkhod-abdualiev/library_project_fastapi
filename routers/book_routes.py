from fastapi import APIRouter, Depends, UploadFile, File
from typing import Optional, List
from schemas import book_schemas
from sqlalchemy.orm import Session
from database import get_db
from crud import book, user


router = APIRouter(
    prefix="/books",
    tags=["books"]
)

@router.get("/", response_model=List[book_schemas.Book])
async def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return book.get_books(db, skip, limit)

@router.post("/", response_model=book_schemas.Book, dependencies=[Depends(user.get_current_active_staff_user)])
async def create_book(book_data: book_schemas.BookCreate, book_file: Optional[UploadFile] = File(None), db: Session = Depends(get_db)):
    return book.create_book(db, book_data, book_file)