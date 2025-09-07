from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.conductor_schema import ConductorCreate, ConductorUpdate, ConductorResponse
from app.crud import conductor_crud
from app.dependencies.db import get_db

router = APIRouter(
    prefix="/conductores",
    tags=["Conductores"]
)


@router.get("/", response_model=List[ConductorResponse])
def listar_conductores(db: Session = Depends(get_db)):
    return conductor_crud.get_all(db)




@router.get("/{numero_id}", response_model=ConductorResponse)
def obtener_conductor(numero_id: int, db: Session = Depends(get_db)):
    conductor = conductor_crud.get_by_numero(db, numero_id)
    if not conductor:
        raise HTTPException(status_code=404, detail="Conductor no encontrado")
    return conductor


@router.post("/", response_model=ConductorResponse, status_code=201)
def crear_conductor(conductor_in: ConductorCreate, db: Session = Depends(get_db)):
    return conductor_crud.create(db, conductor_in)


@router.put("/{numero_id}", response_model=ConductorResponse)
def actualizar_conductor(numero_id: int, conductor_in: ConductorUpdate, db: Session = Depends(get_db)):
    return conductor_crud.update(db, numero_id, conductor_in)


@router.delete("/{numero_id}")
def eliminar_conductor(numero_id: int, db: Session = Depends(get_db)):
    return conductor_crud.delete(db, numero_id)
