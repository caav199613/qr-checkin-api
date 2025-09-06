from sqlalchemy.orm import Session
from app.models.admin import Usuario
from app.schemas.admin_schema import UsuarioCreate, UsuarioUpdate
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException


def get_all(db: Session):
    """Obtener todos los usuarios"""
    return db.query(Usuario).all()


def get_by_numero(db: Session, numero_identificacion: str):
    """Buscar usuario por número de identificación"""
    return db.query(Usuario).filter(
        Usuario.numero_identificacion == numero_identificacion
    ).first()


def get_by_correo(db: Session, correo: str):
    """Buscar usuario por correo"""
    return db.query(Usuario).filter(Usuario.correo == correo).first()


def create(db: Session, usuario_in: UsuarioCreate):
    """Crear un usuario nuevo"""
    # Validar duplicados
    if get_by_numero(db, usuario_in.numero_identificacion):
        raise HTTPException(status_code=409, detail="El número de identificación ya está registrado.")

    if get_by_correo(db, usuario_in.correo):
        raise HTTPException(status_code=409, detail="El correo ya está registrado.")
    
    # Crear instancia
    user = Usuario(**usuario_in.model_dump())  # Pydantic v2
    db.add(user)

    try:
        db.commit()
        db.refresh(user)
        return user
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Error de integridad: número de identificación o correo duplicado.")


def update_by_numero(db: Session, numero_path: str, data: UsuarioUpdate):
    """Actualizar usuario por número de identificación"""
    user = db.query(Usuario).filter(Usuario.numero_identificacion == numero_path).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # 🚫 No permitir cambiar el número de identificación
    if "numero_identificacion" in data.model_dump(exclude_unset=True):
        raise HTTPException(status_code=400, detail="No se permite cambiar el número de identificación")

    # ✅ Validar correo solo si lo cambió
    if data.correo and data.correo != user.correo:
        if get_by_correo(db, data.correo):
            raise HTTPException(status_code=409, detail="El correo ya está registrado.")

    # ✅ Actualizar solo los campos enviados
    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(user, k, v)

    try:
        db.commit()
        db.refresh(user)
        return user
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Error de integridad al actualizar el usuario.")


def delete_by_numero(db: Session, numero_identificacion: str):
    """Eliminar usuario por número de identificación"""
    user = get_by_numero(db, numero_identificacion)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    db.delete(user)
    db.commit()
    return {"detail": "Usuario eliminado"}
