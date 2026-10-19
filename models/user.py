
from sqlalchemy import String, Integer, DateTime, Enum
from sqlalchemy.orm import mapped_column, Mapped
from datetime import datetime, timezone
from enums.user_status import UserStatus
from models.base import Base

class User(Base):

    __tablename__='users'

    id: Mapped[int] = mapped_column(
        Integer, 
        primary_key=True
    )
    
    username: Mapped[str] = mapped_column(
        String(128), 
        nullable=False, 
        unique=True
    )

    email: Mapped[str] = mapped_column(
        String(128), 
        nullable=False, 
        unique=True
    )

    password_hash: Mapped[str] = mapped_column(
        String(512), 
        nullable=False
    ) 

    status: Mapped[UserStatus] = mapped_column(
        Enum(UserStatus), 
        nullable=False, 
        default=UserStatus.ACTIVE)
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        nullable=False,
        default= lambda: datetime.now(timezone.utc)
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        nullable=False,
        default= lambda: datetime.now(timezone.utc),
        onupdate= lambda: datetime.now(timezone.utc)
    )
