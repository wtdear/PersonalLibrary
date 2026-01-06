from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .api.endpoints import auth, books, films, games
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

# Создаем таблицы

app = FastAPI(
    title="Personal Library API",
    description="Backend для личной библиотеки книг, фильмов и игр",
    version="1.0.0"
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app.mount(
    "/static",
    StaticFiles(directory=os.path.join(BASE_DIR, "static")),
    name="static"
)


# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React фронтенд
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем роутеры
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(books.router, prefix="/api", tags=["books"])
app.include_router(films.router, prefix="/api", tags=["films"])
app.include_router(games.router, prefix="/api", tags=["games"])

@app.get("/")
async def root():
    return {"message": "Personal Library API", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}