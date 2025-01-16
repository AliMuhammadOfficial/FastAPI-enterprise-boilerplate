from fastapi import Depends

from apps.users.schemas import UserCreate
from .models import User

def get_session():
    pass

class UserService:
    def __init__(self):
        pass
    
    async def create_user(self, data: UserCreate) -> User:
        user = User(**data.model_dump(exclude={'password'}))
        return user