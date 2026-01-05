from sqlalchemy import Column, Integer, String, Text, Float
from ..database import Base
from sqlalchemy.orm import relationship

class Film(Base):
    __tablename__ = "films"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    director = Column(String)
    release_year = Column(Integer)
    rating = Column(Float)
    genres = Column(String)  # JSON строка
    cover_url = Column(String)
    description = Column(Text)
    external_link = Column(String)
    
    # Связь с пользователями
    user_films = relationship("UserFilm", back_populates="film")