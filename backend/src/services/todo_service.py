from sqlalchemy.orm import Session
from src.models.controllers.todo_controller import create_item, remove_item, edit_item, update_item 
from src.models.dto.todo_dto import ToDoItemCreate, ToDoItemUpdate
from src.models.controllers.todo_controller import search_items
from src.models.models import TodoItem

def list_todo_items(db: Session):
    return get_items(db)

def add_todo_item(db: Session, item: ToDoItemCreate):
    return create_item(db, item)

def remove_todo_item(db: Session, item_id: int):
    return remove_item(db, item_id)

def edit_todo_item(db: Session, item_id: int, item: ToDoItemUpdate):
    return edit_item(db, item_id, item)

def search_todo_items(db: Session, search_term: str):
    return search_items(db, search_term)

def get_items(db: Session):
    """Obtiene todas las tareas"""
    return db.query(TodoItem).all()


def update_item_favorite(db: Session, item_id: int, favorite: bool):
    """Actualiza solo el campo 'favorite' de la tarea"""
    item = db.query(TodoItem).filter(TodoItem.id == item_id).first()
    if item:
        item.favorite = favorite  # update favorite filed
        db.commit()
        db.refresh(item)
        return item
    return None
