from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class BookBase(BaseModel):
    title: str
    author: str
    genres: Optional[str] = None
    cover_url: Optional[str] = None
    description: Optional[str] = None
    external_link: Optional[str] = None

class BookCreate(BookBase):
    pass

class BookInDB(BookBase):
    id: int
    
    class Config:
        orm_mode = True

class BookSearch(BaseModel):
    query: str

class BookResponse(BookInDB):
    added_date: Optional[datetime] = None

class ExternalBook(BaseModel):
    title: str
    author: Optional[str] = None
    genres: Optional[List[str]] = None
    cover_url: Optional[str] = None
    description: Optional[str] = None
    external_link: Optional[str] = None
    external_id: Optional[str] = None