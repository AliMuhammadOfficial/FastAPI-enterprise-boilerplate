from core.config.base import settings

# Import settings instance to make it available project-wide
__all__ = ['settings', 'INSTALLED_APPS']

# Define installed apps
INSTALLED_APPS = {
    "auth": "apps.auth",
    "users": "apps.users",
}
