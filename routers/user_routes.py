from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from fastapi.security import OAuth2PasswordRequestForm
from crud import user
from uuid import UUID
from schemas import user_schemas
from typing import List



router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.get("/", response_model=List[user_schemas.User], dependencies=[Depends(user.get_current_active_staff_user)])
async def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return user.get_users(db, skip, limit)

@router.post("/", response_model=user_schemas.User)
async def create_user(user_data: user_schemas.UserCreate, db: Session = Depends(get_db)):
    return user.create_user(db, user_data)

@router.get("/me", response_model=user_schemas.User)
async def read_user_me(current_user: user_schemas.User = Depends(user.get_current_user)):
    return current_user

@router.put("/me", response_model=user_schemas.User)
async def update_user_me_put(current_user: user_schemas.User = Depends(user.get_current_user)):
    return current_user

@router.patch("/me", response_model=user_schemas.User)
async def update_user_me_patch(current_user: user_schemas.User = Depends(user.get_current_user)):
    return current_user

@router.delete("/me", response_model=user_schemas.User)
async def delete_user_me(current_user: user_schemas.User = Depends(user.get_current_user)):
    return current_user

@router.get("/{user_id}", response_model=user_schemas.User, dependencies=[Depends(user.get_current_active_staff_user)])
async def read_user(user_id: UUID, db: Session = Depends(get_db)):
    return user.get_user(db, user_id)

@router.put("/{user_id}", response_model=user_schemas.User, dependencies=[Depends(user.get_current_active_staff_user)])
async def update_user_put(user_id: UUID, user_data: user_schemas.UserUpdate, db: Session = Depends(get_db)):
    return user.update_user(db, user_id, user_data)

@router.patch("/{user_id}", response_model=user_schemas.User, dependencies=[Depends(user.get_current_active_staff_user)])
async def update_user_patch(user_id: UUID, user_data: user_schemas.UserUpdate, db: Session = Depends(get_db)):
    return user.update_user(db, user_id, user_data)

@router.delete("/{user_id}", response_model=user_schemas.User, dependencies=[Depends(user.get_current_active_staff_user)])
def delete_user(user_id: UUID, db: Session = Depends(get_db)):
    return user.delete_user(db=db, user_id=user_id)

@router.post("/token", response_model=user_schemas.Token)
def login_for_access_token(user_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = user.authenticate_user(db, user_schemas.USerSignIn(phone_number=user_data.username,password=user_data.password))
    access_token = user.create_access_token({"sub": db_user.phone_number})
    refresh_token = user.create_refresh_token({"sub": db_user.phone_number})
    return {
        "access_token": access_token, 
        "refresh_token": refresh_token,
        "token_type": "Bearer"
    }   

@router.get("/verify-token/")
async def verify_user_token(token: str):
    user.verify_token(token)
    return {
        'success': True,
        "message": "Token is valid"
    }