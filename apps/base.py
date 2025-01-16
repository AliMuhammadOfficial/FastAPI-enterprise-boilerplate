from abc import ABC, abstractmethod
from typing import Any

class BaseApp(ABC):
    @abstractmethod
    def get_app_config(self) -> dict[str, Any]:
        """Get app configuration"""
        pass
    
    @abstractmethod
    async def startup(self) -> None:
        """Run startup tasks"""
        pass
    
    @abstractmethod
    async def shutdown(self) -> None:
        """Run shutdown tasks"""
        pass