from typing import Any
from redis.asyncio import Redis

from plugins.base import BasePlugin
from .config import CacheConfig


class CachePlugin(BasePlugin):
    def __init__(self, url: str):
        self.url = url
        self.redis: Redis | None = None

    async def initialize(self) -> None:
        self.redis = Redis.from_url(self.url)

    async def cleanup(self) -> None:
        if self.redis:
            await self.redis.close()

    def get_app_config(self) -> dict[str, Any]:
        return {
            "cache": CacheConfig(
                enabled=True,
                url=self.url
            )
        }
