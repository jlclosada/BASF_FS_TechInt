from pydantic import BaseModel

class TodoItemBase(BaseModel):
    title: str
    description: str
    completed: bool = False

class ToDoItemCreate(TodoItemBase):
    pass

class ToDoItemUpdate(TodoItemBase):
    completed: bool 

class ToDoItemResponse(TodoItemBase):
    id: int

    class Config:
        orm_mode = True
