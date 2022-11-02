from pydantic import BaseSettings, Field


class AppConfig(BaseSettings):
    secret_key: str = Field(env="SECRET_KEY")
    amqp_url: str = Field(env="AMQP_URL")

    class Config:
        env_file = ".env"


config = AppConfig()
