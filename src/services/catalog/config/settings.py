
from sqlalchemy.orm import sessionmaker
from pydantic import BaseSettings, Field
from config.logger import logger
from aio_pika import connect, Channel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


Base = declarative_base()


class Settings(BaseSettings):
    SECRET_KEY: str = Field(env="SECRET_KEY")
    AMQP_URL: str = Field(env="AMQP_URL")
    DB_NAME: str = Field(env="DBNAME")
    DB_USER: str = Field(env="DBUSER")
    DB_PASSWORD: str = Field(env="DBPASSWORD")
    DB_URL: str = Field(env="DBURL")


def get_session(db_url: str) -> Session:
    session = sessionmaker(bind=create_engine(db_url))()
    try:
        return session
    except Exception:
        logger.error("Exception occured, rolling back")
        session.rollback()
    finally:
        session.close()
    

async def get_channel(amqp_url: str) -> Channel:
    connection = await connect(amqp_url)
    async with connection:
        channel = await connection.channel()
        return await channel



     
