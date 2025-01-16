from pydantic import BaseModel


class CacheConfig(BaseModel):
    enabled: bool
    url: str
