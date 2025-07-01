from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Authentication Service"
    DEBUG_MODE: bool = False
    
    DATABASE_URL: str
    
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"

settings = Settings()