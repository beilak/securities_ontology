from pydantic_settings import BaseSettings


class Config(BaseSettings):
    DB_DSN: str = "postgresql://securities_user:securities_pwd@127.0.0.1:5432/securities_db"  # PostgresDsn
