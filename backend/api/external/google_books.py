import json
import httpx
from typing import List, Optional
from ...schemas.book import ExternalBook

from ...config import settings

async def search_google_books(query: str) -> List[ExternalBook]:
    if not settings.GOOGLE_BOOKS_API_KEY:
        return []
    
    params = {
        "q": query,
        "key": settings.GOOGLE_BOOKS_API_KEY,
        "maxResults": 20
    }
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(settings.GOOGLE_BOOKS_URL, params=params)
            response.raise_for_status()
            data = response.json()
        except Exception:
            return []
    
    books = []
    for item in data.get("items", []):
        volume_info = item.get("volumeInfo", {})
        
        # Извлекаем авторов
        authors = volume_info.get("authors", [])
        author = ", ".join(authors) if authors else "Unknown"
        
        # Извлекаем жанры
        categories = volume_info.get("categories", [])
        genres = ", ".join(categories) if categories else None
        
        # Извлекаем описание
        description = volume_info.get("description", "")
        if description and len(description) > 500:
            description = description[:500] + "..."
        
        # Извлекаем обложку
        image_links = volume_info.get("imageLinks", {})
        cover_url = image_links.get("thumbnail") if image_links else None
        
        book = ExternalBook(
            title=volume_info.get("title", ""),
            author=author,
            genres=genres,
            cover_url=cover_url,
            description=description,
            external_link=volume_info.get("infoLink"),
            external_id=item.get("id")
        )
        books.append(book)
    
    return books