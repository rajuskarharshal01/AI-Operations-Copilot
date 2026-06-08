from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "AI Operations copilot"
    version: str = "1.0.0"

settings = Settings()