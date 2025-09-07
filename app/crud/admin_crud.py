from sqlalchemy.orm import Session
from app.models.admin import Admin
from app.schemas.admin_schema import AdminCreate, AdminUpdate
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException


def get_all(db: Session):
    """Obtener todos los admins"""
    return db.query(Admin).all()


def get_by_usuario(db: Session, usuario: str):
    """Buscar admin por número de identificación"""
    return db.query(Admin).filter(
        Admin.usuario == usuario
    ).first()

def create(db: Session, admin_in: AdminCreate):
    """Crear un admin nuevo"""
    # Validar duplicados
    if get_by_usuario(db, admin_in.usuario):
        raise HTTPException(status_code=409, detail="El número de identificación ya está registrado.")

    # Crear instancia
    user = Admin(**admin_in.model_dump())  # Pydantic v2
    db.add(user)

    try:
        db.commit()
        db.refresh(user)
        return user
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Error de integridad: número de identificación o correo duplicado.")


def update_by_usuario(db: Session, usuario: str, data: AdminUpdate):
    """Actualizar admin por número de identificación"""
    user = db.query(Admin).filter(Admin.usuario == usuario).first()
    if not user:
        raise HTTPException(status_code=404, detail="Admin no encontrado")

    # Actualizar solo los campos enviados
    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(user, k, v)

    try:
        db.commit()
        db.refresh(user)
        return user
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Error de integridad al actualizar el admin.")


def delete_by_usuario(db: Session, usuario: str):
    """Eliminar admin por número de identificación"""
    admin = get_by_usuario(db, usuario)
    if not admin:
        raise HTTPException(status_code=404, detail="Admin no encontrado")

    db.delete(admin)
    db.commit()
    return {"detail": "Admin eliminado"}
