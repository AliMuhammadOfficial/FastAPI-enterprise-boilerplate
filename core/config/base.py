from typing import List
from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """
    Application settings and configuration.
    All settings can be overridden by environment variables.
    """
    # Core settings
    PROJECT_NAME: str = "FastAPI App"
    DEBUG: bool = False
    API_V1_STR: str = "/api/v1"
    
    # CORS
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:8000"]
    
    # Database
    DATABASE_URL: str = "postgresql+asyncpg://user:pass@localhost/dbname"
    
    # Feature flags
    ENABLE_CACHE: bool = False
    ENABLE_EVENTS: bool = False
    ENABLE_SEARCH: bool = False
    
    # External services
    REDIS_URL: str | None = None
    KAFKA_BROKERS: List[str] | None = None
    ELASTICSEARCH_URL: str | None = None

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache
def get_settings() -> Settings:
    """Create cached settings instance."""
    return Settings()


settings = get_settings()
