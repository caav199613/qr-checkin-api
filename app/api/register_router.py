from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.registro_schema import RegistroCreate, RegistroUpdate, RegistroResponse  # 👈 corregido
from app.crud import registro_crud
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
def obtener_registro(registro_id: int, db: Session = Depends(get_db)):
    """Obtener un registro de ruta por ID"""
    registro = registro_crud.get_by_id(db, registro_id)
    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return registro


@router.post("/", response_model=RegistroResponse, status_code=201)
def crear_registro(registro_in: RegistroCreate, db: Session = Depends(get_db)):
    """Crear un nuevo registro de ruta"""
    return registro_crud.create(db, registro_in)


@router.put("/{registro_id}", response_model=RegistroResponse)
def actualizar_registro(
    registro_id: int,
    registro_in: RegistroUpdate,
    db: Session = Depends(get_db),
):
    """Actualizar un registro de ruta por ID"""
    return registro_crud.update(db, registro_id, registro_in)


@router.delete("/{registro_id}")
def eliminar_registro(registro_id: int, db: Session = Depends(get_db)):
    """Eliminar un registro de ruta por ID"""
    return registro_crud
