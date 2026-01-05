from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ...database import get_db
from ... import schemas, crud, models
from ...api.dependencies import get_current_user
from ...api.external import search_tmdb

router = APIRouter()

@router.post("/films/search")
async def search_films(
    search: schemas.FilmSearch,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    # Ищем в локальной БД
    local_results = crud.search_films_in_db(db, search.query)
    
    # Ищем во внешних API
    external_results = await search_tmdb(search.query)
    
    # Объединяем результаты
    all_films = []
    
    # Добавляем локальные результаты
    for film in local_results:
        all_films.append(schemas.FilmResponse.from_orm(film))
    
    # Добавляем внешние результаты
    for film in external_results:
        # Проверяем, есть ли уже фильм в библиотеке пользователя
        is_in_library = False
        if film.title:
            existing_film = crud.get_film_by_title(db, film.title)
            if existing_film:
                # Проверяем, есть ли связь с пользователем
                user_has_film = db.query(models.UserFilm).filter(
                    models.UserFilm.user_id == current_user.id,
                    models.UserFilm.film_id == existing_film.id
                ).first()
                is_in_library = user_has_film is not None
        
        film_dict = film.dict()
        film_dict["is_in_library"] = is_in_library
        all_films.append(film_dict)
    
    return {"results": all_films}

@router.post("/user/films/add")
def add_film_to_user(
    film: schemas.FilmCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    # Проверяем, существует ли фильм
    existing_film = crud.get_film_by_title(db, film.title)
    if not existing_film:
        # Создаем новый фильм
        existing_film = crud.create_film(db, film)
    
    # Добавляем фильм пользователю
    user_film = crud.add_film_to_user(db, current_user.id, existing_film.id)
    
    if user_film:
        return {"message": "Фильм добавлен в библиотеку", "film_id": existing_film.id}
    else:
        return {"message": "Фильм уже в библиотеке", "film_id": existing_film.id}

@router.get("/user/films", response_model=List[schemas.FilmResponse])
def get_user_films(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    films = crud.get_user_films(db, current_user.id)
    return films