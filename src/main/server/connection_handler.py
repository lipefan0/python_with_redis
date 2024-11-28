from src.models.redis.settings.connection import RedisConnectionHandler
from src.models.sqlite.settings.connection import SqliteConnectionHandler

redis_connection_handle = RedisConnectionHandler()
sqlite_connection_handle = SqliteConnectionHandler()

redis_connection_handle.connect()
sqlite_connection_handle.connect()
