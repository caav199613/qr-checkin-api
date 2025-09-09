from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.token import crear_token
from app.schemas.admin_schema import AdminCreate, AdminUpdate, AdminResponse, AdminLogin
from app.crud import admin_crud

import bcrypt
 
router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


@router.get("/", response_model=list[AdminResponse])
def listar_admin(db: Session = Depends(get_db)):
    """Obtener todos los usuarios"""
    return admin_crud.get_all(db)


@router.get("/{usuario}", response_model=AdminResponse)
def obtener_usuario(usuario: str, db: Session = Depends(get_db)):
    """Buscar usuario por número de identificación"""
    user = admin_crud.get_by_usuario(db, usuario)
    if not user:
        raise HTTPException(status_code=404, detail="Admin no encontrado")
    return user


@router.post("/", response_model=AdminResponse, status_code=201)
def crear_usuario(usuario_in: AdminCreate, db: Session = Depends(get_db)):
    """Crear un nuevo usuario"""
    return admin_crud.create(db, usuario_in)


@router.put("/{usuario}", response_model=AdminResponse)
def actualizar_usuario(usuario: str, data: AdminUpdate, db: Session = Depends(get_db)):
    """Actualizar usuario por número de identificación"""
    return admin_crud.update_by_usuario(db, usuario, data)


@router.delete("/{usuario}")
def eliminar_usuario(usuario: str, db: Session = Depends(get_db)):
    """Eliminar usuario por número de identificación"""
    return admin_crud.delete_by_usuario(db, usuario)

@router.post("/login")
def login(body: AdminLogin, db: Session = Depends(get_db)):
    """
    Verifica credenciales de Admin. Retorna 200 si coinciden.
    """
    ok = admin_crud.verify_credentials(db, body.usuario, body.contrasena)
    if not ok:
        raise HTTPException(status_code=401, detail="Credenciales inválidas.")
    # Aquí podrías devolver un JWT; por ahora solo confirmamos autenticación.
    token = crear_token(body.usuario)
    return {"access_token": token, "token_type": "bearer"}