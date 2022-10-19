from sqlalchemy import (
    ForeignKey,
    Table,
    MetaData,
    Column,
    Integer,
    String,
    Float
)
from domain.entities import Product, Category
from sqlalchemy.orm import mapper

metadata = MetaData()

products = Table(
    "products",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(64)),
    Column("price", Float),
    Column("stock", Integer),
    Column("description", String(256)),
)


categories = Table(
    "categories",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(64)),
    Column("parent", ForeignKey("categories.id")),
    Column("level", Integer),
)


def begin_mapping():
    mapper(Product, products)
    mapper(Category, categories)