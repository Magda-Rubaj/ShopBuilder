from application.commands import CreateProductCommand, CommandMapper
from config.container import Container
from dependency_injector.wiring import Provide, inject
from flask import Blueprint, request
from infrastructure.repos import ProductRepository

product_blueprint = Blueprint("product_blueprint", __name__)


@product_blueprint.route("/products/create", methods=["POST"])
@inject
def add_product(
    command_mapper: CommandMapper = Provide[Container.command_mapper],
    repo: ProductRepository = Provide[Container.product_repository],
):
    command = CreateProductCommand(**request.data)
    command_mapper.execute_command(command, repo)
    return "OK", 201
