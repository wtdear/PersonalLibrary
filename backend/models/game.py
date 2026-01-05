from sqlalchemy import Column, Integer, String, Text
from ..database import Base
from sqlalchemy.orm import relationship

class Game(Base):
    __tablename__ = "games"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    platform = Column(String)
    release_year = Column(Integer)
    genres = Column(String)  # JSON строка
    cover_url = Column(String)
    description = Column(Text)
    external_link = Column(String)
    
    # Связь с пользователями
    user_games = relationship("UserGame", back_populates="game")