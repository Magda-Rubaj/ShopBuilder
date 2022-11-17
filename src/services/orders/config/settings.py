from pydantic import BaseSettings, Field
from pymongo import MongoClient


class Settings(BaseSettings):
    secret_key: str = Field(env="SECRET_KEY")
    amqp_url: str = Field(env="AMQP_URL")
    mongo_url: str = Field(env="DB_URL")
    db_name: str = Field(env="DB_NAME")

    @property
    def mongo_client(self) -> MongoClient:
        mongodb_client = MongoClient(self.mongo_url)
        return mongodb_client[self.db_name]
