
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)





class Settings:
    PROJECT_TITLE: str = "jobsite"
    PROJECT_VERSION: str = "0.1.0"

    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER:str = os.getenv("POSTGRES_SERVER","http://172.16.0.111")
    POSTGRES_PORT:str = os.getenv("POSTGRES_PORT",5432)
    POSTGRES_DB:str = os.getenv("POSTGRES_DB","user_db")
    DATABASE_URL:f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


settings = Settings()

