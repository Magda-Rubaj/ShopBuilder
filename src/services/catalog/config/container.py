from dependency_injector import containers, providers
from infrastructure.repos import ProductRepository
from config.db import get_session


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()