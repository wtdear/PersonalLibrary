import json
from typing import Any, List, Dict

def format_genres(genres: Any) -> str:
    """Форматирование жанров в JSON строку"""
    if not genres:
        return ""
    
    if isinstance(genres, str):
        # Пробуем распарсить JSON
        try:
            genres_list = json.loads(genres)
            if isinstance(genres_list, list):
                return json.dumps(genres_list, ensure_ascii=False)
            return genres
        except json.JSONDecodeError:
            # Если не JSON, возвращаем как есть
            return genres
    
    if isinstance(genres, list):
        return json.dumps(genres, ensure_ascii=False)
    
    return str(genres)

def parse_genres(genres_str: str) -> List[str]:
    """Парсинг JSON строки с жанрами"""
    if not genres_str:
        return []
    
    try:
        genres = json.loads(genres_str)
        if isinstance(genres, list):
            return genres
        return [genres]
    except json.JSONDecodeError:
        # Если не JSON, разбиваем по запятым
        return [g.strip() for g in genres_str.split(',') if g.strip()]

def format_external_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """Стандартизация данных из внешних API"""
    formatted = {
        "title": data.get("title", ""),
        "cover_url": data.get("cover_url") or data.get("image") or data.get("poster"),
        "description": data.get("description") or data.get("overview") or data.get("summary", ""),
        "external_link": data.get("external_link") or data.get("url") or data.get("link"),
    }
    
    # Обрезаем слишком длинное описание
    if formatted["description"] and len(formatted["description"]) > 500:
        formatted["description"] = formatted["description"][:500] + "..."
    
    return formatted