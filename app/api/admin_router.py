from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.admin_schema import UsuarioCreate, UsuarioUpdate, UsuarioResponse
from app.crud import admin_crud

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)


@router.get("/", response_model=list[UsuarioResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    """Obtener todos los usuarios"""
    return admin_crud.get_all(db)


@router.get("/{numero_identificacion}", response_model=UsuarioResponse)
def obtener_usuario(numero_identificacion: str, db: Session = Depends(get_db)):
    """Buscar usuario por número de identificación"""
    user = admin_crud.get_by_numero(db, numero_identificacion)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user


@router.post("/", response_model=UsuarioResponse, status_code=201)
def crear_usuario(usuario_in: UsuarioCreate, db: Session = Depends(get_db)):
    """Crear un nuevo usuario"""
    return admin_crud.create(db, usuario_in)


@router.put("/{numero_identificacion}", response_model=UsuarioResponse)
def actualizar_usuario(numero_identificacion: str, data: UsuarioUpdate, db: Session = Depends(get_db)):
    """Actualizar usuario por número de identificación"""
    return admin_crud.update_by_numero(db, numero_identificacion, data)


@router.delete("/{numero_identificacion}")
def eliminar_usuario(numero_identificacion: str, db: Session = Depends(get_db)):
    """Eliminar usuario por número de identificación"""
    return admin_crud.delete_by_numero(db, numero_identificacion)
