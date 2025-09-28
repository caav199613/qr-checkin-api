from dotenv import load_dotenv
import os

# 👇 Función única de normalización
def to_capitalize(value: str) -> str:
    """
    Convierte un string a Capitalize (primera letra mayúscula, resto en minúscula).
    Si no es string, lo devuelve igual.
    """
    return value.capitalize() if isinstance(value, str) else value


def to_upper(value: str) -> str:
    """
    Convierte un string a mayúsculas de forma segura.
    Si no es string, lo devuelve igual.
    """
    return value.upper() if isinstance(value, str) else value


# Cargar variables de entorno
load_dotenv()

DB_NAME = os.getenv("DB_NAME", "qrcheckindb")
DB_USER = os.getenv("DB_USER", "admin")
DB_PASSWORD = os.getenv("DB_PASSWORD", "admin")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
URL_WITHOUT_DB = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}"
