from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class GameBase(BaseModel):
    title: str
    platform: Optional[str] = None
    release_year: Optional[int] = None
    genres: Optional[str] = None
    cover_url: Optional[str] = None
    description: Optional[str] = None
    external_link: Optional[str] = None

class GameCreate(GameBase):
    pass

class GameInDB(GameBase):
    id: int
    
    class Config:
        orm_mode = True

class GameSearch(BaseModel):
    query: str

class GameResponse(GameInDB):
    added_date: Optional[datetime] = None

class ExternalGame(BaseModel):
    title: str
    platform: Optional[List[str]] = None
    release_year: Optional[int] = None
    genres: Optional[List[str]] = None
    cover_url: Optional[str] = None
    description: Optional[str] = None
    external_link: Optional[str] = None
    external_id: Optional[str] = None