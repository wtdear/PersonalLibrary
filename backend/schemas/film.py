from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class FilmBase(BaseModel):
    title: str
    director: Optional[str] = None
    release_year: Optional[int] = None
    rating: Optional[float] = None
    genres: Optional[str] = None
    cover_url: Optional[str] = None
    description: Optional[str] = None
    external_link: Optional[str] = None

class FilmCreate(FilmBase):
    pass

class FilmInDB(FilmBase):
    id: int
    
    class Config:
        orm_mode = True

class FilmSearch(BaseModel):
    query: str

class FilmResponse(FilmInDB):
    added_date: Optional[datetime] = None

class ExternalFilm(BaseModel):
    title: str
    director: Optional[str] = None
    release_year: Optional[int] = None
    rating: Optional[float] = None
    genres: Optional[List[str]] = None
    cover_url: Optional[str] = None
    description: Optional[str] = None
    external_link: Optional[str] = None
    external_id: Optional[str] = None