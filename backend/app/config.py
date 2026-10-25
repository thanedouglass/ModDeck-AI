from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    twitch_client_id: str = ""
    twitch_client_secret: str = ""
    twitch_webhook_secret: str = ""
    openai_api_key: str = ""

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
