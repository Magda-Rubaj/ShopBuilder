from sqlalchemy import (
    ForeignKey,
    Table,
    MetaData,
    Column,
    Integer,
    String,
    Float,
)
from domain.entities import Product, Category
from sqlalchemy.orm import mapper
from sqlalchemy.dialects.postgresql import JSONB


metadata = MetaData()


products = Table(
    "products",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(64)),
    Column("price", JSONB),
    Column("stock", Integer),
    Column("description", String(256)),
    Column("category", ForeignKey("categories.id")),
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