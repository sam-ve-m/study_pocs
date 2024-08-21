from abc import ABC, abstractmethod
from typing import Any


class IDetail(ABC):
    @abstractmethod
    def get_detail(self, value: Any) -> dict:
        pass
