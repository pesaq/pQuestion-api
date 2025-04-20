from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from typing import Sequence

from core.models import User

from api.api_v1.schemas.users import *

from api.api_v1.secure import pwd_context

async def register_user(
    session: AsyncSession,
    user_create: UserCreateSchema
) -> User:
    if await session.scalar(select(User).where(User.username == user_create.username)):
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail='User with this username already exists!'
        )
    user = User(**user_create.model_dump())
    user.password = pwd_context.hash(user_create.password)
    session.add(user)
    await session.commit()

    return user