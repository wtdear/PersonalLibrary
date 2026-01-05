import json
import httpx
from typing import List, Optional
from ..schemas.film import ExternalFilm
from ...config import settings

async def search_tmdb(query: str) -> List[ExternalFilm]:
    if not settings.TMDB_API_KEY:
        return []
    
    search_url = f"{settings.TMDB_URL}/search/movie"
    params = {
        "api_key": settings.TMDB_API_KEY,
        "query": query,
        "language": "ru-RU",
        "page": 1
    }
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(search_url, params=params)
            response.raise_for_status()
            data = response.json()
        except Exception:
            return []
    
    films = []
    for movie in data.get("results", []):
        # Получаем детальную информацию о фильме
        movie_id = movie.get("id")
        if not movie_id:
            continue
        
        detail_url = f"{settings.TMDB_URL}/movie/{movie_id}"
        detail_params = {
            "api_key": settings.TMDB_API_KEY,
            "language": "ru-RU",
            "append_to_response": "credits"
        }
        
        try:
            detail_response = await client.get(detail_url, params=detail_params)
            detail_response.raise_for_status()
            detail_data = detail_response.json()
        except Exception:
            continue
        
        # Извлекаем режиссера
        director = "Unknown"
        for person in detail_data.get("credits", {}).get("crew", []):
            if person.get("job") == "Director":
                director = person.get("name", "Unknown")
                break
        
        # Извлекаем жанры
        genres = [genre.get("name", "") for genre in detail_data.get("genres", [])]
        genres_str = ", ".join(genres) if genres else None
        
        # Извлекаем описание
        description = detail_data.get("overview", "")
        if not description:
            description = movie.get("overview", "")
        
        # Извлекаем обложку
        cover_url = None
        poster_path = movie.get("poster_path") or detail_data.get("poster_path")
        if poster_path:
            cover_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
        
        film = ExternalFilm(
            title=movie.get("title", ""),
            director=director,
            release_year=int(movie.get("release_date", "0")[:4]) if movie.get("release_date") else None,
            rating=movie.get("vote_average"),
            genres=genres_str,
            cover_url=cover_url,
            description=description,
            external_link=f"https://www.themoviedb.org/movie/{movie_id}",
            external_id=str(movie_id)
        )
        films.append(film)
    
    return films