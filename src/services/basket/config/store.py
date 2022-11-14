import aioredis
import os


def setup_store():
    redis = aioredis.from_url(os.environ.get("REDIS_URL"))
    return redis