from dataclasses import dataclass
from typing import Literal


@dataclass
class Price:
    currency: Literal["USD", "PLN", "EUR"]
    value: float
