from sqlalchemy.orm import Session
from database import engine, Base, get_db
from models import User, Book, Author
from crud.user import get_password_hash


def create_initial_users(db: Session):
    admin_password = get_password_hash("admin".encode("utf-8"))
    admin = User(
        first_name="Admin",
        phone_number="+998901234567",
        email="admin@example.com",
        hashed_password=admin_password,
        is_active=True,
        is_staff=True,
        is_superuser=True
    )
    db.add(admin)
    db.commit()
    db.refresh(admin)
    
    user_password = get_password_hash("user".encode("utf-8"))
    user = User(
        first_name="User",
        phone_number="+998901234568",
        email="user@example.com",
        hashed_password=user_password,
        is_active=True,
        is_staff=False,
        is_superuser=False
    )
    db.add(user)
    db.commit()
    db.refresh(user)

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
    print("Database yaratildi!")
    db = next(get_db())
    create_initial_users(db)
    print("Foydalanuvchilar yaratildi!")
