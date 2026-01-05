from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..database import Base
from sqlalchemy.orm import relationship

class UserBook(Base):
    __tablename__ = "user_books"
    
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id"), primary_key=True)
    added_date = Column(DateTime(timezone=True), server_default=func.now())
    
    user = relationship("User", back_populates="books")
    book = relationship("Book", back_populates="user_books")

class UserFilm(Base):
    __tablename__ = "user_films"
    
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    film_id = Column(Integer, ForeignKey("films.id"), primary_key=True)
    added_date = Column(DateTime(timezone=True), server_default=func.now())
    
    user = relationship("User", back_populates="films")
    film = relationship("Film", back_populates="user_films")

class UserGame(Base):
    __tablename__ = "user_games"
    
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    game_id = Column(Integer, ForeignKey("games.id"), primary_key=True)
    added_date = Column(DateTime(timezone=True), server_default=func.now())
    
    user = relationship("User", back_populates="games")
    game = relationship("Game", back_populates="user_games")