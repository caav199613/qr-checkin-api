from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.schemas.estudiante_schema import estudianteCreate, estudianteResponse, estudianteUpdate
from app.crud import estudiante_crud
from app.dependencies.db import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/estudiante", tags=["estudiante"])

@router.get("/", response_model=List[estudianteResponse])
def listar_estudiante(db: Session = Depends(get_db)):
    return estudiante_crud.get_all(db)

@router.get("/{numero_identificacion}", response_model=estudianteResponse)
def obtener_estudiante(numero_identificacion: str, db: Session = Depends(get_db)):
    estudiante = estudiante_crud.get_by_numero(db, numero_identificacion)
    if not estudiante:
        raise HTTPException(status_code=404, detail="estudiante no encontrado")
    return estudiante

@router.post("/", response_model=estudianteResponse)
def crear_estudiante(estudiante: estudianteCreate, db: Session = Depends(get_db)):
    return estudiante_crud.create(db, estudiante)

@router.put("/{numero_identificacion}", response_model=estudianteResponse)
def actualizar_estudiante(numero_identificacion: str, estudiante: estudianteUpdate, db: Session = Depends(get_db)):
    estudiante = estudiante_crud.update_by_numero(db, numero_identificacion, estudiante)
    if not estudiante:
        raise HTTPException(status_code=404, detail="estudiante no encontrado")
    return estudiante

@router.delete("/{numero_identificacion}")
def eliminar_estudiante(numero_identificacion: str, db: Session = Depends(get_db)):
    estudiante = estudiante_crud.delete_by_numero(db, numero_identificacion)
    if not estudiante:
        raise HTTPException(status_code=404, detail="estudiante no encontrado")
    return {"mensaje": "estudiante eliminado"}
