# app/routers/registro_ruta_router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.registro_schema import RegistroCreate, RegistroUpdate, RegistroResponse
from app.crud import registro_crud, estudiante_crud, conductor_crud, bus_crud
from app.dependencies.db import get_db

router = APIRouter(
    prefix="/registros",
    tags=["Registros de Ruta"]
)

@router.get("/", response_model=List[RegistroResponse])
def listar_registros(db: Session = Depends(get_db)):
    """Obtener todos los registros de ruta"""
    return registro_crud.get_all(db)

@router.get("/{registro_id}", response_model=RegistroResponse)
def obtener_registro(registro_id: str, db: Session = Depends(get_db)):
    """Obtener un registro de ruta por su UUID"""
    registro = registro_crud.get_by_id(db, registro_id)
    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return registro

# --------- NUEVOS GETS ---------

@router.get("/por-estudiante/{numero_identificacion}", response_model=List[RegistroResponse])
def listar_por_estudiante(numero_identificacion: str, db: Session = Depends(get_db)):
    """
    Listar registros por estudiante.
    Primero busca el Estudiante por su numero_identificacion en estudiante_crud,
    luego usa su id para traer los registros.
    """
    est = estudiante_crud.get_by_numero(db, numero_identificacion)
    if not est:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return registro_crud.get_by_estudiante(db, est.id)

@router.get("/por-conductor/{numero_id}", response_model=List[RegistroResponse])
def listar_por_conductor(numero_id: str, db: Session = Depends(get_db)):
    """
    Listar registros por conductor.
    Busca el Conductor por numero_id en conductor_crud y usa su id para traer los registros.
    """
    cond = conductor_crud.get_by_numero(db, numero_id)
    if not cond:
        raise HTTPException(status_code=404, detail="Conductor no encontrado")
    return registro_crud.get_by_conductor(db, cond.id)

@router.get("/por-bus/{placa}", response_model=List[RegistroResponse])
def listar_por_bus(placa: str, db: Session = Depends(get_db)):
    """
    Listar registros por bus.
    Busca el Bus por placa en bus_crud y usa su id para traer los registros.
    """
    bus = bus_crud.get_by_placa(db, placa)
    if not bus:
        raise HTTPException(status_code=404, detail="Bus no encontrado")
    return registro_crud.get_by_bus(db, bus.id)

@router.post("/", response_model=RegistroResponse, status_code=201)
def crear_registro(registro_in: RegistroCreate, db: Session = Depends(get_db)):
    """Crear un nuevo registro de ruta"""
    return registro_crud.create(db, registro_in)

@router.put("/{registro_id}", response_model=RegistroResponse)
def actualizar_registro(registro_id: str, registro_in: RegistroUpdate, db: Session = Depends(get_db)):
    """Actualizar un registro de ruta por UUID"""
    return registro_crud.update(db, registro_id, registro_in)

@router.delete("/{registro_id}")
def eliminar_registro(registro_id: str, db: Session = Depends(get_db)):
    """Eliminar un registro de ruta por UUID"""
    return registro_crud.delete(db, registro_id)
