from abc import ABC, abstractmethod


class IRedisInfrastructure(ABC):
    connection: any

    @staticmethod
    @abstractmethod
    def get_connection(url: str = None, port: int = None, password: str = None, db: int = 0) -> any:
        pass

    @classmethod
    @abstractmethod
    def get_singleton_connection(cls, url: str = None, port: int = None, password: str = None, db: int = 0) -> any:
        pass
