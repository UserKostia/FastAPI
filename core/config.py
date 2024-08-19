from pathlib import Path

from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent


class Setting(BaseSettings):
    # Setting up a prefix for api v1
    api_v1_prefix: str = "/api/v1"

    # Setting up a SQLite database
    db_url: str = f"sqlite+aiosqlite:///{BASE_DIR}/db.sqlite3"
    # Output queries to the database to the console
    db_echo: bool = False
    # db_echo: bool = True


settings = Setting()
