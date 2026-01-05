from sqlalchemy.orm import Session
from .. import models, schemas
from typing import List, Optional

def get_game(db: Session, game_id: int):
    return db.query(models.Game).filter(models.Game.id == game_id).first()

def get_game_by_title(db: Session, title: str):
    return db.query(models.Game).filter(models.Game.title == title).first()

def create_game(db: Session, game: schemas.GameCreate):
    db_game = models.Game(**game.dict())
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game

def add_game_to_user(db: Session, user_id: int, game_id: int):
    existing = db.query(models.UserGame).filter(
        models.UserGame.user_id == user_id,
        models.UserGame.game_id == game_id
    ).first()
    
    if existing:
        return existing
    
    user_game = models.UserGame(user_id=user_id, game_id=game_id)
    db.add(user_game)
    db.commit()
    db.refresh(user_game)
    return user_game

def get_user_games(db: Session, user_id: int):
    return db.query(models.Game).join(models.UserGame).filter(
        models.UserGame.user_id == user_id
    ).all()

def search_games_in_db(db: Session, query: str):
    return db.query(models.Game).filter(
        models.Game.title.ilike(f"%{query}%") |
        models.Game.platform.ilike(f"%{query}%")
    ).limit(20).all()