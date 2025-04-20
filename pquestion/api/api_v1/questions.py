from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from .schemas.questions import *

from .crud import questions
from core.models.db_helper import db_helper

from utils.question import get_moscow_time

from typing import Annotated

from datetime import datetime

router = APIRouter(tags=['Questions'])

@router.get('/get-lasted-questions/')
async def get_lasted_questions(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter)
    ],
    payload: Annotated[QuestionsReadSchema, Depends()]
):
    questions_list = await questions.get_lasted_questions(session, limit=payload.limit)
    return {'data': questions_list}

@router.get('/get-question/')
async def get_question(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter)
    ],
    payload: Annotated[QuestionReadSchema, Depends()]
):
    question = await questions.get_question(session, payload.id)
    return {'data': question}

@router.post('/add-question/')
async def add_question(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter)
    ],
    current_moscow_time: Annotated[
        datetime,
        Depends(get_moscow_time)
    ],
    question: QuestionCreateSchema
):
    new_question = await questions.add_question(session, question, time_create=current_moscow_time)
    return {'ok': True, 'question': new_question}