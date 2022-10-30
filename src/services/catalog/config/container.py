from dependency_injector import containers, providers
from infrastructure.repos import ProductRepository, CategoryRepository
from application.commands import CommandMapper
from config.db import get_session
from config.rabbitmq import prepare_channel
from integration.eventbus import RabbitMQEventBus


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    wiring_config = containers.WiringConfiguration(
        modules=["api.routes"]
    )
    session = providers.Singleton(get_session)
    rabbit_channel = providers.Singleton(prepare_channel)
    command_mapper = providers.Factory(CommandMapper)
    product_repository = providers.Factory(
        ProductRepository, session=session
    )
    category_repository = providers.Factory(
        CategoryRepository, session=session
    )
    rabbit_publisher = providers.Factory(
        RabbitMQEventBus, channel=rabbit_channel
    )