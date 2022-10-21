
from dataclasses import dataclass
from typing import Literal


@dataclass
class ValueObject:
    ...


@dataclass
class Address(ValueObject):
    country: str
    city: str
    street: str
    zip_code: str


@dataclass
class Price:
    value: float
    currency: Literal["USD", "EUR", "PLN"]