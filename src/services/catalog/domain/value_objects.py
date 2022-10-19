
from dataclasses import dataclass
from typing import Literal


@dataclass
class ValueObject:
    pass


@dataclass
class Price(ValueObject):
    net_value: float
    gross_value: float
    currency: Literal["USD", "PLN", "EUR"]
