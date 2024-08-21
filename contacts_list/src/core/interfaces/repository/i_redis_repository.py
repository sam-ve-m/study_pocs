from abc import ABC
from typing import Type

from redis.client import Redis
from redis.exceptions import ConnectionError

from src.core.interfaces.infrastructure.i_redis_infrastructure import IRedisInfrastructure


class IRedis(ABC):
    def __init__(self, infrastructure: Redis):
        connection: Redis = infrastructure
        self.connection = connection

    def insert(self, key: str) -> bool:
        try:
            self.connection.set(key, 1)
            return True
        except ConnectionError:
            return False

    def exclude(self, key: str) -> bool:
        try:
            self.connection.delete(key)
            return True
        except ConnectionError:
            return False

    def verify_if_exists(self, key: str) -> bool:
        try:
            number_of_names_that_exists = self.connection.exists(key)
            doest_exists = number_of_names_that_exists == 0
            exists = not doest_exists
            return exists
        except ConnectionError:
            return False



