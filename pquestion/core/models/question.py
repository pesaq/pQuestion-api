from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, Column
from .base import Base

class Question(Base):

    title: Mapped[str] = mapped_column()
    content: Mapped[str] = mapped_column()
    time_create = Column(DateTime(timezone=True))

    #user

class Answer(Base):
    #question

    text: Mapped[str] = mapped_column()
    time_create = Column(DateTime(timezone=True))

    #user