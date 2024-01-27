from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    debug: bool = True
    database_url: PostgresDsn
    redis_url: str
    admin_logo_url: str = "https://preview.tabler.io/static/logo-white.svg"
    login_logo_url: str = "https://preview.tabler.io/static/logo.svg"


settings = Settings()

TORTOISE_CONFIG = {
    'connections': {'default': str(settings.database_url)},
    'apps': {
        'models': {
            'models': ['aerich.models', 'code.models'],
            'default_connection': 'default',
        },
    },
}
