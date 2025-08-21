from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.schemas.estudiante_schema import UsuarioCreate, UsuarioResponse, UsuarioUpdate
from app.crud import estudiante_crud
from app.dependencies.db import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.get("/", response_model=List[UsuarioResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    return estudiante_crud.get_all(db)

@router.get("/{numero_identificacion}", response_model=UsuarioResponse)
def obtener_usuario(numero_identificacion: str, db: Session = Depends(get_db)):
    estudiante = estudiante_crud.get_by_numero(db, numero_identificacion)
    if not estudiante:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return estudiante

@router.post("/", response_model=UsuarioResponse)
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return estudiante_crud.create(db, usuario)

@router.put("/{numero_identificacion}", response_model=UsuarioResponse)
def actualizar_usuario(numero_identificacion: str, usuario: UsuarioUpdate, db: Session = Depends(get_db)):
    estudiante = estudiante_crud.update_by_numero(db, numero_identificacion, usuario)
    if not estudiante:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return estudiante

@router.delete("/{numero_identificacion}")
def eliminar_usuario(numero_identificacion: str, db: Session = Depends(get_db)):
    estudiante = estudiante_crud.delete_by_numero(db, numero_identificacion)
    if not estudiante:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"mensaje": "Usuario eliminado"}
