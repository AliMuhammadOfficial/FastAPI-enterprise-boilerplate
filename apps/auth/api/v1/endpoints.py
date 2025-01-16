from fastapi import APIRouter


router = APIRouter()


@router.post("/")
async def login():
    return {"message": "User logged in successfully"}
