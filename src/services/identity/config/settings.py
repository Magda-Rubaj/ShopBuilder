from functools import lru_cache
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    redis_url: str = Field(env="REDIS_URL")

@lru_cache
def get_settings() -> Settings:
    return Settings()
