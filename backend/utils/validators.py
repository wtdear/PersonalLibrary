import re
from typing import Optional

def validate_email(email: str) -> bool:
    """Проверка валидности email"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_password(password: str) -> tuple[bool, Optional[str]]:
    """Проверка сложности пароля"""
    if len(password) < 8:
        return False, "Пароль должен содержать минимум 8 символов"
    
    if not re.search(r'[A-Z]', password):
        return False, "Пароль должен содержать хотя бы одну заглавную букву"
    
    if not re.search(r'[a-z]', password):
        return False, "Пароль должен содержать хотя бы одну строчную букву"
    
    if not re.search(r'\d', password):
        return False, "Пароль должен содержать хотя бы одну цифру"
    
    return True, None

def sanitize_string(text: str) -> str:
    """Очистка строки от потенциально опасных символов"""
    # Удаляем HTML теги
    text = re.sub(r'<[^>]*>', '', text)
    # Удаляем управляющие символы
    text = re.sub(r'[\x00-\x1F\x7F]', '', text)
    return text.strip()