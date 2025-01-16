"""FastAPI Application Main Module.

This module serves as the entry point for the FastAPI application, handling all bootstrap
operations and core configurations. It initializes the FastAPI application instance,
registers all apps/routes, middleware, plugins, and event handlers.

Key Features:
    - Application initialization and configuration
    - Router registration and API endpoint setup
    - Database connection management
    - Middleware configuration
    - Exception handlers setup

Note:
    Ensure all environment variables are properly set before running the application.
    Refer to the project documentation for required configurations.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from settings import INSTALLED_APPS, settings
from registry import registry
from plugins.cache.backend import CachePlugin


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize plugins
    await registry.initialize()
    yield
    # Cleanup
    await registry.cleanup()


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
        lifespan=lifespan,
    )

    ####### CORS Middleware and Configuration ######
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.BACKEND_CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    ###### End CORS Middleware and Configuration ######
    
    ###### App registration ######
    for app_name, app_module in INSTALLED_APPS.items():
        module = __import__(app_module, fromlist=["router"])
        app.include_router(
            module.router, prefix=settings.API_V1_STR, tags=[app_name]
        )
    ###### End App registration ######

    ###### Register plugins based on configuration ######
    if settings.ENABLE_CACHE and settings.REDIS_URL:
        registry.register_plugin("cache", CachePlugin(settings.REDIS_URL))

    if settings.ENABLE_EVENTS:
        pass
        # registry.register_plugin("events", EventPlugin(settings.KAFKA_BROKERS))
    ###### End Register plugins based on configuration ######
    
    return app


app = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)