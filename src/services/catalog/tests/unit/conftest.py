import pytest
from domain.entities import Category, Product
from domain.value_objects import Price


@pytest.fixture
def root_category():
    return Category(name="root")


@pytest.fixture
def lower_lvl_category(root_category):
    return Category(name="lvl2", parent=root_category)


@pytest.fixture
def price():
    return Price(net_value=2000.0, gross_value=3000.0, currency="USD")


@pytest.fixture
def product(price, root_category):
    return Product(
        name="test product",
        price=price,
        image="some str",
        stock=300,
        category=root_category,
        description="this is regular product",
    )
