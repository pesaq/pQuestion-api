from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from typing import Sequence

from core.models import Question

from api.api_v1.schemas.questions import *

async def get_lasted_questions(
    session: AsyncSession,
    limit: int = 20
) -> Sequence[Question]:
    stmt = select(Question).order_by(Question.time_create).limit(limit)
    result = await session.scalars(stmt)
    return result.all()

async def get_question(
    session: AsyncSession,
    id: int
) -> Question:
    stmt = select(Question).where(Question.id == id)
    result = await session.execute(stmt)
    return result.scalar_one_or_none()

async def add_question(
    session: AsyncSession,
    question_create: QuestionBase,
    time_create
) -> Question:
    question = Question(**question_create.model_dump(), time_create=time_create)
    session.add(question)
    await session.commit()
    # await session.refresh(question)
    return question