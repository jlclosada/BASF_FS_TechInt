import os
from src.constants.app_constants import user, pwd

class Config:
    DATABASE_URL = f"postgresql://{user}:{pwd}@localhost/todoapp"

config = Config()
