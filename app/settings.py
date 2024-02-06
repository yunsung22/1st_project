from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    dbname: str = 'clouds2024'
    dbconn: str = f'sqlite:///app/{dbname}'

config = Settings()