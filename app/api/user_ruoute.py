from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.schemas.user_schema import UsuarioCreate, UsuarioResponse
from app.crud import user_crud
from app.dependencies.db import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.get("/", response_model=List[UsuarioResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    return user_crud.get_all(db)

@router.get("/{user_id}", response_model=UsuarioResponse)
def obtener_usuario(user_id: int, db: Session = Depends(get_db)):
    user = user_crud.get_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

@router.post("/", response_model=UsuarioResponse)
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return user_crud.create(db, usuario)

@router.put("/{user_id}", response_model=UsuarioResponse)
def actualizar_usuario(user_id: int, usuario: UsuarioCreate, db: Session = Depends(get_db)):
    user = user_crud.update(db, user_id, usuario)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

@router.delete("/{user_id}")
def eliminar_usuario(user_id: int, db: Session = Depends(get_db)):
    user = user_crud.delete(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"mensaje": "Usuario eliminado"}
