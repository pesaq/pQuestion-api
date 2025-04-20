from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import UniqueConstraint
from .base import Base

class User(Base):

    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[bytes] = mapped_column()

    is_active: Mapped[bool] = mapped_column(default=True)