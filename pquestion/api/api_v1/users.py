from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from .schemas.users import *

from .crud import users

from core.models.db_helper import db_helper

from typing import Annotated

router = APIRouter(tags=['Users'])

@router.post('/register/', response_model=LiteUserSchema)
async def register_user(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter)
    ],
    user: UserCreateSchema
):
    return await users.register_user(session, user)