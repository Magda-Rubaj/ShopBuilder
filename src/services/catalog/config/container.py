from dependency_injector import containers, providers
from infrastructure.repos import ProductRepository, CategoryRepository
from application.commands import CommandMapper
from config.db import get_session


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    wiring_config = containers.WiringConfiguration(
        modules=["api.routes"]
    )
    session = providers.Singleton(get_session)
    command_mapper = providers.Factory(CommandMapper)
    product_repository = providers.Factory(
        ProductRepository, session=session
    )
    category_repository = providers.Factory(
        CategoryRepository, session=session
    )