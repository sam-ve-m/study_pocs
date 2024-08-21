from abc import ABC, abstractmethod
from typing import Any


class IDelete(ABC):
    @abstractmethod
    def delete(self, value: Any) -> bool:
        pass
