from fastapi import APIRouter

from core.config import settings

from .users import router as users_router
from .questions import router as question_router

router = APIRouter()

router.include_router(
    users_router,
    prefix=settings.api.v1.users
)
router.include_router(
    question_router,
    prefix=settings.api.v1.questions
)