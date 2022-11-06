import logging
from pydantic import BaseModel
from logging.config import dictConfig


class LogConfig(BaseModel):
    """Logging configuration"""

    LOGGER_NAME: str = "OrdersLogger"
    LOG_FORMAT: str = "%(levelprefix)s [%(asctime)s] | %(filename)s: %(message)s"
    LOG_LEVEL: str = "DEBUG"

    version = 1
    disable_existing_loggers = False
    formatters = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
    }
    loggers = {
        "OrdersLogger": {"handlers": ["default"], "level": LOG_LEVEL},
    }


log_config = LogConfig()
dictConfig(log_config.__dict__)
logger = logging.getLogger("OrdersLogger")