from redis import Redis
from .interface.redis_repository import RedisRepositoryInterface

class RedisRepository(RedisRepositoryInterface):
    def __init__(self, redis_conn: Redis) -> None:
        self.__redis_conn = redis_conn

    def insert(self, key: str, value: any) -> None:
        self.__redis_conn.set(key, value)

    def get(self, key: str) -> str:
        value = self.__redis_conn.get(key)
        if value:
            return value.decode('utf-8')
        return None

    def insert_hash(self, key: str, field: str, value: any) -> None:
        self.__redis_conn.hset(key, field, value)

    def get_hash(self, key: str, field: str) -> any:
        value = self.__redis_conn.hget(key, field)
        if value:
            return value.decode('utf-8')
        return None

    def insert_ex(self, key: str, value: any, time: int) -> None:
        self.__redis_conn.set(key, value, ex=time)

    def insert_hash_ex(self, key: str, field: str, value: any, time: int) -> None:
        self.__redis_conn.hset(key, field, value)
        self.__redis_conn.expire(key, time)