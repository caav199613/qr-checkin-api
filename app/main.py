from fastapi import FastAPI
from app.create_db import crear_base_datos
from app.core.database import Base, engine
from app.api import user_router

# Crear Base de datos
crear_base_datos()


# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Usuarios")

app.include_router(user_router.router)
