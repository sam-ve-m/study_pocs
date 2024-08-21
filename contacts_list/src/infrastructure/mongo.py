import pymongo
from src.services.utils.env_config import config
from src.core.interfaces.infrastructure.i_mongo_infrastructure import IMongoDBInfrastructure


class MongoDBInfrastructure(IMongoDBInfrastructure):
    connection: any = None

    @staticmethod
    def get_connection(
            url: str = config("MONGO_HOST"),
            port=config("MONGO_PORT"),
            username: str = config("MONGO_USER"),
            password: str = config("MONGO_PASS")
    ) -> pymongo.MongoClient:
        try:
            host = f"mongodb://{username}:{password}@{url}:{port}"
            connection = pymongo.MongoClient(host)
            return connection
        except Exception as error:
            raise error

    @classmethod
    def get_singleton_connection(
            cls,
            url: str = config("MONGO_HOST"),
            port: int = config("MONGO_PORT"),
            username: str = config("MONGO_USER"),
            password: str = config("MONGO_PASS")
    ) -> pymongo.MongoClient:
        if cls.connection is None:
            cls.connection = cls.get_connection(url, port, username, password)
        return cls.connection
