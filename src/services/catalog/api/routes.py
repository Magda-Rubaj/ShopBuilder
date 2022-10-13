from flask import Blueprint

product_blueprint = Blueprint("product_blueprint", __name__)


@product_blueprint.route('/products/create')
def add_product():
    return ""