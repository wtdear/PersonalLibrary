from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ...database import get_db
from ... import schemas, crud, models
from ...api.dependencies import get_current_user
from ...api.external import search_rawg

router = APIRouter()

@router.post("/games/search")
async def search_games(
    search: schemas.GameSearch,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    # Ищем в локальной БД
    local_results = crud.search_games_in_db(db, search.query)
    
    # Ищем во внешних API
    external_results = await search_rawg(search.query)
    
    # Объединяем результаты
    all_games = []
    
    # Добавляем локальные результаты
    for game in local_results:
        all_games.append(schemas.GameResponse.from_orm(game))
    
    # Добавляем внешние результаты
    for game in external_results:
        # Проверяем, есть ли уже игра в библиотеке пользователя
        is_in_library = False
        if game.title:
            existing_game = crud.get_game_by_title(db, game.title)
            if existing_game:
                # Проверяем, есть ли связь с пользователем
                user_has_game = db.query(models.UserGame).filter(
                    models.UserGame.user_id == current_user.id,
                    models.UserGame.game_id == existing_game.id
                ).first()
                is_in_library = user_has_game is not None
        
        game_dict = game.dict()
        game_dict["is_in_library"] = is_in_library
        all_games.append(game_dict)
    
    return {"results": all_games}

@router.post("/user/games/add")
def add_game_to_user(
    game: schemas.GameCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    # Проверяем, существует ли игра
    existing_game = crud.get_game_by_title(db, game.title)
    if not existing_game:
        # Создаем новую игру
        existing_game = crud.create_game(db, game)
    
    # Добавляем игру пользователю
    user_game = crud.add_game_to_user(db, current_user.id, existing_game.id)
    
    if user_game:
        return {"message": "Игра добавлена в библиотеку", "game_id": existing_game.id}
    else:
        return {"message": "Игра уже в библиотеке", "game_id": existing_game.id}

@router.get("/user/games", response_model=List[schemas.GameResponse])
def get_user_games(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    games = crud.get_user_games(db, current_user.id)
    return games