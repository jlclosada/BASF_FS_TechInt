from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from config import config

def test_connection():
    try:
        # Crea el motor de conexión a la base de datos
        engine = create_engine(config.DATABASE_URL)
        
        # Intenta conectar a la base de datos
        with engine.connect() as connection:
            print("Conexión a la base de datos establecida exitosamente.")
        
    except OperationalError as e:
        print("Error al conectar con la base de datos:", e)

if __name__ == "__main__":
    test_connection()
