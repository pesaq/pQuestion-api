from fastapi import FastAPI
#from fastapi.responses import ORJSONResponse
import uvicorn

from contextlib import asynccontextmanager

from core.config import settings

from api import router as api_router
from core.models import db_helper

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield

    # shutdown
    await db_helper.dispose()

app = FastAPI(
    #default_response_class=ORJSONResponse,
    lifespan=lifespan
)

app.include_router(api_router, prefix=settings.api.prefix)

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=settings.run.host,
        port=settings.run.port,
        reload=True
    )