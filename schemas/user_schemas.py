from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from uuid import UUID


class UserBase(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    phone_number: str
    email: Optional[EmailStr]
    address: Optional[str]


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    pass


class User(UserBase):
    id: UUID
    date_joined: datetime

    class Config:
        from_atributes = True


class USerSignIn(BaseModel):
    phone_number: str
    password: str


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str
