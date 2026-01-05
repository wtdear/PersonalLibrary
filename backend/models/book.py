from sqlalchemy import Column, Integer, String, Text
from ..database import Base

class Book(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    author = Column(String, nullable=False)
    genres = Column(String)  # JSON строка
    cover_url = Column(String)
    description = Column(Text)
    external_link = Column(String)
    
    # Связь с пользователями
    user_books = relationship("UserBook", back_populates="book")