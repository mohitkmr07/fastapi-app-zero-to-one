from pydantic import PostgresDsn, RedisDsn
from starlette.config import Config
from starlette.datastructures import Secret

config = Config()


class Settings:
    POSTGRES_USER = config("POSTGRES_USER", cast=str)
    POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=Secret)
    POSTGRES_SERVER = config("POSTGRES_SERVER", cast=str)
    POSTGRES_PORT = config("POSTGRES_PORT", cast=str, default="5432")
    POSTGRES_DB = config("POSTGRES_DB", cast=str)

    SQLALCHEMY_DATABASE_URI: str = PostgresDsn.build(
        scheme="postgresql",
        user=POSTGRES_USER,
        password=str(POSTGRES_PASSWORD),
        host=POSTGRES_SERVER,
        port=POSTGRES_PORT,
        path=f"/{POSTGRES_DB or ''}",
    )
    POOL_SIZE = config("POOL_SIZE", cast=int, default=5)
    MAX_OVERFLOW = config("MAX_OVERFLOW", cast=int, default=-1)
    POOL_PRE_PING = config("POOL_PRE_PING", cast=bool, default=True)
    ECHO = config("ECHO", cast=bool, default=False)
    POOL_RECYCLE_IN_SECONDS = config("POOL_RECYCLE_IN_SECONDS", cast=int, default=3600)
    ECHO_POOL = config("ECHO_POOL", cast=bool, default=False)
    POOL_RESET_ON_RETURN = config("POOL_RESET_ON_RETURN", cast=str, default="rollback")
    POOL_TIMEOUT_IN_SECONDS = config("POOL_TIMEOUT_IN_SECONDS", cast=int, default=30)
    POOL = config("POOL", cast=str, default="~sqlalchemy.pool.QueuePool")
    # REDIS_URL = config("REDIS_URL", cast=str)
    REDIS_MAX_CONNECTION = config("REDIS_MAX_CONNECTION", cast=int, default=1)

    REDIS_SCHEME = config("REDIS_SCHEME", cast=str, default="redis")
    REDIS_USER = config("REDIS_USER", cast=str, default=None)
    REDIS_PASSWORD = config("REDIS_PASSWORD", cast=Secret)
    REDIS_URL = config("REDIS_URL", cast=str)
    REDIS_PORT = config("REDIS_PORT", cast=str, default="6379")
    REDIS_DB = config("REDIS_DB", cast=str, default="0")

    REDIS_URI: str = RedisDsn.build(
        scheme=REDIS_SCHEME,
        user=REDIS_USER,
        password=str(REDIS_PASSWORD),
        host=REDIS_URL,
        port=REDIS_PORT,
        path=f"/{REDIS_DB or ''}",
    )


settings = Settings()
