from flask import Blueprint
from application.commands import CreateProductCommand, create_product
from infrastructure.repos import ProductRepository
from config.db import get_session


product_blueprint = Blueprint("product_blueprint", __name__)


@product_blueprint.route('/products/create', methods=["GET"])
def add_product():
    command = CreateProductCommand(
        name="test",
        price=10.0,
        image="fsdfsdf",
        stock=100,
        description="sdfsdf"
    )
    repo = ProductRepository(get_session())
    create_product(command, repo)
    return ""