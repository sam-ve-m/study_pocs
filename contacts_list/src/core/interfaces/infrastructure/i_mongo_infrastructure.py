from abc import ABC, abstractmethod


class IMongoDBInfrastructure(ABC):
    connection: any

    @staticmethod
    @abstractmethod
    def get_connection(url: str, port: int, username: str, password: str) -> any:
        pass

    @classmethod
    @abstractmethod
    def get_singleton_connection(cls, url: str, port: int, username: str, password: str) -> any:
        pass
