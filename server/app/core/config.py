from pydantic_settings import BaseModel
from pydantic_settings import BaseSettings

class RunConfig(BaseModel):
    run: str = "0.0.0.0"
    port: int = 8000



class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    db_url: str

settings = Settings()