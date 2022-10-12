from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Session = sessionmaker(bind=create_engine(""))
Base = declarative_base()


def get_session() -> Session:
    session = Session()
    try:
        return session
    except:
        session.rollback()
    finally:
        session.close()