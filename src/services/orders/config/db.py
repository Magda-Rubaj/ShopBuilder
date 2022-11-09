import os
from pymongo import MongoClient


def setup_db() -> MongoClient:
    mongo_url = os.environ.get("DB_URL")
    mongodb_client = MongoClient(mongo_url)
    dbname = os.environ.get("DB_NAME")
    db = mongodb_client[dbname]
    return db


