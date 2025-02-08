import os
from uuid import uuid4 
from fastapi import UploadFile


UPLOAD_DIRECTORY = 'book_files'

def save_file(book_file: UploadFile) -> str:
    if not os.path.exists(UPLOAD_DIRECTORY):
        os.makedirs(UPLOAD_DIRECTORY)
    
    file_extension = book_file.filename.split(".")[-1]
    file_name = f"{uuid4()}.{file_extension}"
    file_path = os.path.join(UPLOAD_DIRECTORY, file_name)

    with open(file_path, "wb") as buffer:
        buffer.write(book_file.file.read())
    
    return file_path