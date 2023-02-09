from dependency_injector import containers, providers
from infrastructure.repos import ProductRepository, CategoryRepository
from application.commands import CommandMapper
from config.settings import Settings, get_session, get_channel
from integration.eventbus import RabbitMQEventBus


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    wiring_config = containers.WiringConfiguration(
        modules=["api.routes"]
    )
    settings = providers.Singleton(Settings)
    session = providers.Singleton(get_session, db_url=settings.provided.DB_URL)
    rabbit_channel = providers.Resource(
        get_channel, amqp_url=settings.provided.AMQP_URL
    )
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