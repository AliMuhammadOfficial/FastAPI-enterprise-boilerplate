from fastapi import APIRouter
from . import endpoints

router = APIRouter(prefix="/auth")

router.include_router(endpoints.router)