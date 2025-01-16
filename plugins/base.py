from abc import ABC, abstractmethod
from typing import Any

class BasePlugin(ABC):
    @abstractmethod
    async def initialize(self) -> None:
        """Initialize plugin resources"""
        pass
    
    @abstractmethod
    async def cleanup(self) -> None:
        """Cleanup plugin resources"""
        pass
    
    @abstractmethod
    def get_app_config(self) -> dict[str, Any]:
        """Get plugin configuration for FastAPI app"""
        pass