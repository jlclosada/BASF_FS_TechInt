from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.commons.db.sql_driver import get_db
from src.models.dto.todo_dto import ToDoItemCreate, ToDoItemUpdate, ToDoItemResponse
from src.services.todo_service import list_todo_items, add_todo_item, remove_todo_item, edit_todo_item, search_todo_items, update_item_favorite
from pydantic import BaseModel

router = APIRouter()

@router.get("/items", response_model=list[ToDoItemResponse])
def read_items(db: Session = Depends(get_db)):
    return list_todo_items(db)

@router.post("/items", response_model=ToDoItemResponse)
def create_item(item: ToDoItemCreate, db: Session = Depends(get_db)):
    return add_todo_item(db, item)

@router.delete("/items/{item_id}", response_model=ToDoItemResponse)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = remove_todo_item(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.put("/items/{item_id}", response_model=ToDoItemResponse)
def update_item(item_id: int, item: ToDoItemUpdate, db: Session = Depends(get_db)):
    return edit_todo_item(db, item_id, item)

# @router.get("/todos/search")
# def search_todos(search_term: str, db: Session = Depends(get_db)):
#     # Llama al servicio de búsqueda
#     results = search_todo_items(db, search_term)
#     return results

# get all tasks endpoint
@router.get("/items")
def read_items(db: Session = Depends(get_db)):
    try:
        return list_todo_items(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error al obtener las tareas")

# Define a model for payload body
class FavoriteRequest(BaseModel):
    favorite: bool

@router.put("/items/{item_id}/favorite")
async def update_favorite(item_id: int, favorite_request: FavoriteRequest, db: Session = Depends(get_db)):
    """Actualiza solo el estado de 'favorite' de la tarea"""
    item = update_item_favorite(db, item_id, favorite_request.favorite)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item