from fastapi import APIRouter

from .crud import create_user as cu
from .schemas import CreateUser

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
async def create_user(user: CreateUser):
    """
    Create a new user
    """
    return cu(user_in=user)
