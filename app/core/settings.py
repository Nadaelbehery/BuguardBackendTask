from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url:str

    def get_db_url(self):
        return self.database_url
    
    class Config:
        env_file = ".env"

def get_settings():
    return Settings()