import aioredis
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    redis_url: str = Field(env="REDIS_URL")

    @property
    def redis_instance(self):
        return aioredis.from_url(self.redis_url)
