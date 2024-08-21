from abc import ABC, abstractmethod
from typing import Any


class IRegister(ABC):
    @abstractmethod
    def register(self, value: Any) -> dict:
        pass
