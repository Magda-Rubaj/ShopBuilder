from typing import Literal
from pydantic import BaseModel


class CategoryPost(BaseModel):
    name: str


class Price(BaseModel):
    currency: Literal["USD", "PLN", "EUR"]
    net_value: float
    gross_value: float


class PartPrice(BaseModel):
    currency: Literal["USD", "PLN", "EUR"]
    value: float


class BasketItemPost(BaseModel):
    name: str
    price: PartPrice
    quantity: int
    attributes: dict


class ProductPost(BaseModel):
    name: str
    price: Price
    image: str
    stock: int
    description: str
    category: int