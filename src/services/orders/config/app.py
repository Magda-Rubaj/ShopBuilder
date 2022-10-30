from pydantic import BaseSettings, Field


class AppConfig(BaseSettings):
    secret_key: str = Field(env="SECRET_KEY")

    class Config:
        env_file = ".env"


config = AppConfig()
