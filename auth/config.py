from dotenv import load_dotenv
import os

load_dotenv()  # Loads .env into environment

class Settings:
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")

    JWT_SECRET = os.getenv("JWT_SECRET")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
    JWT_EXP_MINUTES = int(os.getenv("JWT_EXP_MINUTES", 30))

settings = Settings()
