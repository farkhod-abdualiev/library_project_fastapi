import uuid
from database import Base
from sqlalchemy.sql import func
from sqlalchemy import (
    Column,
    String,
    Boolean,
    Text,
    DateTime
)


class User(Base):
    __tablename__ = "users"
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    phone_number = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=False) 
    address = Column(Text)
    date_joined = Column(DateTime(timezone=True), server_default=func.now())
    is_active = Column(Boolean, default=True)
    is_staff = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

