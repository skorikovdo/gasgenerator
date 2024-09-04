from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

ENV = Path(__file__).parent / ".env"


class Settings(BaseSettings):
    DEBUG: bool

    # Token settings
    SECRET_KEY: str
    SECRET_KEY_REFRESH: str
    ALGORITHM: str
    ACCESS_TOKEN_LIFETIME_MINUTE: int
    REFRESH_TOKEN_LIFETIME_MINUTE: int

    model_config = SettingsConfigDict(env_file=ENV)


settings = Settings()
