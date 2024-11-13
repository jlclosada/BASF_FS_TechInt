# src/constants/app_constants.py
# works with docker
import os
from sqlalchemy import create_engine

# Obtener las variables de entorno
user = os.getenv("DB_USER", "myuser")
pwd = os.getenv("DB_PASSWORD", "mypassword")
db_name = os.getenv("DB_NAME", "todoapp")
host = os.getenv("DB_HOST", "localhost")
port = os.getenv("DB_PORT", "5434")

# Crear la conexión a la base de datos PostgreSQL
DATABASE_URL = f"postgresql://{user}:{pwd}@{host}:{port}/{db_name}"

engine = create_engine(DATABASE_URL)

# no docker
# user = "<your_postgres_username>" 
# pwd = "<your_postgres_password>"  