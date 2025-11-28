# app/config.py
from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    SECRET_KEY: str = "change_this_secret"

    class Config:
        env_file = str(Path(__file__).resolve().parent.parent / ".env")

settings = Settings()
