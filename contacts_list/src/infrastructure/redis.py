from redis.client import Redis

from src.core.interfaces.infrastructure.i_redis_infrastructure import IRedisInfrastructure
from src.services.utils.env_config import config


class RedisKeyDBInfrastructure(IRedisInfrastructure):
    connection: any = None

    @staticmethod
    def get_connection(
            url: str = config("REDIS_HOST"),
            port: int = config("REDIS_PORT"),
            password: str = config("REDIS_PASS"),
            db: int = config("REDIS_DB")
    ) -> Redis:
        try:
            connection = Redis(host=url, port=port, password=password, db=db)
            return connection
        except Exception as error:
            raise error

    @classmethod
    def get_singleton_connection(
            cls,
            url: str = config("REDIS_HOST"),
            port: int = config("REDIS_PORT"),
            password: str = config("REDIS_PASS"),
            db: int = config("REDIS_DB")
    ) -> Redis:
        if cls.connection is None:
            cls.connection = cls.get_connection(url, port, password, db)
        return cls.connection
