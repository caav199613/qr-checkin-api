from sqlalchemy import create_engine, text
from app.core.config import URL_WITHOUT_DB, DATABASE_URL, DB_NAME
from app.models.user import Base

def crear_base_datos():
    # Conexión sin base de datos
    engine = create_engine(URL_WITHOUT_DB)
    with engine.connect() as conn:
        conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {DB_NAME} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"))
        print(f"Base de datos '{DB_NAME}' verificada o creada.")
    
    # Crear tablas
    engine_with_db = create_engine(DATABASE_URL)
    Base.metadata.create_all(bind=engine_with_db)
    print("Tablas creadas (si no existían).")

if __name__ == "__main__":
    crear_base_datos()
