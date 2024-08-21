from abc import ABC, abstractmethod
from typing import Any


class IUpdate(ABC):
    @abstractmethod
    def update(self, identity: str, updates: Any) -> dict:
        pass
