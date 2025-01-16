from typing import Dict, Any
from fastapi import FastAPI
from plugins.base import BasePlugin


class ApplicationRegistry:
    def __init__(self):
        self._apps: Dict[str, Any] = {}
        self._plugins: Dict[str, BasePlugin] = {}
        self._initialized: bool = False

    def register_app(self, name: str, app_module: Any) -> None:
        if self._initialized:
            raise RuntimeError("Cannot register app after initialization")
        self._apps[name] = app_module

    def register_plugin(self, name: str, plugin: BasePlugin) -> None:
        if self._initialized:
            raise RuntimeError("Cannot register plugin after initialization")
        self._plugins[name] = plugin

    async def initialize(self) -> None:
        if self._initialized:
            return

        # Initialize plugins
        for plugin in self._plugins.values():
            await plugin.initialize()

        self._initialized = True

    async def cleanup(self) -> None:
        for plugin in self._plugins.values():
            await plugin.cleanup()
        self._initialized = False

    @property
    def apps(self) -> Dict[str, Any]:
        return self._apps

    @property
    def plugins(self) -> Dict[str, BasePlugin]:
        return self._plugins


registry = ApplicationRegistry()
