from sqlalchemy.orm import Session
from .. import models, schemas
from typing import List, Optional

def get_film(db: Session, film_id: int):
    return db.query(models.Film).filter(models.Film.id == film_id).first()

def get_film_by_title(db: Session, title: str):
    return db.query(models.Film).filter(models.Film.title == title).first()

def create_film(db: Session, film: schemas.FilmCreate):
    db_film = models.Film(**film.dict())
    db.add(db_film)
    db.commit()
    db.refresh(db_film)
    return db_film

def add_film_to_user(db: Session, user_id: int, film_id: int):
    existing = db.query(models.UserFilm).filter(
        models.UserFilm.user_id == user_id,
        models.UserFilm.film_id == film_id
    ).first()
    
    if existing:
        return existing
    
    user_film = models.UserFilm(user_id=user_id, film_id=film_id)
    db.add(user_film)
    db.commit()
    db.refresh(user_film)
    return user_film

def get_user_films(db: Session, user_id: int):
    return db.query(models.Film).join(models.UserFilm).filter(
        models.UserFilm.user_id == user_id
    ).all()

def search_films_in_db(db: Session, query: str):
    return db.query(models.Film).filter(
        models.Film.title.ilike(f"%{query}%") |
        models.Film.director.ilike(f"%{query}%")
    ).limit(20).all()