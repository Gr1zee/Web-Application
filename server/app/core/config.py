from pydantic_settings import BaseModel
from pydantic_settings import BaseSettings
from pydantic import PostgresDsn

class RunConfig(BaseModel):
    run: str = "0.0.0.0"
    port: int = 8000

class ApiPrefix(BaseModel):
    prefix: str="/api"

class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool
    echo_pool: bool
    pool_size: int  = 50
    max_overflow: int

class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    db_url: str
    api_prefix: ApiPrefix
    db: DatabaseConfig

settings = Settings()