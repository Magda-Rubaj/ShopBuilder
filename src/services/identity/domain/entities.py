from dataclasses import dataclass
import secrets


@dataclass
class Guest:
    key: str = None

    def generate_key(self) -> str:
        return secrets.token_urlsafe(16)
