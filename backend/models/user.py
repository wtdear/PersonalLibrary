from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    name = Column(String, nullable=False)
    
    # Связи с библиотекой
    books = relationship("UserBook", back_populates="user")
    films = relationship("UserFilm", back_populates="user")
    games = relationship("UserGame", back_populates="user")