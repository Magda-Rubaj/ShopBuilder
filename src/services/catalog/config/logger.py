import logging
from logging.config import dictConfig


dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "default",
            }
        },
        "loggers": {
            "CatalogLogger": {"handlers": ["console"], "level": "DEBUG"},
        }
    }
)

logger = logging.getLogger("CatalogLogger")