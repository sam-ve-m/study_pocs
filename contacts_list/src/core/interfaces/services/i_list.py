from abc import ABC, abstractmethod
from typing import Any, Optional


class IList(ABC):
    @abstractmethod
    def get_list(self, optional_filter: Optional[Any] = None) -> dict:
        pass
