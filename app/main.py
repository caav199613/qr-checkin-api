from fastapi import FastAPI
from app.create_db import crear_base_datos
from app.core.database import Base, engine
from app.api import estudiante_router, bus_router, register_router, conductor_router

# Crear Base de datos
crear_base_datos()


# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Usuarios")


app.include_router(estudiante_router.router)
app.include_router(bus_router.router)
app.include_router(register_router.router)
app.include_router(conductor_router.router)