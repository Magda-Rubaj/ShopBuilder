from application.commands import CreateCategoryCommand, CreateProductCommand, CommandMapper
from config.container import Container
from dependency_injector.wiring import Provide, inject
from flask import Blueprint, request
from infrastructure.repos import CategoryRepository, ProductRepository
from integration.eventbus import EventBus



product_blueprint = Blueprint("product_blueprint", __name__)
category_blueprint = Blueprint("category_blueprint", __name__)


@product_blueprint.route("/products/create", methods=["POST"])
@inject
def add_product(
    command_mapper: CommandMapper = Provide[Container.command_mapper],
    repo: ProductRepository = Provide[Container.product_repository],
    publisher: EventBus = Provide[Container.rabbit_publisher],
):
    command = CreateProductCommand(**request.json)
    command_mapper.execute_command(command, repo, publisher)
    return "OK", 201


@product_blueprint.route("/categories/create", methods=["POST"])
@inject
def add_category(
    command_mapper: CommandMapper = Provide[Container.command_mapper],
    repo: CategoryRepository = Provide[Container.category_repository],
):
    command = CreateCategoryCommand(**request.json)
    command_mapper.execute_command(command, repo)
    return "OK", 201


# @product_blueprint.route("/products/test", methods=["POST"])
# @inject
# def test(command_mapper: CommandMapper = Provide[Container.command_mapper],
#     repo: CategoryRepository = Provide[Container.category_repository]):
#     publisher = RabbitMQEventPublisher(prepare_channel())
#     repo.insert(Category(name="dsdfsd"))
#     return "k"