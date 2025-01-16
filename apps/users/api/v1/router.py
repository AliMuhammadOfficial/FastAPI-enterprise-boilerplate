from fastapi import APIRouter
from . import endpoints

router = APIRouter(prefix="/users")

router.include_router(endpoints.router)