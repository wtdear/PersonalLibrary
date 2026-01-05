from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ...database import get_db
from ... import schemas, crud, models
from ...api.dependencies import get_current_user
from ...api.external import search_google_books

router = APIRouter()

@router.post("/books/search")
async def search_books(
    search: schemas.BookSearch,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    # Ищем в локальной БД
    local_results = crud.search_books_in_db(db, search.query)
    
    # Ищем во внешних API
    external_results = await search_google_books(search.query)
    
    # Объединяем результаты
    all_books = []
    
    # Добавляем локальные результаты
    for book in local_results:
        all_books.append(schemas.BookResponse.from_orm(book))
    
    # Добавляем внешние результаты
    for book in external_results:
        # Проверяем, есть ли уже книга в библиотеке пользователя
        is_in_library = False
        if book.title:
            existing_book = crud.get_book_by_title(db, book.title)
            if existing_book:
                # Проверяем, есть ли связь с пользователем
                user_has_book = db.query(models.UserBook).filter(
                    models.UserBook.user_id == current_user.id,
                    models.UserBook.book_id == existing_book.id
                ).first()
                is_in_library = user_has_book is not None
        
        book_dict = book.dict()
        book_dict["is_in_library"] = is_in_library
        all_books.append(book_dict)
    
    return {"results": all_books}

@router.post("/user/books/add")
def add_book_to_user(
    book: schemas.BookCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    # Проверяем, существует ли книга
    existing_book = crud.get_book_by_title(db, book.title)
    if not existing_book:
        # Создаем новую книгу
        existing_book = crud.create_book(db, book)
    
    # Добавляем книгу пользователю
    user_book = crud.add_book_to_user(db, current_user.id, existing_book.id)
    
    if user_book:
        return {"message": "Книга добавлена в библиотеку", "book_id": existing_book.id}
    else:
        return {"message": "Книга уже в библиотеке", "book_id": existing_book.id}

@router.get("/user/books", response_model=List[schemas.BookResponse])
def get_user_books(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    books = crud.get_user_books(db, current_user.id)
    return books