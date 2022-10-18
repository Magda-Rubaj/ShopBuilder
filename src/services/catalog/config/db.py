import os
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

load_dotenv()
db_name = os.environ.get("DBNAME")
db_user = os.environ.get("DBUSER")
db_password = os.environ.get("DBPASSWORD")
db_str = f"postgresql://{db_user}:{db_password}@localhost:5432/{db_name}"
Base = declarative_base()
Session = sessionmaker(bind=create_engine(db_str))


def get_session() -> Session:
    session = Session()
    try:
        return session
    except Exception:
        print(Exception)
        session.rollback()
    finally:
        session.close()