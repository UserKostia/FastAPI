from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from api_v1 import router as router_v1
from core.config import settings
from core.models import Base, db_helper
from items_views import router as items_router
from users.views import router as users_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan event handler for the FastAPI application.

    This function is called when the application starts and stops.
    It creates the database tables on startup and does nothing on shutdown.
    """
    async with db_helper.engine.begin() as conn:  # Connect to the database
        await conn.run_sync(
            Base.metadata.create_all
        )  # Create tables if they don't exist

    yield  # Yield control back to the application


app = FastAPI(lifespan=lifespan)  # Create the FastAPI app with the lifespan handler

# Include routers for different parts of the API
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)
app.include_router(items_router)
app.include_router(users_router)


@app.get("/")
async def index_greetings():
    """
    Endpoint for the root path '/' of the API.
    Returns a simple greeting message.
    """
    return {"Hello": "User!"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
