from redis import Redis

class RedisRepositoryInterface:
    def insert(self, key: str, value: any) -> None:
        pass

    def get(self, key: str) -> str:
        pass

    def insert_hash(self, key: str, field: str, value: any) -> None:
        pass

    def get_hash(self, key: str, field: str) -> any:
        pass

    def insert_ex(self, key: str, value: any, time: int) -> None:
        pass

    def insert_hash_ex(self, key: str, field: str, value: any, time: int) -> None:
        pass