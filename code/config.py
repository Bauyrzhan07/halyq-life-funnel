from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    debug: bool = True
    database_url: PostgresDsn
    redis_url: str
    admin_logo_url: str = (
        "https://www.halyklife.kz/themes/halyk/assets/images/svg/logo.svg"
    )
    login_logo_url: str = (
        "https://www.halyklife.kz/themes/halyk/assets/images/svg/logo.svg"
    )
    favicon_url: str = (
        "https://www.halyklife.kz/themes/halyk/assets/favicon/favicon-32x32.png"
    )


settings = Settings()

TORTOISE_CONFIG = {
    "connections": {"default": str(settings.database_url)},
    "apps": {
        "models": {
            "models": ["aerich.models", "code.models"],
            "default_connection": "default",
        },
    },
}
