from sqlalchemy.orm import Session
from .. import models, schemas
from typing import List, Optional

def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def get_book_by_title(db: Session, title: str):
    return db.query(models.Book).filter(models.Book.title == title).first()

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def add_book_to_user(db: Session, user_id: int, book_id: int):
    # Проверяем, есть ли уже такая связь
    existing = db.query(models.UserBook).filter(
        models.UserBook.user_id == user_id,
        models.UserBook.book_id == book_id
    ).first()
    
    if existing:
        return existing
    
    user_book = models.UserBook(user_id=user_id, book_id=book_id)
    db.add(user_book)
    db.commit()
    db.refresh(user_book)
    return user_book

def get_user_books(db: Session, user_id: int):
    return db.query(models.Book).join(models.UserBook).filter(
        models.UserBook.user_id == user_id
    ).all()

def search_books_in_db(db: Session, query: str):
    return db.query(models.Book).filter(
        models.Book.title.ilike(f"%{query}%") |
        models.Book.author.ilike(f"%{query}%")
    ).limit(20).all()