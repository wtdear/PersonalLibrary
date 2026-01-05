import json
import httpx
from typing import List, Optional
from ..schemas.game import ExternalGame
from ...config import settings

async def search_rawg(query: str) -> List[ExternalGame]:
    if not settings.RAWG_API_KEY:
        return []
    
    params = {
        "key": settings.RAWG_API_KEY,
        "search": query,
        "page_size": 20,
        "search_precise": True
    }
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(settings.RAWG_URL, params=params)
            response.raise_for_status()
            data = response.json()
        except Exception:
            return []
    
    games = []
    for game_data in data.get("results", []):
        # Извлекаем платформы
        platforms = [platform.get("platform", {}).get("name", "") 
                    for platform in game_data.get("platforms", [])]
        platform_str = ", ".join(platforms) if platforms else None
        
        # Извлекаем жанры
        genres = [genre.get("name", "") for genre in game_data.get("genres", [])]
        genres_str = ", ".join(genres) if genres else None
        
        # Извлекаем описание
        description = game_data.get("description", "")
        if description and len(description) > 500:
            description = description[:500] + "..."
        
        # Извлекаем обложку
        cover_url = game_data.get("background_image")
        
        # Извлекаем год выпуска
        release_year = None
        released = game_data.get("released")
        if released and len(released) >= 4:
            try:
                release_year = int(released[:4])
            except ValueError:
                pass
        
        game = ExternalGame(
            title=game_data.get("name", ""),
            platform=platform_str,
            release_year=release_year,
            genres=genres_str,
            cover_url=cover_url,
            description=description,
            external_link=game_data.get("website") or f"https://rawg.io/games/{game_data.get('slug', '')}",
            external_id=str(game_data.get("id"))
        )
        games.append(game)
    
    return games