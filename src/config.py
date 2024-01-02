from pydantic_settings import BaseSettings


class Config(BaseSettings):
    DB_DSN: str  # PostgresDsn
