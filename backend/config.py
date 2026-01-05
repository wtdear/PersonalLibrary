import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # База данных
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./library.db")
    
    # JWT настройки
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
    
    # Внешние API ключи
    GOOGLE_BOOKS_API_KEY = os.getenv("GOOGLE_BOOKS_API_KEY", "")
    TMDB_API_KEY = os.getenv("TMDB_API_KEY", "")
    RAWG_API_KEY = os.getenv("RAWG_API_KEY", "")
    
    # Настройки внешних API
    GOOGLE_BOOKS_URL = "https://www.googleapis.com/books/v1/volumes"
    TMDB_URL = "https://api.themoviedb.org/3"
    RAWG_URL = "https://api.rawg.io/api/games"
    
    # Настройки безопасности
    BCRYPT_ROUNDS = 12

settings = Settings()