from sqlalchemy.orm import Session
from src.models.dto.todo_dto import ToDoItemCreate, ToDoItemUpdate
from src.models import models

# get all ToDo items
def get_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.TodoItem).offset(skip).limit(limit).all()


def create_item(db: Session, item: ToDoItemCreate):
    db_item = models.TodoItem(title=item.title, description=item.description, completed=item.completed)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


# delete item ToDo
def delete_todo_item(db: Session, item_id: int):
    item = db.query(models.TodoItem).filter(models.TodoItem.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
    return item

# update item ToDo state
def update_item(db: Session, item_id: int, completed: bool):
    item = db.query(models.TodoItem).filter(models.TodoItem.id == item_id).first()
    if item:
        item.completed = completed
        db.commit()
        db.refresh(item)
    return item


def remove_item(db: Session, item_id: int):
    item = db.query(models.TodoItem).filter(models.TodoItem.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
    return item


def edit_item(db: Session, item_id: int, item_update: ToDoItemUpdate):
    item = db.query(models.TodoItem).filter(models.TodoItem.id == item_id).first()
    if item:
        item.title = item_update.title
        item.description = item_update.description
        item.completed = item_update.completed
        db.commit()
        db.refresh(item)
    return item

# search function
def search_items(db: Session, search_term: str, skip: int = 0, limit: int = 10):
    return db.query(models.TodoItem).filter(
        or_(
            models.TodoItem.title.ilike(f"%{search_term}%"),  
            models.TodoItem.description.ilike(f"%{search_term}%") 
        )
    ).offset(skip).limit(limit).all()
