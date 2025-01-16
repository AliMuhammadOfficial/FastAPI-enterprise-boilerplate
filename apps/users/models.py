from sqlmodel import SQLModel, Field
from datetime import datetime

class User(SQLModel, table=True):
    id: int = Field(primary_key=True)
    username: str = Field(unique=True)
    email: str = Field(unique=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

