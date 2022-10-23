
from dataclasses import dataclass
from typing import Literal


@dataclass
class ValueObject:
    pass


@dataclass
class Price(ValueObject):
    currency: Literal["USD", "PLN", "EUR"]
    net_value: float = None
    gross_value: float = None
